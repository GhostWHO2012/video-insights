# 【中英双语】用 Claude Code 做好 AI Eval的 8 个核心 Skills | Hamel Husain

B站视频：https://www.bilibili.com/video/BV1zPykz1EkF/

https://www.youtube.com/watch?v=c5Ur73GosR4
原视频标题：8 Claude Code skills I use for building better AI evals
原视频链接：https://www.youtube.com/watch?v=c5Ur73GosR4
视频所述项目：https://github.com/ai-evals-course/evals-skills/

AI 产品现在更容易做出来，但怎么知道它真的按预期工作？Hamel Husain 介绍他与 Shreya Shankar 打磨的一组 Claude Code Skill，目标是让团队先阅读实际调用轨迹、发现失败模式，再编写针对自己产品的评测。这组 Skill 来自他们与 50 多家公司合作、教授 5000 多名学员时积累的问题。

视频重点演示两项：error-discovery 帮你搭建适合产品数据的标注界面，以广度和深度相结合的方式审阅样本；eval-audit 检查已有评测是否存在通用指标、过大的 LLM 评审范围或缺少人工验证等问题。其余 Skill 涉及合成数据、评审提示词、RAG 评测等。适合已有 AI 应用与 trace、想把评测流程做得更扎实的团队。

时长：11 分 40 秒
语言：英语 → 简体中文
说话人：Hamel Husain
频道：Hamel Husain
发布时间：2026-09-30

看点（根据视频简介与字幕整理）
1. 为什么写 eval 之前，应先看产品真实失败案例。
2. error-discovery 如何识别数据结构并搭建可用的标注界面。
3. 租房助手案例里，怎样把多轮对话和工具调用呈现给审阅者。
4. 随机抽样、按簇抽样与深入追查失败，怎样配合使用。
5. eval-audit 会检查哪些常见的评测设计问题。
6. 为什么要用人工标签核对 LLM 评审，并优先考虑简单代码检查。
7. 数据不够时，合成数据等其他 Skill 能起什么作用。

时间轴（翻译自原视频简介，保留原时间点）
00:00 为什么写评测前要先看失败案例
00:32 在哪里找到评测 Skill
00:49 八个 Skill 概览
01:57 错误发现：让 agent 理解数据
02:31 设计标注界面
03:14 真实案例：租房助手的标注界面
04:48 按多样性抽样，而非只看高频样本
05:41 审阅循环：广度与深度
07:06 评测审计 Skill
08:06 二元通过／失败优于 1–5 分和字母等级
08:41 用人工标签检验 LLM 评审
09:48 最值得优先投入的两项 Skill
10:06 合成数据、评审提示词、RAG 等其他 Skill
