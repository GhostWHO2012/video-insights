# 翻译参考资料

课程：Voice for AI Agents and Applications

课程链接：https://www.deeplearning.ai/courses/voice-for-ai-agents-and-applications

## 推荐中文标题

为 AI 智能体和应用构建语音能力

## 课程基本信息

原课程标题：Voice for AI Agents and Applications
平台：DeepLearning.AI
合作方：Vocal Bridge
主讲人：Ashwin Sharma
嘉宾：Scott Johnston
课程主题：语音 AI、语音智能体、应用内语音、语音工具调用、语音评估

## 核心术语统一

Voice UI：语音 UI / 语音界面
voice agent：语音智能体
voice AI：语音 AI
voice interaction：语音交互
voice-to-voice model：端到端语音模型 / 语音到语音模型
speech-to-text：语音转文字
text-to-speech：文本转语音
LLM-to-speech pipeline：LLM 到语音的流水线
foreground agent：前台智能体
background agent：后台智能体
reasoning background agent：负责推理的后台智能体
concierge architecture：礼宾式架构
thin layer：轻量层
real-time：实时
latency：延迟
endpointing：端点检测 / 判断用户何时说完
turn-taking：话轮转换
interruption：打断
barge-in：插话 / 打断
bridge line：过渡语 / 衔接语
paralinguistics：副语言信息
prosody：韵律
multimodal：多模态
client actions：Client Actions / 客户端动作
bidirectional channel：双向通道
application state：应用状态
voice embedded in an application：嵌入应用的语音能力
voice layered onto an existing agent：叠加到已有智能体上的语音层
voice as a tool：作为工具的语音
make_phone_call tool：make_phone_call 工具 / 发起电话工具
outbound call：外呼
transcript：转写文本 / 通话记录
multimodal evaluator：多模态评估器
LLM-as-a-judge：以 LLM 作为评判器
evaluation-driven development：评估驱动开发
session ID：会话 ID
tool logs：工具日志
prompt refinement：提示词优化
production：生产环境
production voice agents：生产级语音智能体

## 专名参考

DeepLearning.AI：DeepLearning.AI
Vocal Bridge：Vocal Bridge
Ashwin Sharma：Ashwin Sharma
Scott Johnston：Scott Johnston
Docker：Docker
Claude：Claude
React SDK：React SDK
RAG：RAG
LLM：LLM

## 常用表达建议

Voice is one of the most natural human interfaces.
语音是人类最自然的交互方式之一。

adding it to AI applications has historically forced a tradeoff
过去把语音加入 AI 应用，往往必须在不同方案之间做取舍

fast voice-to-voice models that sacrifice reliability
反应很快但可靠性不足的端到端语音模型

accurate speech-to-text-to-LLM-to-speech pipelines that add latency
准确但会增加延迟的“语音转文字 → LLM → 文本转语音”流水线

voice embedded in an application
把语音嵌入应用

voice layered onto an existing agent without touching its logic
在不改动已有智能体逻辑的情况下，为它叠加语音层

voice as a tool your LLM can call
把语音作为 LLM 可以调用的工具

without touching prompts, RAG pipeline, and tools
不改动提示词、RAG 流水线和工具

stream the transcript back live
实时回传通话转写文本

move voice agents from demos to production
把语音智能体从演示推进到生产环境

## 翻译风格建议

1. voice 在本课程里多数译为“语音”，不要泛化成“声音”。
2. agent 统一译为“智能体”，不要译成“代理”。
3. Vocal Bridge 是产品/公司名，保留英文，不要译成“语音桥”。
4. concierge architecture 建议译为“礼宾式架构”，强调前台语音层协调、委派和衔接后台智能体。
5. foreground/background agent 建议译为“前台智能体 / 后台智能体”，比“前景/背景代理”自然。
6. paralinguistics 建议译为“副语言信息”，prosody 译为“韵律”。
7. endpointing 可以译为“端点检测”，必要时补充为“判断用户何时说完”。
8. voice as a tool 建议译为“把语音作为工具”，不要译成“声音作为工具”。
9. evaluation-driven development 建议译为“评估驱动开发”。
10. production 语境里译为“生产环境 / 生产级”，不要译成“生产制造”。
