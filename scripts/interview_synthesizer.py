#!/usr/bin/env python3
"""Lightweight interview text helper for Claude Code PM Kit."""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path


STOPWORDS = {
    "the",
    "and",
    "for",
    "that",
    "this",
    "with",
    "you",
    "are",
    "was",
    "were",
    "have",
    "has",
    "not",
    "but",
    "they",
    "our",
    "your",
    "their",
    "就是",
    "一个",
    "我们",
    "他们",
    "这个",
    "那个",
    "因为",
    "所以",
    "如果",
    "没有",
    "可以",
}


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}|[\u4e00-\u9fff]{2,}", text.lower())
    return [token for token in tokens if token not in STOPWORDS]


def notable_lines(text: str, limit: int) -> list[str]:
    signals = ("痛", "难", "慢", "麻烦", "担心", "失败", "错误", "cost", "slow", "hard", "confusing", "risk")
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if len(line) < 8:
            continue
        if any(signal in line.lower() for signal in signals):
            lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract lightweight interview themes.")
    parser.add_argument("path", help="Interview transcript or notes text file.")
    parser.add_argument("--top", type=int, default=20, help="Number of frequent terms to show.")
    parser.add_argument("--quotes", type=int, default=8, help="Number of notable lines to show.")
    args = parser.parse_args()

    try:
        text = Path(args.path).read_text(encoding="utf-8")
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    counts = collections.Counter(tokenize(text))
    quotes = notable_lines(text, args.quotes)

    print("# Interview Synthesis Helper\n")
    print("## Frequent Terms\n")
    for token, count in counts.most_common(args.top):
        print(f"- {token}: {count}")

    print("\n## Notable Lines\n")
    if quotes:
        for line in quotes:
            print(f"- {line}")
    else:
        print("- No obvious pain/risk lines detected. Ask Claude to analyze the full transcript.")

    print("\n## Prompt For Claude\n")
    print(
        "请基于访谈文本提炼：1. 主要痛点主题；2. 每个主题的原话证据；"
        "3. 用户现有替代方案；4. 机会点；5. 证据强弱和样本偏差；6. 下一步研究问题。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
