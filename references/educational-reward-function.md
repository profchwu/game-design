# Educational reward function

Use this reference for educational, training, assessment, or research games. The function is a transparent design diagnostic, not a claim that a game is effective and not a replacement for formal learning outcomes.

## Developer priority interview

Before candidate generation or scoring, ask the developer:

1. Which two positive factors matter most: **L** Learning, **E** Engagement, **M** Motivation/self-efficacy, or **A** Appropriate challenge/flow?
2. Allocate 100 percentage points across L/E/M/A, or choose a preset profile.
3. How severe should the maximum penalties be for **G** Guessing/exploitation and **C** Cognitive overload: 0-30 points each?
4. Should either G or C become a hard gate? If yes, set the threshold before seeing candidate scores.
5. What observable data will provide each component value?

Do not ask the developer to choose weights after revealing candidate scores. If the developer does not answer, use the Balanced baseline, label it as an assumption, and invite later revision before scoring begins.

## Variables

Score every component from 0 to 100 using observable evidence:

| Code | Construct | Example evidence |
| --- | --- | --- |
| L | Learning outcome | pre/post change, concept accuracy, strategy quality, misconception reduction |
| E | Engagement | completion, voluntary replay, persistence, return rate, time-on-task interpreted with context |
| M | Motivation and self-efficacy | brief validated items about competence, willingness to retry, and challenge seeking |
| A | Appropriate challenge and flow | ability-difficulty match, recoverable failure, boredom/frustration balance |
| G | Guessing or exploit behavior | random clicking, answer copying, rapid skipping, hint dependence without reasoning |
| C | Cognitive overload | confusion reports, instruction rereads, excessive errors, inability to explain the task |

Do not treat time-on-task alone as engagement, or speed alone as learning.

## Deterministic calculation

The conceptual form is:

`R_edu = wL*L + wE*E + wM*M + wA*A - pG*G - pC*C`

Implementation requirements:

- L/E/M/A/G/C are bounded to 0-100.
- Positive weights `wL + wE + wM + wA = 1.00`.
- Penalty coefficients `pG` and `pC` are each 0.00-0.30.
- `R_edu = clamp(positive_score - guessing_penalty - overload_penalty, 0, 100)`.
- Compute this with rules or code. An LLM may explain the result but must not choose runtime scores.

## Preset profiles

These are transparent starting values, not universal research constants.

| Profile | wL | wE | wM | wA | pG | pC | Use when |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Balanced baseline | 0.40 | 0.20 | 0.15 | 0.25 | 0.15 | 0.10 | no priority has been chosen yet |
| Learning-first | 0.50 | 0.15 | 0.10 | 0.25 | 0.15 | 0.10 | formal learning is the dominant purpose |
| Engagement-first | 0.35 | 0.30 | 0.15 | 0.20 | 0.15 | 0.10 | initial adoption and voluntary replay matter more |
| Accessibility-sensitive | 0.40 | 0.15 | 0.15 | 0.30 | 0.15 | 0.20 | overload and ability-difficulty fit are high risks |

## Default interpretation and review flags

- `R_edu >= 75`: promising enough to prototype, subject to G/R/D and evidence quality.
- `R_edu 60-74.99`: revise the weakest component or test the largest uncertainty.
- `R_edu < 60`: do not advance without a written exception.
- `G >= 60`: integrity review flag; inspect guessing, copying, skipping, or reward exploitation.
- `C >= 70`: overload review flag; simplify presentation or scaffold the task.

These thresholds are configurable before scoring. They are not validated universal cutoffs.

## Example

Balanced baseline with `L=82, E=74, M=68, A=76, G=20, C=30`:

- positive score = `0.40*82 + 0.20*74 + 0.15*68 + 0.25*76 = 76.8`
- guessing penalty = `0.15*20 = 3.0`
- overload penalty = `0.10*30 = 3.0`
- `R_edu = 70.8` → revise/test range

## Research safeguards

- Keep `R_edu` separate from formal outcomes such as CADS or a validated post-test.
- Freeze weights, component definitions, event mappings, and thresholds before formal data collection.
- Do not optimize the game directly against the formal study post-test.
- Store raw component values, weights, penalties, version, evidence label, and calculation result so the score can be recomputed.
- When L is unavailable before playtesting, label it as a hypothesis or AI pre-score; do not imply measured learning.
