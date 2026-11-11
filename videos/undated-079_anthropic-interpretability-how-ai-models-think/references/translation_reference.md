# 翻译参考资料
项目：Interpretability： Understanding how AI models think [fGKNUvivvnc].mp3
更新时间：2026-11-11 11:51:49

翻译参考资料

原视频标题：Interpretability: Understanding how AI models think
中文参考标题：打开 AI 黑箱：我们如何理解模型的内部思考
原视频链接：https://www.youtube.com/watch?v=fGKNUvivvnc
发布频道：Anthropic
视频时长：约 59 分钟
出镜研究者：Josh Batson、Emmanuel Ameisen、Jack Lindsey
主题：AI 模型的可解释性研究

内容背景

这期视频讨论一个核心问题：大语言模型回答问题时，内部究竟发生了什么？Anthropic 的三位研究者介绍如何研究 Claude 的内部活动，以及这些研究能怎样帮助我们理解模型的推理、幻觉和安全问题。

视频会谈到“AI 生物学”的研究视角、打开模型黑箱的方法、Claude 内部一些出人意料的特征，以及模型说出的推理过程是否忠实反映了它实际进行的计算。结尾讨论可解释性研究的价值与目前的局限。

原视频章节（时间点来自原视频简介）

00:00 引言：模型内部究竟在做什么
01:37 把 AI 模型当作研究对象
06:43 用科学方法打开模型黑箱
10:35 Claude 内部令人意外的特征
20:39 能相信模型自述的“思考过程”吗
25:17 AI 模型为什么会产生幻觉
34:15 模型会提前规划吗
38:30 为什么可解释性研究重要
53:35 可解释性研究的未来

人物与名称

Josh Batson：保留英文名，不自行音译。
Emmanuel Ameisen：保留英文名，注意姓氏拼写为 Ameisen。
Jack Lindsey：保留英文名，注意姓氏为 Lindsey。
Anthropic：公司名，保留英文。
Claude：模型名，保留英文；不要根据语音识别结果误写为 Cloud。
Claude 3.5 Haiku：具体模型名称，出现时保留完整写法。

术语统一

interpretability：可解释性，指研究模型内部机制、理解其行为如何产生。
mechanistic interpretability：机制可解释性。
black box：黑箱。
AI biology：首次写 AI biology（AI 生物学），之后可保留英文；这是研究视角，不是说模型真的具有生物生命。
large language model / LLM：大语言模型 / LLM。
next-token prediction：预测下一个 token；token 首次出现写 token（词元），之后保留 token。
feature：特征，指研究者识别出的内部活动模式；不要一律译为“功能”。
activation：激活；根据语境可译为“激活值”或“激活状态”。
circuit：计算回路；不是实体电路。
circuit tracing：回路追踪。
attribution graph：归因图。
representation：表征。
internal computation：内部计算。
reasoning：推理。
chain of thought：首次写 chain of thought（思维链），之后保留英文或简称“思维链”。
faithful reasoning：忠实推理，指模型给出的解释与实际计算过程相符。
unfaithful reasoning：非忠实推理，指解释听起来合理，却未准确反映实际过程。
hallucination：幻觉，指模型生成貌似可信但不符合事实的内容。
sycophancy：迎合用户；视语境也可译为“谄媚倾向”。
planning ahead：提前规划。
AI safety：AI 安全。
alignment：对齐；涉及目标和行为时可译为“AI 对齐”。
intervention：干预；在研究实验中常指人为改变某些内部活动，观察输出如何变化。

容易误译的地方

“how models think”可作为标题译为“模型如何思考”，但正文不要据此断言模型具有人的意识。谈具体机制时，优先译为“内部如何计算、表征或规划”。
“预测下一个 token”是模型训练任务的描述，不等于它在每一步都只做简单的自动补全。
模型展示出来的思维链，不一定完整、准确地说明其内部实际发生的计算；也不要反过来断言它始终不可信。
研究者在特定实验中观察到的机制，不要扩写成“所有 AI 模型都这样运作”。
“发现模型会提前规划”应保留实验范围，不要夸大成模型对所有任务都有完整的长期计划。
“幻觉”不是模型有意撒谎；翻译时区分错误生成、迎合用户和有意欺骗等不同概念。

常见语音识别错误

Cloud / clouds → 结合语境核对是否为 Claude
Emmanuel Amison / Amaisen → Emmanuel Ameisen
Jack Lindsay → Jack Lindsey
Josh Batsun / Batsonn → Josh Batson
token / spoken / taking → 根据上下文核对 token
circuit / circle → 根据上下文核对 circuit
interpretability / interoperability → 注意区分“可解释性”和“互操作性”

翻译风格

采用清楚、自然的科技研究访谈语气，保留提问和探索感。首次出现的英文专有名词可用“英文（简短中文解释）”，之后保留英文原文。研究发现要说明适用范围；涉及意识、真实思维、幻觉成因和安全性时，避免把假设或局部实验结果写成定论。
