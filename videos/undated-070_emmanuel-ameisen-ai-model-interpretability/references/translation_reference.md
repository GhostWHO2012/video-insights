# 翻译参考资料
项目：A mind-expanding conversation on how models actually work ｜ Emmanuel Ameisen (Anthropic) [JHo-aiePjoM].mp3
更新时间：2026-10-20 19:02:23

翻译参考资料

内容背景
原视频标题：A mind-expanding conversation on how models actually work | Emmanuel Ameisen (Anthropic)
中文参考标题：打开 AI 黑箱：模型究竟如何思考｜Emmanuel Ameisen（Anthropic）
视频链接：https://www.youtube.com/watch?v=JHo-aiePjoM
频道：Lenny's Podcast
发布时间：2026-10-18
时长：1:12:12
语言：英语
主持人：Lenny Rachitsky
嘉宾：Emmanuel Ameisen，Anthropic 可解释性研究员

嘉宾背景
Emmanuel Ameisen 在 Anthropic 研究大语言模型的内部机制，试图理解 Claude 如何形成概念、规划输出并完成推理。加入 Anthropic 前，他曾在 Stripe 和 Insight 从事应用机器学习，也是《Building Machine Learning Powered Applications》一书的作者。

核心内容
本期讨论如何打开 AI 模型的“黑箱”。Emmanuel 解释，语言模型并不是由工程师逐条写出行为规则，而是在训练过程中“生长”出内部表征、计算回路和解决问题的策略。

视频重点讨论：为什么“下一 token 预测器”不足以描述模型的实际能力；模型如何跨语言表征概念；Claude 如何提前规划多个 token；J-space 如何呈现模型没有说出口的内部思考；平滑的 scaling 曲线为什么会表现为突然的能力跃迁；可解释性研究与 AI 对齐、安全及意识问题之间的关系。

官方内容结构
00:00 Emmanuel Ameisen 介绍
01:30 AI 模型为何是“生长”出来的，而不是构建出来的
05:57 下一 token 预测为何比听起来更复杂
11:49 模型如何表征概念并理解世界
17:06 大语言模型如何提前规划
23:10 AI 是否可能拥有意识
24:44 Scaling laws 与文本的力量
28:29 平滑进步为何会产生突然突破
32:59 仅观察 AI 行为为何无法解决对齐问题
38:21 Golden Gate Claude 实验
39:01 Anthropic 为何严肃对待 AI 安全
42:06 什么时候对 AI 进行拟人化是有用的
48:06 AI 能让我们了解哪些关于智能的事实
51:44 对 AI 对齐保持乐观的理由
55:43 我们是否生活在模拟世界中
59:00 Jev、决策模型与 AI 的直觉判断
1:01:37 关于模型思维方式的另外两个发现
1:03:33 如何进入可解释性研究领域
1:04:55 快问快答与总结

人物、机构与产品
Emmanuel Ameisen：保留英文名，不音译
Lenny Rachitsky：主持人，可简称 Lenny
Chris Olah：Anthropic 可解释性研究者，保留英文名
Ilya Sutskever：保留英文名
Anthropic、Claude、Stripe、Insight、Distill、Neuronpedia：均保留英文
Golden Gate Claude：首次写 Golden Gate Claude（金门大桥 Claude 实验），之后保留原文
Jev：决策模型产品名，始终保留 Jev，不要误译成人名 Jeff
J-space：首次写 J-space（J 空间），之后保留 J-space
J-lens：首次写 J-lens（J 透镜），之后保留 J-lens
Jacobian：首次写 Jacobian（雅可比矩阵），之后保留英文

术语统一
interpretability：可解释性
mechanistic interpretability：机制可解释性
large language model / LLM：大语言模型 / LLM
next-token predictor：下一 token 预测器
token：首次写 token（词元），之后保留 token
representation：表征
concept representation：概念表征
feature：特征
circuit：计算回路 / 回路
activation：激活 / 激活值
internal state：内部状态
latent space：潜在空间
world model：世界模型
scaling laws：首次写 scaling laws（缩放定律），之后保留 scaling laws
emergence：涌现
emergent capability：涌现能力
capability jump：能力跃迁
alignment：对齐
AI alignment：AI 对齐
alignment problem：对齐问题
AI safety：AI 安全
anthropomorphizing：拟人化 / 以人的方式理解 AI
global workspace：全局工作空间
global workspace theory：全局工作空间理论
consciously accessible：意识可及 / 可被意识访问
conscious processing：意识加工
unconscious processing：无意识加工
chain of thought：首次写 chain of thought（思维链），之后保留原文
scratchpad：推理草稿区
self-awareness：自我觉察，不要轻易译成“自我意识”
model organism：模型生物 / 用于研究的模型系统
causal intervention：因果干预
faithful reasoning：忠实推理
unfaithful reasoning：非忠实推理
motivated reasoning：动机性推理
System 1 / System 2：系统一 / 系统二
decision model：决策模型
gut instinct：直觉判断
black box：黑箱
AI biology：AI biology（AI 生物学）

ASR 易错词
Emmanuel Amison / Amaisen → Emmanuel Ameisen
Lenny Ratchetsky / Rachiski → Lenny Rachitsky
Anthropic / anthropic → Anthropic
cloud → Claude
Chris Ola / Olar → Chris Olah
Ilya Suskever / Sutskever → Ilya Sutskever
jay space / J space → J-space
jay lens / J lens → J-lens
Jacobson / Jacobean → Jacobian
Golden Gate cloud → Golden Gate Claude
Jeff / JEV → Jev
neuron pedia → Neuronpedia
scaling loss → scaling laws（结合上下文判断）
next word predictor → next-token predictor
system one / system two → System 1 / System 2

翻译风格
整体采用自然、清晰的科技访谈语气，兼顾研究准确性与普通观众的可理解性。
首次出现的英文专有名词使用“英文（中文解释）”，之后保留英文原文。
不要把 model thinks 一律翻成“模型有思想”；根据语境译为“模型进行内部计算”“模型形成表征”或“模型在规划”。
grown, not built 统一译为“生长出来的，而不是被逐条构建出来的”，强调模型能力来自训练，而不是人工编写规则。
next-token prediction 不要简单译成“猜下一个词”，应译为“预测下一个 token”。
consciousness、self-awareness 和 consciously accessible 必须区分，不能都译成“意识”。
anthropomorphizing 不必一概译成负面的“人格化误导”，本期语境中可译为“用拟人化方式理解模型”。
涉及 Claude 是否拥有意识时保持审慎，不要把研究中的结构相似性写成已经证明 Claude 有意识。
删除或弱化赞助、订阅和平台推广内容，不扩写广告。
