#!/usr/bin/env python3
"""Find bundled AWS SVG assets without guessing paths or artwork sizes."""
import argparse
import json
from pathlib import Path
import re

ALIASES = {
    "s3": "simple storage service", "kms": "key management service",
    "ec2": "elastic compute cloud", "sqs": "simple queue service",
    "sns": "simple notification service", "vpc": "virtual private cloud",
    "efs": "elastic file system", "ebs": "elastic block store",
    "eks": "elastic kubernetes service", "ecs": "elastic container service",
    "elb": "elastic load balancing",
}


def words(value):
    return re.findall(r"[a-z0-9]+", value.lower())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="All words must occur in the asset name or category")
    parser.add_argument("--kind", choices=["service", "resource", "general", "group", "category"])
    parser.add_argument("--variant", type=int, choices=[16, 32, 48, 64])
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--include-dark", action="store_true")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    terms = words(args.query)
    if not terms:
        parser.error("query must contain a word or number")
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "assets/icon-index.json").read_text(encoding="utf-8"))
    matches = []
    for item in catalog["icons"]:
        if args.kind and item["kind"] != args.kind:
            continue
        if args.variant and item["variant"] != args.variant:
            continue
        if item["theme"] == "dark" and not args.include_dark:
            continue
        haystack = set(words(item["name"] + " " + item["category"]))
        for alias, expansion in ALIASES.items():
            if set(words(expansion)).issubset(haystack):
                haystack.add(alias)
        if not all(term in haystack for term in terms):
            continue
        matches.append(item)
    matches.sort(key=lambda item: (
        0 if item.get("source_slide") == 25 else 1,
        0 if item["variant"] == 64 and item["kind"] == "service" else 1,
        item["name"].lower(), item["path"]
    ))
    selected = []
    for item in matches[:args.limit]:
        path = root / item["path"]
        if not path.is_file():
            raise FileNotFoundError(f"Catalog asset is missing: {path}")
        selected.append({**item, "absolute_path": str(path)})
    print(json.dumps({"release": catalog["release"], "total_matches": len(matches),
                      "matches": selected}, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
