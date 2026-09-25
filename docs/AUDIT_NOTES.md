# Yormio legal-site audit notes

Audit basis: the two Repomix packages supplied on 25 September 2026 plus current official Apple/Google policy verification.

## Current implementation used by the public legal text

- Local-first product store: manual reminders/lists are local SQLite data before account/cloud use.
- Supabase anonymous auth starts when a guest first requests AI.
- Permanent accounts can use Apple, Google and email flows in the inspected source.
- Linked-account product data can synchronize through Supabase.
- Voice recording is limited to 60 seconds on-device; local audio is deleted after processing/cancel/discard.
- `capture-parse` sends audio or pasted text to Google Gemini. Current server code does not persist raw audio to Supabase Storage and does not put raw audio/content in application logs.
- Raw transcript is not persisted by Yormio by default; confirmed structured product data is retained.
- RevenueCat uses the permanent Supabase UUID as App User ID. Yormio mirrors entitlement/product/store/status/expiration metadata server-side.
- Checklist share snapshots use a raw 64-hex token given to the user and a hash stored in Supabase. Current share expiry is 7 days.
- No analytics or Sentry SDK appears in the audited mobile `package.json`; the legal site is shipped without trackers.
- Netlify is added as a website processor because the site uses Netlify Forms for support and external deletion requests.

## Product-document drift found

Older ADR/PRD material still says Premium = 200 AI operations per UTC month. Migration `0020_premium_unlimited_fair_use.sql` is newer and explicitly changes Premium to marketed "Unlimited AI" with server-authoritative rolling 24-hour fair use. Current configured limit in that migration is 100 chargeable AI operations in a rolling 24-hour period. The legal site follows the newer backend policy.

## Do not claim as currently implemented

- Google Calendar mirror or Apple EventKit mirror as active production data flows. The inspected project tree/doc status indicates those provider mirrors are not a completed current V1 flow.
- Permanent storage of raw audio or raw transcripts.
- Advertising or analytics tracking that is not present in the audited dependency/implementation set.

## Store-review issue discovered outside the website

The inspected Supabase `delete-account` Edge Function authenticates the caller and deletes the Supabase Auth user via `auth.admin.deleteUser`. The inspected client then removes local account storage and signs out. No explicit Sign in with Apple token revocation is visible in that deletion path.

Apple's current account-deletion guidance says apps using Sign in with Apple need to revoke user tokens when deleting an account. Audit/fix this before final App Review submission.

## Values still required from product owner

These cannot be inferred safely from source code and are centralized as placeholders in the public files:

- legal operator/controller name
- public support/privacy email address
- final Netlify/custom-domain HTTPS origin
