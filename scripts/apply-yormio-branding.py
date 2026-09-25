#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if ROOT.name == 'scripts':
    ROOT = ROOT.parent
PUBLIC = ROOT / 'public'
CSS = PUBLIC / 'assets' / 'css' / 'styles.css'
BRANDING = PUBLIC / 'assets' / 'branding'

ASSETS = [
    'yormio-app-icon-light.png',
    'yormio-app-icon-dark.png',
    'yormio-lockup-primary-on-light-transparent.png',
    'yormio-lockup-primary-on-dark-transparent.png',
    'yormio-symbol-primary-on-light-transparent.png',
    'yormio-symbol-primary-on-dark-transparent.png',
]

FAVICON_BLOCK = '''  <link rel="icon" type="image/png" href="/assets/branding/yormio-app-icon-light.png" media="(prefers-color-scheme: light)">
  <link rel="icon" type="image/png" href="/assets/branding/yormio-app-icon-dark.png" media="(prefers-color-scheme: dark)">
  <link rel="apple-touch-icon" href="/assets/branding/yormio-app-icon-light.png">
'''

HEADER_OLD = '''      <a class="brand" href="/" aria-label="Yormio home">
        <span class="brand-dot" aria-hidden="true"></span>
        <span>Yormio</span>
      </a>'''
HEADER_NEW = '''      <a class="brand" href="/" aria-label="Yormio home">
        <picture class="brand-lockup" aria-hidden="true">
          <source media="(prefers-color-scheme: dark)" srcset="/assets/branding/yormio-lockup-primary-on-dark-transparent.png">
          <img src="/assets/branding/yormio-lockup-primary-on-light-transparent.png" alt="">
        </picture>
      </a>'''

FOOTER_OLD = '        <div class="brand footer-brand"><span class="brand-dot" aria-hidden="true"></span><span>Yormio</span></div>'
FOOTER_NEW = '''        <div class="brand footer-brand">
          <picture class="brand-lockup" aria-hidden="true">
            <source media="(prefers-color-scheme: dark)" srcset="/assets/branding/yormio-lockup-primary-on-dark-transparent.png">
            <img src="/assets/branding/yormio-lockup-primary-on-light-transparent.png" alt="">
          </picture>
        </div>'''

COMPACT_OLD = '<div class="brand"><span class="brand-dot" aria-hidden="true"></span><span>Yormio</span></div>'
COMPACT_NEW = '<div class="brand"><picture class="brand-lockup" aria-hidden="true"><source media="(prefers-color-scheme: dark)" srcset="/assets/branding/yormio-lockup-primary-on-dark-transparent.png"><img src="/assets/branding/yormio-lockup-primary-on-light-transparent.png" alt=""></picture></div>'

HERO_OLD = '''    <section class="hero shell">
      <div class="eyebrow">Yormio legal & support</div>'''
HERO_NEW = '''    <section class="hero shell hero-with-mark">
      <picture class="hero-brand-mark" aria-hidden="true">
        <source media="(prefers-color-scheme: dark)" srcset="/assets/branding/yormio-symbol-primary-on-dark-transparent.png">
        <img src="/assets/branding/yormio-symbol-primary-on-light-transparent.png" alt="">
      </picture>
      <div class="eyebrow">Yormio legal & support</div>'''

CSS_OLD_BRAND = '.brand { display: inline-flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 850; letter-spacing: -.4px; text-decoration: none; color: var(--ink); }\n.brand-dot { width: 22px; height: 22px; border-radius: 8px; background: radial-gradient(circle at 32% 28%, #48e0c5, var(--brand-strong) 58%, #075a53 100%); box-shadow: 0 8px 22px rgba(15,159,143,.25); }'
CSS_NEW_BRAND = '.brand { display: inline-flex; align-items: center; text-decoration: none; color: var(--ink); line-height: 0; }\n.brand-lockup { display: block; }\n.brand-lockup img { display: block; width: 152px; height: auto; }\n.footer-brand .brand-lockup img { width: 144px; }'
CSS_HERO_OLD = '.hero { padding: 96px 0 56px; max-width: 880px; }'
CSS_HERO_NEW = '.hero { padding: 96px 0 56px; max-width: 880px; }\n.hero-with-mark { position: relative; padding-right: 190px; }\n.hero-brand-mark { position: absolute; right: 4px; top: 76px; width: 142px; }\n.hero-brand-mark img { display: block; width: 100%; height: auto; filter: drop-shadow(0 18px 34px rgba(8,127,117,.14)); }'
CSS_MOBILE_OLD = '  .hero { padding-top: 62px; }'
CSS_MOBILE_NEW = '  .hero { padding-top: 62px; }\n  .hero-with-mark { padding-right: 0; }\n  .hero-brand-mark { position: static; width: 92px; margin-bottom: 24px; }'


def update_html(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    original = text

    if 'yormio-app-icon-light.png' not in text:
        pretty = '  <link rel="stylesheet" href="/assets/css/styles.css">'
        compact = '<link rel="stylesheet" href="/assets/css/styles.css">'
        if pretty in text:
            text = text.replace(pretty, FAVICON_BLOCK + pretty, 1)
        elif compact in text:
            icons = '<link rel="icon" type="image/png" href="/assets/branding/yormio-app-icon-light.png"><link rel="apple-touch-icon" href="/assets/branding/yormio-app-icon-light.png">'
            text = text.replace(compact, icons + compact, 1)

    text = text.replace(HEADER_OLD, HEADER_NEW)
    text = text.replace(FOOTER_OLD, FOOTER_NEW)
    text = text.replace(COMPACT_OLD, COMPACT_NEW)

    if path == PUBLIC / 'index.html' and 'hero-brand-mark' not in text:
        text = text.replace(HERO_OLD, HERO_NEW)

    if text != original:
        path.write_text(text, encoding='utf-8')
        return True
    return False


def update_css() -> bool:
    text = CSS.read_text(encoding='utf-8')
    original = text
    if '.brand-lockup img' not in text:
        text = text.replace(CSS_OLD_BRAND, CSS_NEW_BRAND)
    if '.hero-with-mark' not in text:
        text = text.replace(CSS_HERO_OLD, CSS_HERO_NEW)
        text = text.replace(CSS_MOBILE_OLD, CSS_MOBILE_NEW)
    if text != original:
        CSS.write_text(text, encoding='utf-8')
        return True
    return False


def main() -> int:
    if not PUBLIC.exists() or not CSS.exists():
        print('Run this script from the yormio-web project, or put it in yormio-web/scripts/.')
        return 1

    changed = []
    for html in sorted(PUBLIC.rglob('*.html')):
        if update_html(html):
            changed.append(str(html.relative_to(ROOT)))
    if update_css():
        changed.append(str(CSS.relative_to(ROOT)))

    print(f'Updated {len(changed)} files.' if changed else 'Branding markup is already up to date.')

    missing = [name for name in ASSETS if not (BRANDING / name).exists()]
    if missing:
        print('\nMissing assets. Copy these exact files into public/assets/branding/:')
        for name in missing:
            print(f'  - {name}')
        return 2

    print('\nAll required Yormio branding assets are present.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
