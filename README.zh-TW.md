# game-design Skill｜繁體中文

本 Skill 以證據為基礎，透過遊戲概念競賽，支援教育遊戲、研究遊戲與嚴肅遊戲的設計。

**建立者：** 國立清華大學 吳智鴻教授（National Tsing Hua University, Professor Chih-Hung Wu）  
**版本：** 1.2.0  
Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved.

[English README](README.md)

## 功能

本 Skill 協助團隊從設計 brief 出發，產生多個具有實質差異的遊戲概念，進行盲評、硬性關卡淘汰、G/R/D 評分、教育獎勵函數診斷、人類核准、視覺方向選擇、原型製作與遊戲測試。

英文 `SKILL.md` 是唯一正式執行入口，完整繁體中文 Skill 參考版位於 [`references/zh-TW.md`](references/zh-TW.md)。

## 安裝到 Codex

建議先 clone 本 repository，再執行內附安裝程式。安裝程式會將 Skill 檔案複製到 Codex Skills 目錄，不會把 repository 的 README 與安裝腳本複製進已安裝的 Skill。

### Windows 快速安裝

開啟 PowerShell，執行以下指令：

```powershell
git clone https://github.com/profchwu/game-design.git
cd game-design
.\INSTALL_SKILL.ps1
```

如果已經安裝 `game-design`，要以目前版本取代原有版本，請執行：

```powershell
.\INSTALL_SKILL.ps1 -Force
```

預設安裝位置是 `%USERPROFILE%\.codex\skills\game-design\`。

若要指定其他 Codex 安裝目錄，可傳入自訂路徑：

```powershell
.\INSTALL_SKILL.ps1 -Destination "$env:USERPROFILE\.codex\skills\game-design" -Force
```

### macOS/Linux

先 clone repository，再將 Skill 內容複製到 `~/.codex/skills/game-design/`：

```bash
git clone https://github.com/profchwu/game-design.git
cd game-design
mkdir -p ~/.codex/skills/game-design
cp -R SKILL.md agents assets references scripts COPYRIGHT.md ~/.codex/skills/game-design/
```

安裝後的最終路徑必須包含 `game-design/SKILL.md`。完成安裝後，請重新啟動 Codex 或重新載入 Skill 清單。

## 驗證

對已安裝的資料夾執行 Skill Creator validator：

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ~/.codex/skills/game-design
```

驗證器應回報 `Skill is valid!`。

## 內附教學教材

- [`assets/Game-Design-Skill-教學簡報.pptx`](assets/Game-Design-Skill-教學簡報.pptx) — 教學簡報
- [`assets/Game-Design-Skill-課程學習任務與學習單.docx`](assets/Game-Design-Skill-課程學習任務與學習單.docx) — 課程任務與學習單
- [`references/course-learning-tasks.md`](references/course-learning-tasks.md) — Markdown 教學指南
- [`assets/student-worksheet.md`](assets/student-worksheet.md) — 學生工作表
- [`assets/instructor-rubric.md`](assets/instructor-rubric.md) — 教師評分規準

## 配套能力

本 Skill 可依任務需要搭配 Sites、視覺化、影像生成、Remotion、SVG/CSS/canvas 與瀏覽器測試等能力。

背景音樂與音效應使用具授權的素材或使用者提供的素材；若環境提供合適的音訊生成能力，也可以依授權與來源規則使用。

## 著作權與署名

本 Skill 及其文件、範例、圖表、教學教材與學習單由國立清華大學 吳智鴻教授開發。

Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved. 完整發布聲明請見 [`COPYRIGHT.md`](COPYRIGHT.md)。
