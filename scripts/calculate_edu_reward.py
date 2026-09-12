#!/usr/bin/env python3
"""Calculate a deterministic educational-game reward diagnostic from JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PROFILES = {
    "balanced": {"L": 0.40, "E": 0.20, "M": 0.15, "A": 0.25, "G": 0.15, "C": 0.10},
    "learning_first": {"L": 0.50, "E": 0.15, "M": 0.10, "A": 0.25, "G": 0.15, "C": 0.10},
    "engagement_first": {"L": 0.35, "E": 0.30, "M": 0.15, "A": 0.20, "G": 0.15, "C": 0.10},
    "accessibility_sensitive": {"L": 0.40, "E": 0.15, "M": 0.15, "A": 0.30, "G": 0.15, "C": 0.20},
}


def bounded_score(value: object, name: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{name} must be numeric")
    value = float(value)
    if value < 0 or value > 100:
        raise ValueError(f"{name} must be between 0 and 100")
    return value


def calculate(payload: dict) -> dict:
    scores = payload.get("scores")
    if not isinstance(scores, dict):
        raise ValueError("scores must be an object")
    values = {key: bounded_score(scores.get(key), key) for key in "LEMAGC"}

    profile_name = payload.get("profile", "balanced")
    if profile_name == "custom":
        weights = payload.get("weights")
        if not isinstance(weights, dict):
            raise ValueError("custom profile requires weights")
        w = {key: float(weights.get(key)) for key in "LEMAGC"}
    else:
        if profile_name not in PROFILES:
            raise ValueError(f"unknown profile: {profile_name}")
        w = PROFILES[profile_name].copy()

    if abs(sum(w[key] for key in "LEMA") - 1.0) > 1e-9:
        raise ValueError("positive weights L/E/M/A must sum to 1.00")
    if any(w[key] < 0 or w[key] > 1 for key in "LEMA"):
        raise ValueError("positive weights must be between 0 and 1")
    if any(w[key] < 0 or w[key] > 0.30 for key in "GC"):
        raise ValueError("penalty coefficients G/C must be between 0 and 0.30")

    positive = sum(w[key] * values[key] for key in "LEMA")
    guessing_penalty = w["G"] * values["G"]
    overload_penalty = w["C"] * values["C"]
    reward = max(0.0, min(100.0, positive - guessing_penalty - overload_penalty))
    status = "prototype" if reward >= 75 else "revise" if reward >= 60 else "do_not_advance"

    return {
        "profile": profile_name,
        "scores": values,
        "weights": w,
        "positive_score": round(positive, 2),
        "guessing_penalty": round(guessing_penalty, 2),
        "overload_penalty": round(overload_penalty, 2),
        "R_edu": round(reward, 2),
        "status": status,
        "flags": {"integrity_review": values["G"] >= 60, "overload_review": values["C"] >= 70},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = calculate(payload)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
