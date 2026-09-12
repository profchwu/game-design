# game-design Skill

Evidence-driven game concept tournaments for educational, research, and serious games.

Creator / 作者：National Tsing Hua University, Professor Chih-Hung Wu（國立清華大學 吳智鴻教授）  
Version / 版本：1.2.0  
Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved.

## What it does

This Skill helps teams move from a design brief to multiple meaningfully different game concepts, blind review, hard-gate elimination, G/R/D scoring, educational reward diagnostics, human approval, visual directions, prototyping, and playtesting.

The formal execution entry point is [`SKILL.md`](SKILL.md). A Traditional Chinese reading version is available at [`references/zh-TW.md`](references/zh-TW.md).

## Install in Codex

### Windows quick install

From a PowerShell window in this repository, run:

```powershell
.\INSTALL_SKILL.ps1 -Force
```

The `-Force` option replaces an existing `game-design` installation.

### Windows

Copy the complete repository contents into:

```text
%USERPROFILE%\.codex\skills\game-design\
```

Confirm that this file exists:

```text
%USERPROFILE%\.codex\skills\game-design\SKILL.md
```

Restart Codex or reload the Skill list.

### macOS/Linux

Copy the complete repository contents into:

```text
~/.codex/skills/game-design/
```

The final path must end with `game-design/SKILL.md`.

## Validate

Run the Skill Creator validator against the installed folder:

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ~/.codex/skills/game-design
```

The validator should report `Skill is valid!`.

## Included teaching materials

- [`assets/Game-Design-Skill-教學簡報.pptx`](assets/Game-Design-Skill-教學簡報.pptx)
- [`assets/Game-Design-Skill-課程學習任務與學習單.docx`](assets/Game-Design-Skill-課程學習任務與學習單.docx)
- [`references/course-learning-tasks.md`](references/course-learning-tasks.md)
- [`assets/student-worksheet.md`](assets/student-worksheet.md)
- [`assets/instructor-rubric.md`](assets/instructor-rubric.md)

## Companion capabilities

The Skill routes work to available companion capabilities such as Sites, visualization, image generation, Remotion, SVG/CSS/canvas, and browser testing. Background music and sound effects require licensed or user-provided assets unless a suitable audio-generation capability is available.

## Copyright and attribution

This Skill and its accompanying documentation, examples, diagrams, teaching materials, and worksheets were created by National Tsing Hua University, Professor Chih-Hung Wu（國立清華大學 吳智鴻教授）.

Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved. See [`COPYRIGHT.md`](COPYRIGHT.md) for the distribution notice.
