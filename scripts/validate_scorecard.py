#!/usr/bin/env python3
"""Validate and deterministically Pareto-rank game-design scorecards."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

EVIDENCE = {"hypothesis", "ai_pre_score", "expert_review", "prototype_observation", "player_evidence"}
CONFIDENCE = {"low", "medium", "high"}
AXES = ("game_experience", "research_validity", "development_feasibility")


def dominates(a: dict, b: dict) -> bool:
    av = [a["scores"][k] for k in AXES]
    bv = [b["scores"][k] for k in AXES]
    return all(x >= y for x, y in zip(av, bv)) and any(x > y for x, y in zip(av, bv))


def validate_candidate(c: dict, seen: set[str]) -> list[str]:
    errors: list[str] = []
    cid = str(c.get("id", "")).strip()
    if not cid:
        errors.append("candidate id is required")
    elif cid in seen:
        errors.append(f"duplicate candidate id: {cid}")
    seen.add(cid)
    if not str(c.get("name", "")).strip():
        errors.append(f"{cid}: name is required")
    gates = c.get("hard_gates")
    if not isinstance(gates, dict) or not gates:
        errors.append(f"{cid}: hard_gates must be a non-empty object")
    elif any(not isinstance(v, bool) for v in gates.values()):
        errors.append(f"{cid}: every hard gate must be boolean")
    scores = c.get("scores", {})
    for axis in AXES:
        value = scores.get(axis)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 100:
            errors.append(f"{cid}: {axis} must be 0-100")
    if c.get("evidence_level") not in EVIDENCE:
        errors.append(f"{cid}: invalid evidence_level")
    if c.get("confidence") not in CONFIDENCE:
        errors.append(f"{cid}: invalid confidence")
    if c.get("evidence_level") in {"hypothesis", "ai_pre_score"} and c.get("confidence") == "high":
        errors.append(f"{cid}: AI-only evidence cannot have high confidence")
    return errors


def pareto_rank(candidates: list[dict]) -> list[dict]:
    eligible = [c for c in candidates if all(c["hard_gates"].values())]
    remaining = eligible[:]
    ranked: list[dict] = []
    front_number = 1
    while remaining:
        front = [c for c in remaining if not any(dominates(other, c) for other in remaining if other is not c)]
        front.sort(
            key=lambda c: (
                -min(c["scores"][k] for k in AXES),
                -sum(c["scores"][k] for k in AXES) / len(AXES),
                str(c["id"]),
            )
        )
        for c in front:
            item = dict(c)
            item["pareto_front"] = front_number
            item["minimum_dimension"] = min(c["scores"][k] for k in AXES)
            item["mean_score"] = round(sum(c["scores"][k] for k in AXES) / len(AXES), 2)
            ranked.append(item)
        remaining = [c for c in remaining if c not in front]
        front_number += 1
    return ranked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        print("scorecard must contain a non-empty candidates list", file=sys.stderr)
        return 2
    seen: set[str] = set()
    errors = [e for c in candidates for e in validate_candidate(c, seen)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 2
    result = {
        "ranking_method": "pareto_front_then_minimum_dimension_then_mean_then_id",
        "ranked": pareto_rank(candidates),
        "eliminated": [c for c in candidates if not all(c["hard_gates"].values())],
    }
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
