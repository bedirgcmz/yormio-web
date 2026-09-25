# Yormio store submission checklist

Website-specific checklist for the first release.

## Before the first Netlify production deploy

- [ ] Replace `__LEGAL_OPERATOR__` with the individual developer's exact legal/public operator name.
- [ ] Replace `__SUPPORT_EMAIL__` with an operational public support/privacy email.
- [ ] After Netlify creates the site, replace `__SITE_ORIGIN__` with the final stable HTTPS origin.
- [ ] Add the official Yormio logo/icon exports to `public/assets/branding/` if image branding is desired.
- [ ] Run `python3 scripts/configure.py --check` and confirm no production placeholders remain.
- [ ] Test `/`, `/privacy/`, `/terms/`, `/support/`, `/account-deletion/`, `/request-received/`, and a 404 path.
- [ ] Submit one Support form and one Account Deletion form and confirm Netlify receives both.
- [ ] Configure Netlify form notifications so requests cannot be missed.

## Apple App Store Connect

- [ ] Privacy Policy URL -> `/privacy/`
- [ ] Support URL -> `/support/`
- [ ] User Privacy Choices URL -> `/account-deletion/` (optional but useful)
- [ ] Complete App Privacy answers so they match the actual app and third-party SDK/data flows.
- [ ] Ensure the subscription purchase screen and metadata contain working Privacy Policy and Terms links.
- [ ] Complete EU Digital Services Act trader-status declaration before EU distribution.
- [ ] Review Sign in with Apple account deletion/token revocation implementation before submission.

## Google Play Console

- [ ] Privacy Policy URL -> `/privacy/`
- [ ] Account deletion web URL -> `/account-deletion/`
- [ ] Complete Data Safety answers so they match the actual app and third-party SDK/data flows.
- [ ] Verify public developer/support email and developer profile details.
- [ ] If the personal developer account was created after 13 Nov 2023, confirm the required closed-test/production-access status.

## In the Yormio mobile app

- [ ] Settings Privacy opens `/privacy/`.
- [ ] Settings Terms opens `/terms/`.
- [ ] Settings Support opens `/support/`.
- [ ] Account deletion remains directly available in-app.
- [ ] Paywall Privacy and Terms links work.
- [ ] Subscription management/cancel/restore actions work and account deletion clearly states that it does not cancel store billing.

## Ongoing

- [ ] Update the website when providers, data retention, account flows, Premium fair-use policy, or subscription features materially change.
- [ ] Keep the public support/privacy email monitored.
