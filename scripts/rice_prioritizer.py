#!/usr/bin/env python3
"""Simple RICE prioritizer for Claude Code PM Kit."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


IMPACT_MAP = {
    "minimal": 0.25,
    "low": 0.5,
    "medium": 1.0,
    "high": 2.0,
    "massive": 3.0,
}
CONFIDENCE_MAP = {
    "low": 0.5,
    "medium": 0.8,
    "high": 1.0,
}
EFFORT_MAP = {
    "xs": 0.5,
    "s": 1.0,
    "m": 2.0,
    "l": 4.0,
    "xl": 8.0,
}


SAMPLE_ROWS = [
    {
        "name": "客户风险提醒",
        "reach": "1200",
        "impact": "high",
        "confidence": "medium",
        "effort": "m",
        "description": "帮助销售识别可能流失的客户",
    },
    {
        "name": "导出报表优化",
        "reach": "700",
        "impact": "medium",
        "confidence": "high",
        "effort": "s",
        "description": "减少每周手工整理时间",
    },
    {
        "name": "移动端仪表盘",
        "reach": "300",
        "impact": "high",
        "confidence": "low",
        "effort": "l",
        "description": "让管理者在手机端查看核心数据",
    },
]


def parse_score(value: str, mapping: dict[str, float], field: str) -> float:
    raw = (value or "").strip().lower()
    if raw in mapping:
        return mapping[raw]
    try:
        return float(raw)
    except ValueError as exc:
        allowed = ", ".join(mapping)
        raise ValueError(f"{field} must be numeric or one of: {allowed}") from exc


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"name", "reach", "impact", "confidence", "effort"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV missing required columns: {', '.join(sorted(missing))}")
        return list(reader)


def score_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    scored = []
    for row in rows:
        reach = parse_score(row["reach"], {}, "reach")
        impact = parse_score(row["impact"], IMPACT_MAP, "impact")
        confidence = parse_score(row["confidence"], CONFIDENCE_MAP, "confidence")
        effort = parse_score(row["effort"], EFFORT_MAP, "effort")
        if effort <= 0:
            raise ValueError(f"effort must be greater than zero for {row.get('name', '<unnamed>')}")
        rice = reach * impact * confidence / effort
        scored.append(
            {
                **row,
                "reach_value": reach,
                "impact_value": impact,
                "confidence_value": confidence,
                "effort_value": effort,
                "rice": rice,
            }
        )
    return sorted(scored, key=lambda item: item["rice"], reverse=True)


def print_markdown(rows: list[dict[str, object]], capacity: float | None) -> None:
    print("# RICE Prioritization\n")
    print("| Rank | Name | RICE | Reach | Impact | Confidence | Effort | Notes |")
    print("| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |")
    used_effort = 0.0
    for index, row in enumerate(rows, start=1):
        used_effort += float(row["effort_value"])
        notes = str(row.get("description") or "")
        if capacity is not None and used_effort > capacity:
            notes = f"Capacity overflow. {notes}".strip()
        print(
            f"| {index} | {row['name']} | {float(row['rice']):.2f} | "
            f"{float(row['reach_value']):.0f} | {float(row['impact_value']):.2f} | "
            f"{float(row['confidence_value']):.2f} | {float(row['effort_value']):.2f} | {notes} |"
        )
    if capacity is not None:
        print(f"\nTotal effort: {used_effort:.2f}; capacity: {capacity:.2f}")


def write_sample(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["name", "reach", "impact", "confidence", "effort", "description"],
        )
        writer.writeheader()
        writer.writerows(SAMPLE_ROWS)
    print(f"Wrote sample CSV to {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prioritize product ideas with RICE.")
    parser.add_argument("csv_path", help="CSV path, or 'sample' to write a sample CSV.")
    parser.add_argument("--sample-output", default="sample_features.csv")
    parser.add_argument("--capacity", type=float, default=None, help="Optional effort capacity.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown.")
    args = parser.parse_args()

    if args.csv_path == "sample":
        write_sample(Path(args.sample_output))
        return 0

    try:
        rows = score_rows(load_rows(Path(args.csv_path)))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print_markdown(rows, args.capacity)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
