# 《我用来改进 AI 评测的 8 个 Claude Code Skill》翻译参考

原视频：8 Claude Code skills I use for building better AI evals
链接：https://www.youtube.com/watch?v=c5Ur73GosR4
主讲：Hamel Husain；片中提到与 Shreya Shankar 合作开发
项目：https://github.com/ai-evals-course/evals-skills/
依据：原视频简介、官方时间点、本项目英文原版字幕；仓库名称以项目页核对。仓库内容可能更新，翻译以视频所说的版本为准。

## 一句话主题

这期不是让 Claude Code 凭空写一套评测，而是介绍一组辅助产品团队查看 trace、发现真实失败、审计已有 eval 的 Skill。讲者把重点放在 `error-discovery` 和 `eval-audit` 上，其余 Skill 用于后续的具体任务。

## 内容脉络

1. 开场说明“产品做出来”比“知道它是否按预期工作”容易得多。先看产品里的真实失败，再写 eval。
2. `evals-start` 是入口，按团队手头的数据和评测状态引导到合适的 Skill。
3. `error-discovery` 帮助 agent 理解 trace 结构、找出重要差异维度、搭建贴合产品的人工标注界面。租房助手示例展示多轮对话、工具调用与结果，让人能顺手翻看样本。
4. 样本选择既要有随机样本，也要覆盖不同数据簇；发现某类错误后继续深入查看相似案例。片中的 breadth/depth 分别指广度探索和针对已发现问题的深入追查。
5. `eval-audit` 检查已有评测：是否滥用 1–5 分、是否把太多标准塞进同一个 LLM 评审、能否改用代码检查、有没有用人工标签验证评审器、是否审阅了足够多的样本。
6. 末尾快速带过其他功能，如生成合成数据、写评审提示词、RAG 评测与搭建审阅界面；不要把这些误写成片中等量展开的八场完整教程。

## 名称与术语

| 原文 | 建议译法 | 说明 |
| --- | --- | --- |
| Claude Code | Claude Code（编程智能体工具）；后续原文 | 产品名不翻译 |
| Skill / skills | Skill（可复用的任务指令）；后续 Skill | 此处特指工具中的 Skill，不是泛泛的“技能水平” |
| eval / evals | eval（评测）；后续 eval | 产品特定评测 |
| evals-start | `evals-start` | 入口 Skill，名称保持原文 |
| error-discovery | `error-discovery`（错误发现） | 视频重点；后续保留命令名 |
| eval-audit | `eval-audit`（评测审计） | 视频重点；后续保留命令名 |
| trace | trace（调用轨迹）；后续 trace | 多轮对话与工具调用记录 |
| annotation interface | 标注界面 | 供人查看、判定并备注 |
| failure mode | 失败模式 | 从样本归纳的错误类型 |
| cluster / sample | 数据簇／抽样 | “按簇抽样”用于多样性覆盖 |
| breadth / depth | 广度／深度 | 广度找新问题，深度追查已发现的问题 |
| Likert scale | 李克特量表 | 此处指 1–5 等等级评分 |
| human labels | 人工标签 | 用于检验 LLM 评审 |
| synthetic data | 合成数据 | 数据不足时生成测试输入 |
| RAG | RAG（检索增强生成） | 首次解释，后续保留 RAG |

## 翻译核对

- 本视频说“八个 Skill”；当前 GitHub 仓库可能已增删项目。不要根据仓库后来版本把视频口述数量改成别的数字。
- 字幕把 Claude 误识成 Cloud、把 LLM 误识成 LM / LMS、把 Likert 误识成 art 时，按上下文和画面核对后统一。
- “至少 100 条 trace 对应每种失败模式”在视频中是审计 Skill 的目标建议，不要表述为统计学硬性门槛。
- `error-discovery` 让 agent 加速整理和抽样；人仍需亲自阅读、标注并确认失败模式。
- 首次出现写 Shreya Shankar（共同开发者），后续保留 Shreya；人名不要音译或猜测职位。

## 原视频时间点

00:00 为什么先找失败再写 eval
00:49 八个 Skill 概览
01:57 错误发现与理解数据
03:14 租房助手标注界面
04:48 多样性抽样
05:41 广度与深度审阅
07:06 评测审计
08:41 用人工标签检验评审
10:06 其余 Skill
