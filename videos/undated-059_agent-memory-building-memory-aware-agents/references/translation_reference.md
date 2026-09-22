# 翻译参考资料
项目：全课程合并音频333333.mp3
更新时间：2026-09-20 11:30:55

课程翻译参考：Agent Memory: Building Memory-Aware Agents

推荐中文标题

智能体记忆：构建具备记忆能力的 AI 智能体

也可选：
智能体记忆：打造记忆感知型智能体
构建具备记忆能力的 AI 智能体｜Richmond Alake、Nacho Martínez

课程基本信息

原课程标题：Agent Memory: Building Memory-Aware Agents
课程链接：https://www.deeplearning.ai/courses/agent-memory-building-memory-aware-agents
平台：DeepLearning.AI
合作方：Oracle
主讲人：Richmond Alake、Nacho Martínez
课程难度：Intermediate
建议翻译：中级
课程时长：1 小时 57 分钟
课程结构：7 个视频章节，4 个代码示例，1 个计分作业
适合人群：正在构建 AI 智能体，并希望让智能体具备跨会话记忆能力的开发者
前置基础：建议熟悉 Python 和基本 LLM 概念

主讲人称呼统一

Richmond Alake：Richmond Alake
职位：Oracle AI Developer Experience 总监
建议译法：Oracle AI 开发者体验总监

Nacho Martínez：Nacho Martínez
职位：Principal Data Science Advocate at Oracle
建议译法：Oracle 首席数据科学倡导者

Oracle：Oracle
Oracle AI Database：Oracle AI Database
不要译成“甲骨文 AI 数据库”，字幕里建议保留产品名 Oracle AI Database。

课程定位

这门课讲的是如何为 AI 智能体构建真正可持久化、可检索、可更新的长期记忆系统。普通智能体通常只能在一次会话内工作得不错，一旦会话结束，就会丢失上下文；而具备记忆能力的智能体可以跨会话保留重要信息，加载过去的上下文，并随着交互不断更新自己的记忆。

课程围绕 memory-first architecture（记忆优先架构）展开，用 Oracle AI Database、LangChain 和 LLM 驱动的流水线，构建一个完整的 Memory Aware Agent。重点包括：记忆管理器、不同类型的智能体记忆、语义工具检索、记忆提取、记忆整合、自更新记忆，以及跨会话持久化。

核心术语统一

Agent Memory：智能体记忆
Memory-Aware Agents：具备记忆能力的智能体 / 记忆感知型智能体
Memory Aware Agent：具备记忆能力的智能体
memory-aware：具备记忆能力的 / 记忆感知型
memory-first architecture：记忆优先架构
stateless agents：无状态智能体
stateful agent：有状态智能体
fully stateful agent：完全有状态的智能体
long-term memory：长期记忆
persistent memory：持久化记忆
persistence：持久化
external to the model：位于模型之外 / 外置于模型
structured memory：结构化记忆
memory infrastructure：记忆基础设施
memory system：记忆系统
memory store：记忆存储
persistent memory store：持久化记忆存储
Memory Manager：记忆管理器
memory core：记忆核心
agent stack：智能体技术栈
agent execution：智能体执行过程
startup routine：启动流程
prior context：过往上下文
relevant context：相关上下文
context window：上下文窗口
bloated context window：臃肿的上下文窗口
long-horizon tasks：长周期任务 / 长程任务
single-session interaction：单次会话交互
cross-session：跨会话
across sessions：跨会话
learn across sessions：跨会话学习
recursive reasoning loop：递归推理循环
tool use：工具使用
agent tool use：智能体工具使用
semantic tool memory：语义工具记忆
semantic tool retrieval：语义工具检索
semantic search：语义搜索
procedural memory：程序性记忆 / 流程记忆
episodic memory：情景记忆
semantic memory：语义记忆
working memory：工作记忆
memory extraction：记忆提取
memory consolidation：记忆整合
write-back pipeline：写回流水线
write-back loop：写回循环
self-updating memory：自更新记忆
autonomously update：自主更新
refine its own memory：优化自身记忆
structured facts：结构化事实
conversation：对话
inference time：推理时
scaling problem：扩展性问题
tool access：工具访问
retrieve only the relevant ones：只检索相关工具
LLM-powered pipelines：由 LLM 驱动的流水线
LangChain：LangChain
Oracle AI Database：Oracle AI Database

课程章节翻译

Introduction
课程介绍

Why AI Agents Need Memory
为什么 AI 智能体需要记忆

Constructing The Memory Manager
构建记忆管理器

Scaling Agent Tool Use with Semantic Tool Memory
用语义工具记忆扩展智能体的工具使用能力

Memory Operations: Extraction, Consolidation, and Self-Updating Memory
记忆操作：提取、整合与自更新记忆

Memory Aware Agent
具备记忆能力的智能体

Conclusion
课程总结

Extra resources
额外资源

Quiz
测验

Graded Assignment
计分作业

常用表达建议

Most agents work well within a single session but lose everything the moment it ends.
大多数智能体在单次会话中表现不错，但会话一结束就会丢失所有上下文。

Memory engineering treats long-term memory as first-class infrastructure.
记忆工程把长期记忆视为一等基础设施。

external to the model, persistent, and structured
位于模型之外、可持久化，并且结构化

stateless agents fail at long-horizon tasks
无状态智能体难以完成长周期任务

memory-first architecture gives agents persistence
记忆优先架构让智能体具备持久性

Build a Memory Manager
构建一个记忆管理器

handles different memory types
处理不同类型的记忆

semantic tool retrieval system
语义工具检索系统

without bloating the context window
而不会让上下文窗口变得臃肿

memory extraction, consolidation, and write-back pipelines
记忆提取、整合与写回流水线

autonomously update and refine what it knows over time
随着时间自主更新并优化它所知道的内容

loads prior context at startup
在启动时加载过往上下文

assembles relevant context, state, tools, and outputs
组合相关上下文、状态、工具和输出

improves across sessions
在跨会话过程中持续改进

翻译风格建议

1. memory 在本课程里统一译为“记忆”，不要译成“内存”，除非明确指计算机内存。
2. Memory Manager 统一译为“记忆管理器”，不要译成“内存管理器”。
3. memory-aware 建议译为“具备记忆能力的”，比“记忆感知型”更自然；标题或技术名里可以用“记忆感知型”。
4. stateless / stateful 建议译为“无状态 / 有状态”，这是工程语境里的固定译法。
5. persistent / persistence 建议译为“持久化 / 持久性”，不要译成“坚持”。
6. procedural memory 可译为“程序性记忆”或“流程记忆”。如果字幕面向开发者，建议用“程序性记忆”。
7. episodic memory 统一译为“情景记忆”，semantic memory 统一译为“语义记忆”，working memory 统一译为“工作记忆”。
8. write-back 建议译为“写回”，不要译成“回写”也可以，但全文保持一致。
9. context window 统一译为“上下文窗口”。
10. tool retrieval / semantic retrieval 建议译为“工具检索 / 语义检索”，不要翻成“工具召回”除非全文偏检索系统术语。
11. Oracle AI Database 保留英文产品名。
12. LangChain 保留英文。
