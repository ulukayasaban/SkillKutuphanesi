// Windows are cohorts of sessions that START in the interval. This avoids
// attributing a half-turn to another prompt or treating missing starts as drops.
export function createAnalysisWindow({ days = null, since = null, until = null } = {}, now = new Date()) {
  if (days != null && since != null) throw new Error('Use either --days or --since, not both.');
  if (days != null && (!Number.isInteger(days) || days < 1 || days > 3650)) throw new Error('--days must be an integer from 1 to 3650.');
  const parse = value => {
    if (value == null) return null;
    if (!/^\d{4}-\d{2}-\d{2}(?:T.*)?$/.test(value) || !Number.isFinite(Date.parse(value))) throw new Error('Window dates must be ISO dates, such as 2026-09-01.');
    return new Date(value).toISOString();
  };
  const end = parse(until) || (days != null || since != null ? now.toISOString() : null);
  const start = days != null ? new Date(new Date(end).getTime() - days * 86400000).toISOString() : parse(since);
  if (start && end && start >= end) throw new Error('Window start must be before its end.');
  const kind = days != null ? 'rolling' : start || end ? 'range' : 'all';
  return { kind, days, start, end, basis: 'session-start', comparisonKey: kind === 'rolling' ? `rolling:${days}` : kind === 'all' ? 'all' : `range:${start || ''}:${until ? end : 'now'}` };
}

export function sessionInWindow(meta, window) {
  if (window.kind === 'all') return true;
  const timestamp = Date.parse(meta.timestamp);
  return Number.isFinite(timestamp) && (!window.start || timestamp >= Date.parse(window.start)) && (!window.end || timestamp < Date.parse(window.end));
}
