# Yormio Web — Legal & Support

Static, privacy-first legal/support website for Yormio. It is designed for Netlify and contains no runtime framework, analytics tracker, ad pixel or client-side JavaScript.

## Public routes

- `/` — legal/support hub
- `/privacy/` — Privacy Policy
- `/terms/` — Terms of Use
- `/support/` — Support URL + Netlify support form
- `/account-deletion/` — external account-deletion request resource + Netlify form
- `/request-received/` — form confirmation page

## 1. Configure production identity

The generated files intentionally contain three production placeholders. Yormio is currently operated by an individual developer, so `__LEGAL_OPERATOR__` should be replaced with that person's exact legal/public operator name:

- `__LEGAL_OPERATOR__`
- `__SUPPORT_EMAIL__`
- `__SITE_ORIGIN__`

You can configure these in stages. For example, set the operator and support email before the site has a URL:

```bash
python3 scripts/configure.py --operator "YOUR EXACT LEGAL NAME" --email "YOUR SUPPORT EMAIL"
```

After Netlify gives you the production URL:

```bash
python3 scripts/configure.py --origin "https://YOUR-SITE.netlify.app"
```

Before release, verify that nothing remains unresolved:

```bash
python3 scripts/configure.py --check
```

## 2. Add the official Yormio branding assets

This repository is self-contained and does not depend on the mobile-app repository. Put final exported logo/icon files directly in `public/assets/branding/`. Placeholder SVG files and naming guidance are already included there.

The public pages intentionally use a CSS/text Yormio mark until you explicitly wire the official image assets, so an accidental deploy never presents an invented logo.

## 3. Preview locally

```bash
cd public
python3 -m http.server 8088
```

Open `http://localhost:8088`.

## 4. Deploy to Netlify

### Git-based deploy

Create a new repository (for example `yormio-web`), push this project, then create a Netlify site from the repo. `netlify.toml` publishes the `public` directory.

### Netlify Drop

After running the configure and branding steps, you can also drag the `public/` folder into Netlify Drop.

## Netlify Forms

`support` and `account-deletion` are static Netlify Forms. After the first Netlify deployment, verify both forms appear in Netlify's Forms section and submit one test request from each route. Configure form-notification email delivery in Netlify if desired.

The Privacy Policy explicitly discloses that Netlify receives data submitted through these forms.

## Store metadata mapping

Use the final stable HTTPS URLs:

- Apple Privacy Policy URL → `https://YOUR-DOMAIN/privacy/`
- Apple Support URL → `https://YOUR-DOMAIN/support/`
- Apple User Privacy Choices URL (optional but useful) → `https://YOUR-DOMAIN/account-deletion/`
- Google Play Privacy Policy → `https://YOUR-DOMAIN/privacy/`
- Google Play account deletion web resource → `https://YOUR-DOMAIN/account-deletion/`
- In-app paywall Terms → `https://YOUR-DOMAIN/terms/`

## Important product audit notes

See `docs/AUDIT_NOTES.md`. In particular, the website follows the newer migration-backed Premium policy: Unlimited AI is subject to a current server-side fair-use limit of 100 chargeable operations per rolling 24 hours. Older PRD/ADR references to 200/month are stale.

Before store submission, the app/backend still needs an Apple Sign in token-revocation review during account deletion. The inspected `delete-account` function deletes the Supabase user but does not show an explicit Apple token-revocation call.

## Legal review

This project is written to accurately reflect the audited Yormio implementation and current store requirements. It is not a substitute for jurisdiction-specific legal advice. If Yormio's operating entity, providers, features, retention or data flows change, review the policy before deployment.

## Release checklist

See `docs/STORE_SUBMISSION_CHECKLIST.md` for the final Apple/Google/Netlify wiring checklist.
