# Common workflows (agent playbook)

This file outlines typical Etsy shop-management tasks and the resources usually involved.
Exact parameters vary; consult the OpenAPI reference for the specific operation.

## 1) Listing lifecycle (draft → active)

Typical steps:

1. Create a draft listing (requires listings write scope)
2. Upload listing images (and optionally files/videos)
3. Configure inventory / offerings / variations
4. Update listing state to active

Agent guidance:

- Prefer creating drafts during testing to avoid accidental purchases and listing fees.
- When updating inventory, be careful: some inventory endpoints require full offering payloads.

## 2) Inventory sync

A safe sync loop usually needs:

- Read current listing inventory
- Compare with desired state
- Update inventory (often requires price + quantity per offering)

Agent guidance:

- Minimize calls by batching where possible.
- Do not “blind write” fields you didn't read; Etsy may treat omissions as clearing values.

## 3) Orders / receipts

Typical steps:

- List receipts for a shop (filter by status / date where available)
- Retrieve transactions for receipts
- Update fulfillment/shipping info where supported

Agent guidance:

- Receipts are sometimes called “orders” in docs and UI.

## 4) Shop configuration

Common operations:

- Read/update shop announcements and messages
- Manage shop sections
- Manage shipping profiles / processing profiles / return policies

Agent guidance:

- These operations are usually stable and good candidates for caching to reduce QPD usage.

## 5) Webhooks

Typical steps:

- Create a webhook endpoint (destination URL)
- Subscribe to events
- Verify signatures on inbound requests
- Handle retries idempotently

Agent guidance:

- Always treat webhook deliveries as at-least-once (dedupe by webhook id).
