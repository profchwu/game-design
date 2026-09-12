# Game Design Skill｜繁體中文參考版

- 建立者：National Tsing Hua University, Professor Chih-Hung Wu
- 版本：1.2.0
- 著作權：Copyright (c) National Tsing Hua University, Professor Chih-Hung Wu. All rights reserved.

本文件是根目錄 `SKILL.md` 的完整繁體中文參考版，供中文閱讀、教學與溝通使用。正式執行入口仍是根目錄的英文 `SKILL.md`；兩者應保持同步。

本 Skill 由國立清華大學 吳智鴻教授開發。除另有書面授權外，著作權及相關權利保留。完整發布聲明請見 [COPYRIGHT.md](../COPYRIGHT.md)。

## Game Design

採用競賽式、具證據標籤的設計流程。Skill 會提出並挑戰不同方案；所有具關鍵影響的選擇，仍由使用者、教師或專案負責人決定。

## 選擇模式

- **Production（製作）**：從設計 brief 推進到可測試的垂直切片。
- **Teaching（教學）**：呈現 scorecard、工作表、反思問題與評量證據。
- **Research game（研究遊戲）**：加入效度、可重現性與版本凍結關卡。

依請求推斷最輕量且合適的模式。若同時涉及教學與研究遊戲，合併使用 Teaching 與 Research game。

## 不可省略的流程

1. 確認設計 brief 與硬性限制。若是教育遊戲，閱讀 [educational-reward-function.md](educational-reward-function.md) 中的教育獎勵函數規則：詢問 Learning、Engagement、Motivation/self-efficacy、Appropriate challenge 四者的優先順序，以及應多大程度懲罰猜測／鑽漏洞與認知超載；在評分候選方案前鎖定 profile。
2. 當需要當代或事實依據時，研究相關的成功遊戲與領域證據。
3. 產生 6–10 個具有實質差異的遊戲概念。評分前先配置中性的候選 ID。
4. 依 [competition-protocol.md](competition-protocol.md) 執行盲測競賽。
5. 依 [scoring-rubric.md](scoring-rubric.md) 使用獨立的 G/R/D 評分規準。不可把某一維度的失敗隱藏在單一加權總分中。
6. 回傳附有證據層級、風險、成本與建議測試的排序 shortlist。停下來等待人類選擇。
7. 遊戲玩法獲選後，使用相同場景、內容與遊戲狀態建立恰好三個可比較的視覺方向。停下來等待視覺選擇。
8. 視覺獲得核准後，建立最小可行垂直切片，加入動態、音訊與美術，並進行玩家測試。
9. 每次只迭代一個具實質影響的變數；保留版本與回歸證據。
10. 若使用 Research game 模式，在正式資料蒐集前凍結研究版本。

在人類完成玩法與視覺核准前，不要開始完整實作。沉默不代表核准。

## 證據標籤

每一項關於候選方案的實質主張，都必須帶有下列其中一種標籤：

- **Hypothesis**：尚未測試的設計假設。
- **AI pre-score**：結構化的模型判斷，不是玩家證據。
- **Expert review**：可歸屬於特定專家的評估。
- **Prototype observation**：在受控 prototype session 中觀察到的行為。
- **Player evidence**：附有樣本與方法的參與者測量資料。

不可把 AI pre-score 描述成遊戲有趣、有效或具效度的證明。提供簡潔理由與 scorecard，不提供隱藏的推理逐字稿。

## 教育獎勵函數規則

若是教育遊戲，閱讀 [educational-reward-function.md](educational-reward-function.md)。對每一個 finalist 回報六個正規化元件，以及 deterministic 的 `R_edu` 診斷結果。將 `R_edu` 與 G/R/D 分開：它可以觸發審查或揭示取捨，但不可默默取代獨立軸向或正式學習成果。不可讓 LLM 在 runtime 中發明或修改評分值。

## 必要的決策報告

至少回傳前三名與所有因硬性關卡淘汰的候選方案。每個 finalist 都要包含：

- 候選 ID 與名稱；
- 一句話的 fantasy 與核心循環；
- Game Experience、Research Validity、Development Feasibility 分數；
- 若是教育遊戲，包含 L/E/M/A/G/C 元件值、鎖定的權重 profile、`R_edu`，以及 integrity 或 overload flags；
- 證據層級與信心程度；
- 最大優勢與最大風險；
- 可比較的市場模式，但不可複製受保護的資產；
- prototype 範圍與預估複雜度；
- 下一個可證偽的測試。

先使用 Pareto rank。只有在平手時，才依序使用 minimum-dimension score 與 mean score 作為 tie-breaker，並清楚揭露。第一名是建議，不是自動決策。

## 核准後的專業路由

- Brief、關卡、可追溯性與驗收使用 Design Thinking／SDLC 指引。
- 瀏覽器體驗、響應式設計與無障礙使用網站／介面指引。
- 原創 raster concept art 與三組視覺 mockup 使用圖像生成。
- 確定性互動效果與功能圖形使用 SVG／CSS／canvas。
- 新聞、後果與回顧影片序列使用 Remotion，不把它當成交互式遊戲的替代品。
- 可遊玩流程與在地化 QA 使用瀏覽器測試。
- 指定音訊行為與授權；不可宣稱目前不存在的音樂生成能力。

關於視覺與動態交接，閱讀 [visual-motion-pipeline.md](visual-motion-pipeline.md)。

## 建議搭配的其他 Skill

只有在目前任務確實需要相應能力，且該 Skill 在環境中可用時，才使用下列搭配 Skill：

- `sites:sites-building`：製作瀏覽器可玩的 prototype、響應式介面、dashboard 與無障礙遊戲入口。核准的 prototype 需要發布時，再使用 `sites:sites-hosting`。
- `visualize:visualize`：探索與比較視覺方向、圖表、地圖、mockup 與互動式解說視覺。
- `imagegen`：建立原創 raster concept art、sprite、texture 與透明背景資產。確定性的介面圖形與互動效果直接使用 SVG／CSS／canvas；不要求另設 SVG 生成 Skill。
- `remotion-best-practices`：建立遊戲中的新聞、後果與回顧影片序列；不可取代互動式遊戲。
- `browser:control-in-app-browser`：測試瀏覽器中的可玩流程、響應式行為與在地化。
- 背景音樂與音效：目前沒有已安裝的專用音訊生成 Skill。若未來有可用 Skill，使用它建立具備明確時長、循環、強度、stem、格式與授權要求的原創音樂與音效；否則使用已授權或使用者提供的音訊資產，並記錄來源。

## 安裝方法

安裝完整的 Skill 資料夾，讓 `SKILL.md` 直接位於 `game-design` 目錄內。不可只把 zip 檔放入目錄，也不可重新命名 `SKILL.md`。

### Windows

1. 將 Skill 內容複製或解壓縮到 `%USERPROFILE%\\.codex\\skills\\game-design\\`。
2. 確認 `%USERPROFILE%\\.codex\\skills\\game-design\\SKILL.md` 存在。
3. 重新啟動 Codex，或重新載入 Skill 清單。

本專案的來源資料夾是 `C:\\Users\\user\\Documents\\Game-design\\skill`；請複製該資料夾的內容，不要複製上層專案資料夾。

### macOS/Linux

將 Skill 內容複製或解壓縮到 `~/.codex/skills/game-design/`；若已設定 `CODEX_HOME`，則使用 `$CODEX_HOME/skills/game-design/`。最後必須是 `.../game-design/SKILL.md`。

### 驗證安裝

對安裝後的資料夾執行 Skill Creator validator：

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ~/.codex/skills/game-design
```

標準 Codex 安裝中的 `<path-to-skill-creator>` 是 `~/.codex/skills/.system/skill-creator`。驗證器應回報 `Skill is valid!`，再使用或發布 Skill。

## Teaching 模式

當請求具有教育性時，閱讀 [teaching-mode.md](teaching-mode.md)。在揭露 AI 排名之前，先把評分規準提供給學習者。清楚區分學生決策、AI 建議與玩家證據。

## Research game 安全規則

當結果要支援論文、評量或正式研究時，閱讀 [research-game-gates.md](research-game-gates.md)。在設計與評分規則凍結前，不可直接針對正式 post-test 分數最佳化候選方案。

## 可重複使用的資產與驗證

- 決策報告使用 [ranking-report-template.md](../assets/ranking-report-template.md)。
- Teaching 模式使用 [student-worksheet.md](../assets/student-worksheet.md) 與 [instructor-rubric.md](../assets/instructor-rubric.md)。
- 需要完整參考資料時，重複使用 [Game-Design-Skill-說明書.docx](../assets/Game-Design-Skill-說明書.docx) 這份圖解教師手冊。
- 教師導入課程使用 [Game-Design-Skill-教學簡報.pptx](../assets/Game-Design-Skill-教學簡報.pptx)；只有在保留核准關卡與證據規則後，才調整範例。
- 產生 scorecard JSON 時，執行 `scripts/validate_scorecard.py`，驗證範圍、硬性關卡、證據標籤與 deterministic Pareto 排序。
