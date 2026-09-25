#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

parser = argparse.ArgumentParser(description="Configure Yormio legal/support site placeholders.")
parser.add_argument("--operator", help="Legal person/company operating Yormio")
parser.add_argument("--email", help="Public support/privacy email")
parser.add_argument("--origin", help="Public HTTPS site origin, without trailing slash")
parser.add_argument("--check", action="store_true", help="Only report unresolved placeholders")
args = parser.parse_args()

replacements: dict[str, str] = {}

if args.operator is not None:
    operator = args.operator.strip()
    if not operator or len(operator) > 160:
        raise SystemExit("Invalid --operator")
    replacements["__LEGAL_OPERATOR__"] = operator

if args.email is not None:
    email = args.email.strip()
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        raise SystemExit("Invalid --email")
    replacements["__SUPPORT_EMAIL__"] = email

if args.origin is not None:
    origin = args.origin.strip().rstrip("/")
    parsed = urlparse(origin)
    if parsed.scheme != "https" or not parsed.netloc or parsed.path not in ("", "/"):
        raise SystemExit("--origin must be an HTTPS origin such as https://yormio.netlify.app")
    replacements["__SITE_ORIGIN__"] = origin

if not args.check and not replacements:
    parser.error("provide at least one of --operator, --email, --origin, or use --check")

changed = []
if not args.check:
    for path in PUBLIC.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = content
        for key, value in replacements.items():
            updated = updated.replace(key, value)
        if updated != content:
            path.write_text(updated, encoding="utf-8")
            changed.append(path.relative_to(ROOT))

all_tokens = ("__LEGAL_OPERATOR__", "__SUPPORT_EMAIL__", "__SITE_ORIGIN__")
remaining = []
for path in PUBLIC.rglob("*"):
    if not path.is_file():
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for token in all_tokens:
        if token in content:
            remaining.append(f"{path.relative_to(ROOT)}: {token}")

if not args.check:
    print(f"Updated {len(changed)} files.")
if remaining:
    print("Unresolved placeholders:")
    print("\n".join(remaining))
    raise SystemExit(2 if args.check else 0)
print("No unresolved production placeholders found.")
