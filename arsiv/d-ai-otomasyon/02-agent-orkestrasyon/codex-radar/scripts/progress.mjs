import { createHash } from 'node:crypto';

export function stableHash(value) {
  const normalize = item => Array.isArray(item) ? item.map(normalize) : item && typeof item === 'object'
    ? Object.fromEntries(Object.keys(item).sort().map(key => [key, normalize(item[key])])) : item;
  return createHash('sha256').update(JSON.stringify(normalize(value))).digest('hex');
}

export function contentLimits(humanMessages) {
  if (humanMessages < 12) return { observations: { min: 3, max: 6 }, suggestions: { min: 1, max: 3 } };
  if (humanMessages < 40) return { observations: { min: 4, max: 8 }, suggestions: { min: 1, max: 5 } };
  return { observations: { min: 5, max: 12 }, suggestions: { min: 1, max: 7 } };
}

export const METRICS = {
  'verification.coverage': { en: 'Edits followed by verification', zh: '改动后的验证覆盖率', direction: 'up', min: 0, max: 1, minSamples: 3 },
  'verification.passingCoverage': { en: 'Edits followed by passing verification', zh: '改动后的验证通过覆盖率', direction: 'up', min: 0, max: 1, minSamples: 3 },
  'verification.recoveryRate': { en: 'Failed verification recovered', zh: '验证失败后的恢复率', direction: 'up', min: 0, max: 1, minSamples: 3 },
  'commands.successRate': { en: 'Command success rate', zh: '命令成功率', direction: 'up', min: 0, max: 1, minSamples: 5 },
  'turns.cleanEndRatio': { en: 'Completed turns', zh: '回合完成比例', direction: 'up', min: 0, max: 1, minSamples: 5 },
  'messages.filePathRatio': { en: 'Requests naming files', zh: '明确目标文件的指令比例', direction: 'up', min: 0, max: 1, minSamples: 5 },
  'messages.constraintsRatio': { en: 'Requests with boundaries', zh: '明确约束的指令比例', direction: 'up', min: 0, max: 1, minSamples: 5 },
  'messages.verificationAskRatio': { en: 'Requests asking for verification', zh: '要求验证的指令比例', direction: 'up', min: 0, max: 1, minSamples: 5 },
  'corrections.substanceRatio': { en: 'Corrections with concrete context', zh: '提供具体上下文的纠偏比例', direction: 'up', min: 0, max: 1, minSamples: 3 },
  'project.hasAgentsMd': { en: 'Project instructions present', zh: '项目指引已建立', direction: 'up', type: 'boolean', minSamples: 1 },
  'project.hasTestsDir': { en: 'Test assets present', zh: '测试资产已建立', direction: 'up', type: 'boolean', minSamples: 1 },
  'workflow.toolsPerMessage': { en: 'Tool calls per user message', zh: '每条用户消息的工具调用数', direction: 'down', min: 0, max: 10000, minSamples: 5 },
  'workflow.compactionsPerSession': { en: 'Compactions per session', zh: '每个会话的压缩次数', direction: 'down', min: 0, max: 10000, minSamples: 3 }
};

export function metricSnapshot(facts) {
  const { stats: s, outcomeTotals: o, toolcraftSummary: t, signalsByPosition: p, projectAssets: a } = facts;
  const v = o.verification;
  const entries = {
    'verification.coverage': [v.coverage, v.editedSessions],
    'verification.passingCoverage': [v.passingCoverage, v.editedSessions],
    'verification.recoveryRate': [v.recoveryRate, v.failedSessions],
    'commands.successRate': [t.commandSuccessRate, t.commandSuccesses + t.commandFailures],
    'turns.cleanEndRatio': [o.cleanEndRatio, o.observedTurns],
    'messages.filePathRatio': [p.directing.ratios.filePath, s.humanMessages],
    'messages.constraintsRatio': [p.directing.ratios.constraints, s.humanMessages],
    'messages.verificationAskRatio': [p.directing.ratios.asksVerify, s.humanMessages],
    'corrections.substanceRatio': [p.correcting.substanceRatio, p.correcting.messageCount],
    'project.hasAgentsMd': [a.cwdResolved ? a.hasAgentsMd : null, a.cwdResolved ? 1 : 0],
    'project.hasTestsDir': [a.cwdResolved ? a.hasTestsDir : null, a.cwdResolved ? 1 : 0],
    'workflow.toolsPerMessage': [o.toolsPerHumanMsg, s.humanMessages],
    'workflow.compactionsPerSession': [s.sessions ? s.contextCompactions / s.sessions : null, s.sessions]
  };
  return {
    metrics: Object.fromEntries(Object.entries(entries).map(([key, [value, sampleSize]]) => [key, { value, sampleSize }])),
    observationCount: s.humanMessages + s.totalToolCalls + s.turnCompletes,
    sessionIds: facts.analyzedSessionIds || [],
    window: facts.analysisWindow
  };
}

export function validateVerification(value) {
  if (value == null) return [];
  const errors = [];
  const definition = METRICS[value.metric];
  if (!definition) return ['verification.metric must name a supported metric'];
  if (!['gte', 'lte', 'eq'].includes(value.operator)) errors.push('verification.operator must be gte, lte or eq');
  if (definition.type === 'boolean') {
    if (typeof value.target !== 'boolean' || value.operator !== 'eq') errors.push('boolean verification requires eq and a boolean target');
  } else if (!Number.isFinite(value.target) || value.target < definition.min || value.target > definition.max) {
    errors.push('verification.target is outside the metric range');
  }
  return errors;
}

export function trackedSuggestion(suggestion, snapshot) {
  const verification = suggestion.verification || null;
  return {
    id: suggestion.recipeId || stableHash({ dimension: suggestion.dimensionId, type: suggestion.type, verification }).slice(0, 16),
    metric: verification?.metric || null,
    operator: verification?.operator || null,
    target: verification?.target ?? null,
    baseline: verification ? snapshot.metrics[verification.metric]?.value ?? null : null,
    sampleSize: verification ? snapshot.metrics[verification.metric]?.sampleSize || 0 : 0
  };
}

export function comparisonKey(report) {
  const p = report.provenance;
  if (!p) return null;
  return stableHash({ formula: p.formulaVersion, rubric: p.rubricHash, parser: p.parserVersion, profile: report.profile?.type, window: p.window?.comparisonKey });
}

export function evaluateProgress(previous, current) {
  if (!previous?.tracking || !current.metricSnapshot) return [];
  const snapshot = current.metricSnapshot;
  const previousSnapshot = previous.metricSnapshot;
  const fresh = previous.provenance?.factsHash !== current.provenance?.factsHash && (
    snapshot.observationCount !== previousSnapshot?.observationCount
    || snapshot.sessionIds.some(id => !previousSnapshot?.sessionIds?.includes(id))
    || stableHash(snapshot.metrics) !== stableHash(previousSnapshot?.metrics || {})
  );
  return previous.tracking.filter(item => item.metric && METRICS[item.metric]).map(item => {
    const definition = METRICS[item.metric];
    const measured = snapshot.metrics[item.metric];
    const value = measured?.value ?? null;
    const enough = value !== null && measured.sampleSize >= definition.minSamples;
    const newEvidence = definition.type === 'boolean' ? value !== item.baseline : fresh;
    const met = value !== null && (item.operator === 'gte' ? value >= item.target : item.operator === 'lte' ? value <= item.target : value === item.target);
    let status = 'insufficient';
    if (enough && (newEvidence || met && item.baseline === value)) {
      const direction = definition.direction === 'up' ? 1 : -1;
      status = met ? 'met' : item.baseline == null ? 'measured' : (Number(value) - Number(item.baseline)) * direction > 0 ? 'improved' : value === item.baseline ? 'unchanged' : 'regressed';
    }
    return { ...item, label: { en: definition.en, zh: definition.zh }, current: value, sampleSize: measured?.sampleSize || 0, status };
  });
}
