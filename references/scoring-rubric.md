# G/R/D scoring rubric

Score each dimension from 0-100 and keep the dimensions separate.

## G - Game Experience

| Criterion | Points | Observable question |
| --- | ---: | --- |
| Learnability | 15 | Can a first-time player make a valid first action quickly? |
| Agency | 20 | Do materially different choices create different outcomes? |
| Tension and pacing | 20 | Does pressure rise without becoming chaotic? |
| Feedback and causality | 20 | Can players explain what changed and why? |
| Variety and replay value | 15 | Do situations demand adaptation rather than repetition? |
| Recovery and fairness | 10 | Can players recover from mistakes without a free reset? |

## R - Research Validity

| Criterion | Points | Observable question |
| --- | ---: | --- |
| Construct alignment | 25 | Does play measure the intended decision capability? |
| Confound control | 20 | Are motor speed, language, device, and prior genre skill controlled? |
| Determinism/reproducibility | 20 | Can the same inputs reproduce the same scored output? |
| Data traceability | 15 | Can outcomes be recomputed from versioned event records? |
| Assessment separation | 10 | Is formative feedback separated from formal assessment? |
| Ethical/accessibility safeguards | 10 | Are consent, anonymity, exclusion, and access needs handled? |

For a non-research entertainment game, replace R with **Purpose Fit** while preserving the separate-axis rule.

## D - Development Feasibility

| Criterion | Points | Observable question |
| --- | ---: | --- |
| Vertical-slice cost | 20 | Can the riskiest loop be tested cheaply? |
| Technology fit | 20 | Does the mechanic fit the platform and existing architecture? |
| Content scalability | 15 | Can levels vary without multiplying bespoke systems? |
| Art/motion/audio scope | 15 | Are asset requirements coherent and achievable? |
| Testability | 15 | Can rules, timing, localization, and data be regression-tested? |
| Maintainability | 15 | Are configuration, versions, and ownership clear? |

## Default thresholds

- Hard gates: all pass.
- G >= 75.
- R >= 85 for research games, or Purpose Fit >= 75 otherwise.
- D >= 75.

Thresholds may be changed before candidate generation. Never change them after seeing scores without recording the reason and rescoring all candidates.

## Educational reward diagnostic

For educational games, calculate the separate `R_edu` diagnostic defined in `educational-reward-function.md`. Do not average it into G, R, or D. Use it to expose tensions such as high engagement with low learning alignment, or strong learning tasks with excessive cognitive load. A developer may declare an `R_edu` threshold or G/C hard gate before candidate generation; record that choice and apply it to every candidate.

## Evidence and confidence

Use one evidence label: `hypothesis`, `ai_pre_score`, `expert_review`, `prototype_observation`, or `player_evidence`.

Confidence is `low`, `medium`, or `high` and reflects evidence quality, not enthusiasm. AI-only competition cannot exceed medium confidence.
