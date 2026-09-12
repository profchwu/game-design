# Competition protocol

## 1. Brief lock

Record audience, platform, learning or entertainment goal, session length, core subject, accessibility needs, research constraints, non-goals, and decision owner. Convert fixed constraints into pass/fail hard gates before generating candidates.

## 2. Candidate population

Generate 6-10 concepts that differ in core verb, pressure model, information model, failure model, and replay structure. Cosmetic reskins do not count as separate candidates. Assign neutral IDs (A, B, C...) and withhold a preferred winner during the first review.

Each concept must state:

- player fantasy and role;
- 30-60 second core loop;
- meaningful choice and trade-off;
- escalation and recovery;
- success/failure condition;
- expected session length;
- minimum prototype needed to test its riskiest assumption.

## 3. Blind review panel

Run five independent lenses. When independent agents are unavailable, run separated passes and do not let one lens revise another lens's score.

1. Game designer: depth, agency, tension, pacing, replayability.
2. First-time player: discoverability, cognitive load, feedback, accessibility.
3. Domain expert: causal accuracy, representation, misconceptions.
4. Research reviewer: construct validity, confounds, reproducibility, data integrity.
5. Production director: scope, assets, technology, schedule, maintenance.

Return concise findings and observable concerns. Do not expose private chain-of-thought.

## 4. Elimination

Eliminate any candidate that fails a hard gate. Keep its reason in the decision record. Do not rescue a hard-gate failure with a high average score.

## 5. Evolution

Create the next generation by one of these explicit operations:

- **retain**: preserve a mechanism that passed all gates;
- **simplify**: reduce rules or controls while preserving the decision;
- **mutate**: change one material variable to test a hypothesis;
- **recombine**: merge compatible mechanisms from two survivors;
- **specialize**: use a mechanism in only the level where it fits;
- **retire**: remove a mechanism whose risk cannot be tested cheaply.

Run 3-5 generations by default, but stop earlier when candidates converge and later generations no longer create a materially different testable hypothesis. A fixed generation count is not proof of optimization.

## 6. Final tournament

Reapply hard gates and G/R/D scoring. Rank with Pareto fronts. If candidates share a front, rank by the lowest dimension, then the mean of G/R/D, then lower prototype cost. Disclose all tie-breakers.

## 7. Human decision gate

Present the top three, eliminated concepts, uncertainties, and next tests. Offer approve, revise, or pause. Do not generate visual mockups or code until the user selects a gameplay direction.

## 8. Visual tournament

After gameplay approval, create three visual directions using identical content and game state. Compare readability, emotional tone, implementation fit, bilingual resilience, motion potential, and accessibility. Do not compare three different gameplay concepts disguised as art styles.

