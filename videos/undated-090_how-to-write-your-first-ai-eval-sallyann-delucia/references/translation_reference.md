# 《如何编写你的第一条 AI 评测》翻译参考

原视频：How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI
链接：https://www.youtube.com/watch?v=gv4w23xYj-0
主讲：SallyAnn DeLucia，Arize AI 产品负责人
依据：原视频简介、官方章节及本项目 `04_字幕` 中的英文原版字幕。

## 一句话主题

这是一场动手工作坊：用一个旅行规划智能体的 trace，从“感觉它好像变好了”转向定义具体的成功与失败条件，再在 Arize 的界面中选样本、搭建并迭代第一条 LLM 评审。

## 内容脉络

1. 开场说明只凭主观感觉发布改动（vibe checks）无法稳定发现回归。eval 是用于观察 AI 产品行为的信号，不等同于传统单元测试。
2. 智能体会经过多步调用；只看最终回答可能错过中间失败。因此需要 trace 和可观测性。视频解释 trace、span、root span，以及如何在树状执行记录里查输入输出。
3. 概览几类评测：LLM 评审、决策模型、基于代码的评测、人工标注及 agent 评审。不同方式适用于不同失败模式；客观可判定的条件优先考虑代码检查。
4. 工作坊使用旅行规划 agent：用户提出旅行需求，agent 追问、调用工具并输出行程。先看真实 trace，明确这个产品什么叫“好”，再选择一个可操作的判断点。
5. 写评测标准时把任务、成功、失败、判断对象、所需上下文、输出标签写清楚。讲者建议先做单一标准，后续再迭代添加。
6. 从 trace 建立小数据集，在 playground 写 prompt、检查结果并修改。末尾讨论人工对齐、线上评测和进一步迭代；“先用约 20 条 trace 从一条 eval 起步”是工作坊建议，不是所有项目的固定要求。

## 术语统一

| 原文 | 建议译法 | 说明 |
| --- | --- | --- |
| eval / evals | eval（评测）；后续保留 eval | AI 产品行为评测 |
| vibe check | 凭感觉检查／主观感觉检查 | 指未定义可验证标准的检查 |
| unit test | 单元测试 | 不要与 eval 画等号 |
| trace | trace（调用轨迹）；后续 trace | 一次请求经过的完整步骤 |
| span / root span | span（执行片段）／root span（根片段） | trace 树的节点；字幕里的“跨度”不自然 |
| observability | 可观测性 | 用 trace 等手段看系统行为 |
| LLM-as-a-judge | LLM 评审（LLM-as-a-judge） | 用模型判断某项标准是否满足 |
| decision model / decision judge | 决策模型／决策评审器 | 与通用 LLM 评审区分 |
| code eval | 基于代码的评测 | 用确定性规则检查 |
| annotation | 人工标注 | 人在样本上做判定或写备注 |
| pass/fail criteria | 通过／失败标准 | 要写成可核对的具体条件 |
| failure mode | 失败模式 | 一类可归纳的问题，不是一条偶发错误 |
| dataset | 数据集 | 由所选 trace / span 组成 |
| playground | playground（调试界面） | Arize 产品界面，后续保留 playground |
| online eval | 线上评测 | 在真实运行数据上持续评测 |
| regression | 回归问题 | 改动后原本正常的行为变坏 |

## 人名、产品与字幕识别

- 首次出现写 SallyAnn DeLucia（Arize AI 产品负责人）、Arize AI（AI 可观测与评测平台），后续分别保留 SallyAnn、Arize。原版自动字幕多次把 Arize 识别为 “Arise”，应按视频标题核正。
- Alex 是 Arize 平台内的 AI 助手，首次出现写 Alex（Arize 的 AI 助手），后续保留 Alex。Signal 是产品功能名，保留英文，具体功能按画面核对。
- 自动字幕里的 “Elm as a judge” 应核为 “LLM-as-a-judge”；“lane graph”结合画面可能是 LangGraph，不能仅凭识别结果定名。
- 现场问答与等待参会者登录、配置 API key 的片段属于工作坊过程；翻译可自然表达，但不要误写成评测方法本身的步骤。
- 模型提供商账号与 API key 只是练习环境设置；不要在翻译中暗示必须使用某一家模型。

## 原视频章节定位（供核对）

00:00 开场与目标
02:06 为什么主观检查不够
03:08 eval 与单元测试
04:13 智能体评测为什么更难
05:15 评测类型
10:16 查看旅行 agent 的 trace
14:20 读懂 trace
19:03 定义好结果
22:02 写通过／失败标准
25:19 从 trace 建数据集
26:53 编写和测试 LLM 评审
32:08 后续迭代
