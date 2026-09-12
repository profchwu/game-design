---
name: game-design
description: Run evidence-driven game concept tournaments for educational, research, or serious games when the user wants multiple AI-generated gameplay alternatives ranked before human approval, followed by visual style selection, prototyping, playtesting, and teaching artifacts. Do not use for ordinary game code bug fixes or asset-only edits.
metadata:
  creator: "National Tsing Hua University, Professor Chih-Hung Wu"
  version: "1.2.0"
---

# Game Design

Creator / 作者：National Tsing Hua University, Professor Chih-Hung Wu（國立清華大學 吳智鴻教授）  
Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved.

Use a competitive, evidence-labeled design process. The skill proposes and challenges alternatives; the user, teacher, or project owner makes every consequential selection.

繁體中文參考版請見 [references/zh-TW.md](references/zh-TW.md)。正式執行入口仍為本檔案，中文文件用於閱讀與教學，不是另一個獨立 Skill 入口。

## Select a mode

- **Production**: move from brief to a testable vertical slice.
- **Teaching**: expose scorecards, worksheets, reflection prompts, and assessment evidence.
- **Research game**: add validity, reproducibility, and version-freeze gates.

Infer the lightest suitable mode from the request. Combine Teaching and Research game when both apply.

## Non-negotiable sequence

1. Confirm the design brief and hard constraints. For an educational game, run the developer priority interview in [educational-reward-function.md](references/educational-reward-function.md): ask which of Learning, Engagement, Motivation/self-efficacy, and Appropriate challenge matters most; ask how strongly guessing/exploitation and cognitive overload should be penalized. Lock the selected profile before scoring candidates.
2. Research relevant successful games and domain evidence when current or factual grounding matters.
3. Generate 6-10 meaningfully different gameplay concepts. Assign neutral candidate IDs before scoring.
4. Run the blind tournament in [competition-protocol.md](references/competition-protocol.md).
5. Apply the independent G/R/D rubric in [scoring-rubric.md](references/scoring-rubric.md). Never hide a failed dimension inside one weighted total.
6. Return a ranked shortlist with evidence levels, risks, costs, and recommended tests. Stop for human selection.
7. After gameplay selection, create exactly three comparable visual directions using the same scene, content, and game state. Stop for visual selection.
8. After visual approval, build the smallest vertical slice, add motion/audio/art, and conduct player testing.
9. Iterate one material variable at a time; preserve versions and regression evidence.
10. Freeze the study build before formal data collection when Research game mode applies.

Do not start full implementation before the gameplay and visual approval gates. Silence is not approval.

## Evidence labels

Every substantive claim about a candidate must carry one of these labels:

- **Hypothesis** - untested design assumption.
- **AI pre-score** - structured model judgment, not player evidence.
- **Expert review** - attributable specialist assessment.
- **Prototype observation** - behavior observed in a controlled prototype session.
- **Player evidence** - measured participant data with sample and method.

Never describe an AI pre-score as proof that a game is fun, effective, or valid. Provide concise rationale and scorecards, not hidden reasoning transcripts.

## Educational reward-function rule

For educational games, read [educational-reward-function.md](references/educational-reward-function.md). Report the six normalized components and the deterministic `R_edu` diagnostic for every finalist. Keep `R_edu` separate from G/R/D: it may trigger a review or reveal a tradeoff, but it must not silently replace the independent axes or the formal learning outcome. Never let an LLM invent or modify a scored value at runtime.

## Required decision report

Return at least the top three and all hard-gate eliminations. For each finalist include:

- candidate ID and name;
- one-sentence fantasy and core loop;
- Game Experience, Research Validity, and Development Feasibility scores;
- for educational games, L/E/M/A/G/C component values, the locked weight profile, `R_edu`, and any integrity or overload flags;
- evidence level and confidence;
- strongest advantage and largest risk;
- comparable market patterns without copying protected assets;
- prototype scope and estimated complexity;
- next falsifiable test.

Use Pareto rank first. Use minimum-dimension score, then mean score, only as disclosed tie-breakers. The first-ranked candidate is a recommendation, not an automatic decision.

## Specialist routing after approval

- Use Design Thinking/SDLC guidance for briefs, gates, traceability, and acceptance.
- Use website/interface guidance for browser experience, responsiveness, and accessibility.
- Use image generation for original raster concept art and three style mockups.
- Use SVG/CSS/canvas for deterministic, interactive effects and functional graphics.
- Use Remotion for authored news, consequence, and recap video sequences, not as a substitute for interactive gameplay.
- Use browser testing for playable flow and localization QA.
- Specify audio behavior and licensing; do not claim a music-generation capability that is unavailable.

For the visual and motion handoff, read [visual-motion-pipeline.md](references/visual-motion-pipeline.md).

## Recommended companion skills

Use these companion skills only when the current task needs the corresponding capability and the skill is available in the environment:

- `sites:sites-building` - build browser-playable prototypes, responsive interfaces, dashboards, and accessible game hubs. Use `sites:sites-hosting` afterward when the approved prototype must be published.
- `visualize:visualize` - explore and compare visual directions, diagrams, maps, mockups, and interactive explanatory visuals.
- `imagegen` - create original raster concept art, sprites, textures, and transparent-background assets. Use SVG/CSS/canvas directly for deterministic interface graphics and interactive effects; there is no separate SVG-generation skill requirement.
- `remotion-best-practices` - create authored news, consequence, and recap video sequences for the game; it is not a substitute for interactive gameplay.
- `browser:control-in-app-browser` - test playable browser flows, responsive behavior, and localization.
- Background music and sound effects - no dedicated audio-generation skill is currently installed. When one is available, use it for original loops and effects with explicit duration, loop, intensity, stem, format, and licensing requirements; otherwise use licensed or user-provided audio assets and document their provenance.

## Installation

Install the complete Skill folder so `SKILL.md` is directly inside the `game-design` directory. Do not place only the zip file there and do not rename `SKILL.md`.

### Windows

1. Copy or extract the Skill contents to `%USERPROFILE%\.codex\skills\game-design\`.
2. Confirm that `%USERPROFILE%\.codex\skills\game-design\SKILL.md` exists.
3. Restart Codex or reload its Skill list.

For this project, the source folder is `C:\Users\user\Documents\Game-design\skill`; copy the contents of that folder, not the parent project folder.

### macOS/Linux

Copy or extract the Skill contents to `~/.codex/skills/game-design/`, or to `$CODEX_HOME/skills/game-design/` when `CODEX_HOME` is configured. The required final path is `.../game-design/SKILL.md`.

### Verify the installation

Run the Skill Creator validator against the installed folder:

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ~/.codex/skills/game-design
```

In the standard Codex installation, `<path-to-skill-creator>` is `~/.codex/skills/.system/skill-creator`.
The validator should report `Skill is valid!` before the Skill is used or distributed.

## Teaching mode

When the request is educational, read [teaching-mode.md](references/teaching-mode.md). Give learners the rubric before revealing the AI ranking. Keep student decisions, AI recommendations, and player evidence distinguishable.

## Research-game safeguards

When outcomes will support a paper, assessment, or formal study, read [research-game-gates.md](references/research-game-gates.md). Never optimize a candidate directly against the formal post-test score before the design and scoring rules are frozen.

## Reusable assets and validation

- Use [ranking-report-template.md](assets/ranking-report-template.md) for the decision report.
- Use [student-worksheet.md](assets/student-worksheet.md) and [instructor-rubric.md](assets/instructor-rubric.md) in Teaching mode.
- Use [course-learning-tasks.md](references/course-learning-tasks.md) and [Game-Design-Skill-課程學習任務與學習單.docx](assets/Game-Design-Skill-課程學習任務與學習單.docx) for a complete hands-on installation task plus guided course discussion.
- Reuse [Game-Design-Skill-說明書.docx](assets/Game-Design-Skill-說明書.docx) as the illustrated instructor manual when a complete reference is requested.
- Reuse [Game-Design-Skill-教學簡報.pptx](assets/Game-Design-Skill-教學簡報.pptx) for an instructor-led introduction; adapt examples only after preserving the approval gates and evidence rules.
- When a scorecard JSON is produced, run `scripts/validate_scorecard.py` to validate ranges, hard gates, evidence labels, and deterministic Pareto ordering.

## Attribution and copyright

This Skill was created by National Tsing Hua University, Professor Chih-Hung Wu（國立清華大學 吳智鴻教授）.

Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved. See [COPYRIGHT.md](COPYRIGHT.md) for the distribution notice.
