# 翻译参考资料
项目：12_AIEvals_ClaudeCode.m4a
更新时间：2026-09-02 12:30:15

## 内容背景
- 原视频标题：How to Build Better AI Evals with Claude Code in 5 Steps | Shreya & Hamel
- 视频链接：https://www.youtube.com/watch?v=bdMHQLvtVaQ
- 频道：Peter Yang / Behind the Craft
- 发布时间：2026-08-23
- 视频时长：约 53:53
- 视频主题：如何用 Claude Code / ChatGPT 构建更好的 AI evals，重点是从真实输出、失败案例和人工反馈中提炼评估标准，而不是让 AI 凭空生成评分规则。
- 嘉宾：Shreya Shankar 和 Hamel Husain，两人共同教授 AI evaluations 课程，课程已有 4,500+ 名工程师和 PM 学习，学员来自 OpenAI、Google 等公司。
- 场景：Peter Yang 请两位嘉宾现场审查他为 AI skills 做的 evals，并演示如何用免费 eval skill 在 Claude Code / Codex 中运行和改进评估。
- 核心观点：
  1. 做 AI evals 的起点不是写规则，而是先看真实数据、真实输出和真实失败案例。
  2. bottom-up evals 来自数据和错误分析，AI 不擅长自己发明这类标准，人必须参与判断。
  3. top-down evals 可以来自预先设定的产品原则、需求或质量标准，但不能替代真实样本分析。
  4. agent 的作用不是替你创造判断，而是帮助你归类、整理和压缩反馈，变成可执行的评估标准。
  5. 评估不要只追求自动化，要把 AI 的判断和人工标注/人工判断对比，确认 eval 是否真的有效。
  6. 真正的壁垒不是“让 Claude 找错误”，而是你能把多少产品品味、判断力和具体标准注入评估体系。
- 翻译方向：偏 AI 工程实践、产品质量控制、agent 工作流、AI 应用评估。中文应自然、清楚、有工程感，避免把 evals 翻译成泛泛的“评价”，多数场景建议译为“评估 / 评测 / 评估体系”。

## 人物身份/职业背景
| 英文名 | 中文参考 | 身份/职位 | 相关背景 | 翻译注意 |
|---|---|---|---|---|
| Peter Yang | Peter Yang | Behind the Craft 主持人，创作者和产品人 | 关注 AI 工具、个人工作流、产品构建和 creator business | 默认保留英文名 |
| Shreya Shankar | Shreya Shankar | AI/data systems 研究者，AI evals 课程讲师 | 研究 user-centered data & AI systems，参与 AI evals 教学和工具建设 | 默认保留英文名，不强行音译 |
| Hamel Husain | Hamel Husain | AI 工程实践专家，AI evals 课程讲师 | 长期写作和实践 LLM evals、AI 工具、软件工程流程 | 默认保留英文名 |
| Claude | Claude | Anthropic 的大模型/AI 助手 | 视频中常用于 Claude Code 和 eval skill 场景 | 保留 Claude |
| ChatGPT | ChatGPT | OpenAI 的 AI 助手 | 可用于运行或辅助 evals | 保留 ChatGPT |
| Codex | Codex | OpenAI 的编程 agent / 桌面开发工具 | 视频提到可用 Codex 跑可复用 evals | 保留 Codex |
| Claude Code | Claude Code | Anthropic 的编程 agent/代码工具 | 视频核心工具之一 | 保留 Claude Code |

## 公司/产品/工具名
| 名称 | 类型 | 中文参考/说明 | 统一译法建议 |
|---|---|---|---|
| AI evals / evals | AI 评估方法 | 用来判断 AI 输出是否符合标准的评估体系 | 译为“AI 评估 / evals / 评估体系”；首次可写“AI evals（AI 评估）” |
| Claude Code | 编程 agent 工具 | Anthropic 面向代码工作的 agent 工具 | 保留 Claude Code |
| Codex | 编程 agent 工具 | OpenAI 的代码/任务执行 agent | 保留 Codex |
| ChatGPT | AI 助手 | OpenAI 的对话式 AI 工具 | 保留 ChatGPT |
| Maven | 在线课程平台 | 课程平台，视频里提到课程评分和学员评价 | 保留 Maven |
| OpenAI | AI 公司 | OpenAI | 保留 OpenAI |
| Google | 科技公司 | Google | 保留 Google |
| Wispr Flow | 赞助商/语音输入工具 | 语音输入工具 | 保留 Wispr Flow |
| Linear | 赞助商/项目管理工具 | AI agent platform for modern teams | 保留 Linear |
| GitHub | 代码托管平台 | 用于分享 eval skills | 保留 GitHub |
| Google Sheets | 表格工具 | 用于人工查看数据和标注结果 | 保留 Google Sheets 或译为“Google 表格” |

## 核心术语与统一译法
| 英文/概念 | 建议译法 | 说明 |
|---|---|---|
| eval / evals | 评估 / evals / 评估体系 | AI 场景下不要简单译成“评价”；可根据上下文译为“评测” |
| AI evaluations | AI 评估 | 指系统化测试 AI 输出质量 |
| automated evals | 自动化评估 | 注意不是“自动评价” |
| bottom-up evals | 自下而上的评估 / 数据驱动的评估 | 来自真实样本、失败案例和错误分析 |
| top-down evals | 自上而下的评估 | 来自预设原则、产品需求或质量标准 |
| real data | 真实数据 | 核心观点：必须看真实输出 |
| sample outputs | 样本输出 | 指 AI 生成的具体结果 |
| error analysis | 错误分析 | 从失败案例中归纳问题 |
| eval criteria | 评估标准 | 不要译为“评价条件” |
| rubric | 评分标准 / 评估量表 | 如果是结构化标准，译“评估量表”也可以 |
| actionable rubric criteria | 可执行的评估标准 | 指能被模型或人实际判断的标准 |
| pass/fail evals | 通过/不通过评估 | 比随机打分更可靠 |
| yes/no criteria | 是/否判断标准 | 用于清晰评估 |
| labels | 标签 / 标注结果 | 视上下文可译“标注” |
| human labels | 人工标注 | 与 AI 判断对比 |
| model labels | 模型标注 | AI 给出的判断结果 |
| review output labels | 审查输出标注 | 指检查模型/人工标注结果 |
| identify failures | 识别失败案例 | 不要译成“识别故障” |
| reusable evals | 可复用评估 | 指后续可反复运行的 eval |
| eval skill | 评估 skill / eval skill | 如果指 Codex/Claude Code skill，保留 skill |
| AI skill | AI skill / AI 技能 | 用户已有软件里可保留 skill |
| sub-agent | 子 agent | 不建议译“子代理”，可写“子 agent” |
| spin up agents | 启动 agent / 拉起 agent | 工程语境 |
| grade each criterion | 按每条标准评分 / 逐项评估 | |
| output quality | 输出质量 | |
| taste | 品味 / 判断力 | 这里不是“味道”，指产品品味和质量判断 |
| judgment | 判断力 | 常和 taste 一起出现 |
| externalize your taste and judgment | 把你的品味和判断外化出来 | 核心句，指把隐性标准变成可写入 eval 的规则 |
| inject taste | 注入品味 / 注入判断标准 | 指把人的判断融入系统 |
| slop | 低质 AI 垃圾输出 / 粗糙输出 | 根据语境可译“AI 垃圾内容”“低质输出” |
| trace / traces | 轨迹 / 使用记录 / 对话记录 | 如果是 customer traces，译“用户使用轨迹/对话记录” |
| customer conversations | 客户对话 | |
| data-driven | 数据驱动 | |
| workflow | 工作流 | |
| spreadsheet | 表格 | |
| pivot table | 数据透视表 | Hamel 可能提到，译“数据透视表” |
| criterion / criteria | 标准 / 多条标准 | criteria 是复数 |
| hierarchy of importance | 重要性层级 | |
| weights | 权重 | 评估标准加权 |
| failure modes | 失败模式 | |
| feedback | 反馈 | |
| distill feedback | 提炼反馈 | |
| human judgment | 人的判断 / 人类判断力 | |
| automate evals the right way | 用正确方式自动化 evals | 不要译成“完全自动化” |
| do automated evals work? | 自动化评估真的有效吗？ | 可能是 Hamel 文章标题 |

## ASR 易错词校正
| ASR 可能误识别 | 正确形式 | 说明 |
|---|---|---|
| Hambo / Haml / Hamel Hussein / Hamel Husein | Hamel Husain | 嘉宾名 |
| Shrea / Shreya Shanker / Shreyas | Shreya Shankar | 嘉宾名；如果字幕中出现 “Shreyas AI skill” 需确认是否其实是 Shreya’s AI skill |
| Peter Young / Peter Yank | Peter Yang | 主持人 |
| eval / evil / equals / evals | eval / evals | AI 评估术语 |
| Claude Coat / Claude Cote / Claude cold | Claude Code | 工具名 |
| Codex / codecs / code X | Codex | 工具名 |
| bottom up / bottoms up | bottom-up | 评估方法 |
| top down | top-down | 评估方法 |
| rubrics / rubric | rubric | 评估量表 |
| labels / labors | labels | 标注 |
| pass fail / past fail | pass/fail | 通过/不通过 |
| yes no / yes know | yes/no | 是/否判断 |
| slop / sloppy | slop | AI 低质输出 |
| subagent / sub agent | sub-agent | 子 agent |
| Google spreadsheets | Google Sheets | 工具名 |
| pivot table | pivot table | 数据透视表 |
| Maven / maven | Maven | 课程平台 |
| Wispr / Whisper Flow / WISPR Flow | Wispr Flow | 赞助商 |
| Linear / lineer | Linear | 赞助商 |
| Creator Economy | Creator Economy | Peter Yang newsletter |
| Behind the Craft | Behind the Craft | 频道/播客名 |

## 翻译风格规则
- 整体风格：工程实践、产品方法论、AI 工具实操，中文要清楚、直接、有方法感。
- “evals”不要机械翻译成“评价”。建议根据上下文统一为“评估”“AI 评估”“评估体系”，首次可保留英文：AI evals（AI 评估）。
- “taste”在本视频里是“品味/判断力”，不是“味道”。如果和 judgment 连用，可译为“品味和判断力”。
- “bottom-up evals”建议统一为“自下而上的评估”或“数据驱动的评估”，重点强调来自真实样本和错误分析。
- “top-down evals”建议统一为“自上而下的评估”，指预先设定的原则、需求或规则。
- “slop”按语气可译为“低质 AI 输出”“AI 垃圾内容”“粗糙输出”，不要过度文雅。
- “agent”保留为 agent，除非上下文明确适合译为“智能体”。本视频偏工具实践，建议统一用“agent”。
- “skill”如果指 Claude Code/Codex 的可复用能力，建议保留 skill，避免译成“技能”后和普通能力混淆。
- 字幕应短句优先，避免把技术解释塞成很长一句。
- 人名默认保留英文；首次可在参考资料中说明身份，字幕正文里不必强行音译。
- 遇到课程推广、赞助商口播、订阅提示，可在翻译时保留必要信息，但做提纲/简介时应弱化或删除广告性内容。

## 参考资料来源
- 视频/播客信息：Peter Yang / Behind the Craft
- 视频标题：How to Build Better AI Evals with Claude Code in 5 Steps | Shreya & Hamel
- 视频链接：https://www.youtube.com/watch?v=bdMHQLvtVaQ
- 公开简介与时间轴来源：Apple Podcasts / Enpleasure / UseTranscribe / Peter Yang 相关公开帖文
