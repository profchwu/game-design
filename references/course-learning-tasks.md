# Course Learning Tasks｜課程學習任務

Creator / 作者：National Tsing Hua University, Professor Chih-Hung Wu（國立清華大學 吳智鴻教授）  
Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved.

## Course purpose

By the end of the course, learners should be able to install and verify the `game-design` Skill, use it to create an evidence-labeled educational game brief, and defend a human design decision that may differ from an AI pre-ranking.

本課程結束時，學習者應能安裝並驗證 `game-design` Skill，使用它產出具證據標籤的教育遊戲 brief，並為一個可能不同於 AI 預評排名的人類設計決策提出理由。

## Recommended format

- Audience: university students, teachers, researchers, and game-design teams.
- Duration: 90 minutes; extend to 120 minutes for team presentations.
- Group size: 3–5 learners per team.
- Mode: Teaching; add Research Game safeguards when the work will support formal research.
- Required materials: the PPTX introduction deck, this workbook, a computer with Codex, and a shared place to save evidence.

## Task 1 — Hands-on installation and first run

### Student outcome

Install the complete Skill folder, confirm that `SKILL.md` is directly inside the `game-design` directory, restart or reload Codex, and use the Skill to produce a small design brief.

### Installation path

1. Preferred Codex route: run `$skill-installer game-design` when the Skill Installer is available.
2. Manual route: copy or extract the complete Skill folder to `%USERPROFILE%\\.codex\\skills\\game-design\\` on Windows, or `~/.codex/skills/game-design/` on macOS/Linux.
3. Confirm the final path ends with `game-design/SKILL.md`.
4. Restart Codex or reload the Skill list.
5. Verify with the Skill Creator validator:

   `python <path-to-skill-creator>/scripts/quick_validate.py <path-to-installed-game-design>`

### First-run challenge

Use this prompt after installation. Replace the bracketed values:

> Teaching mode. Design an educational game for [learner group] about [learning topic], playable in [time] minutes on [device]. First ask me to lock the L/E/M/A priorities and G/C penalties. Then generate 6 meaningfully different concepts, label hypotheses and AI pre-scores, apply Hard Gates and G/R/D, calculate deterministic R_edu, and return the top three with risks and one falsifiable prototype test for each. Do not choose the winner for me.

### Evidence to submit

- installation path or installer result;
- validator result;
- the brief and locked weight profile;
- six candidate IDs and the top-three shortlist;
- one human decision and one falsifiable next test;
- a note identifying one AI pre-score that is still only a hypothesis.

## Task 2 — Course discussion

### Discussion outcome

Learners should explain why the Reinforcement Learning loop is a useful concept analogy but not proof that the Skill is an autonomous Reinforcement Learning agent; distinguish R_edu from formal learning outcomes; and identify how human review prevents reward hacking and unsupported claims.

### Three discussion rounds

1. **Loop round — 10 minutes**: Explain `State → Action → Reward → Next State`. Map each term to the COAST example, then mark where the analogy stops.
2. **Reward round — 10 minutes**: Choose two positive priorities among Learning, Engagement, Motivation/self-efficacy, and Appropriate Challenge. Explain the weights and identify one guessing or cognitive-load risk.
3. **Decision round — 10 minutes**: Compare an AI ranking with the team's own ranking. Keep, modify, or reject one candidate and defend the decision with evidence and a test.

### Discussion rules

- The rubric is shown before the AI ranking.
- AI pre-score is not player evidence and is capped at medium confidence.
- A high total score cannot repair a failed Hard Gate.
- Grade the quality of reasons and evidence, not agreement with AI.
- Do not collect identifiable playtest data without institutional approval.

## Assessment

- Problem and constraints: 20%
- Candidate distinctness: 15%
- Evidence-based G/R/D scoring: 20%
- Iteration and change rationale: 20%
- Prototype-test quality: 15%
- Reflection on AI limits and human decision: 10%

## Related files

- Student-facing Word workbook: `assets/Game-Design-Skill-課程學習任務與學習單.docx`
- Existing student worksheet: `assets/student-worksheet.md`
- Instructor rubric: `assets/instructor-rubric.md`
- Teaching guidance: `teaching-mode.md`
