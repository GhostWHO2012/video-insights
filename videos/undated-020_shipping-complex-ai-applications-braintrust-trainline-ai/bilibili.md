# 交付复杂的AI应用程序|Braintrust & Trainline

## 基本信息

- **BV号**: BV1zq526eEEN
- **视频链接**: https://www.bilibili.com/video/BV1zq526eEEN
- **发布时间**: 2026-05-14 01:05:45
- **UP主**: 通用人工智障

## 视频简介

原视频标题：
Shipping complex AI applications — Braintrust & Trainline
原视频链接：
https://www.youtube.com/watch?v=ZdheJTfLu-s

本视频是一场线下的实操工作坊（Hands-on workshop），由 Braintrust 联合全球火车票务平台 Trainline 的工程师团队共同主讲。由于许多企业在将生成式 AI 原型（POC）推向生产环境时遇到了规模化和运维管理的挑战，该工作坊重点演示了如何为 AI 系统建立工程化标准，以交付高质量的 AI 应用程序。

视频的核心内容：
1.企业级 AI 的落地挑战：探讨了传统确定性软件工程与非确定性 AI 系统之间的差异，指出了仅靠修改提示词（Prompt）难以解决生产环境中的各类失效问题（如“在我的电脑上能跑，但在生产环境中崩溃”）。Trainline 团队也分享了他们在大规模售票平台中开发“AI 旅行助手”（处理退款、预测列车中断等）时的真实经验与痛点。
2.构建多阶段 AI 代理系统：指导观众将单一的大语言模型调用拆解为微服务化的架构，一步步构建一个包含多个处理阶段和工具调用（Tool calling）的自动化客服工单分流系统。
3.AI 系统的追踪与可观测性：展示了如何使用 Braintrust 平台对复杂的 AI 应用进行端到端的链路追踪（Tracing），捕获延迟、成本、Token 消耗以及每一次嵌套工具调用的元数据，从而清晰了解系统在每一步的运行情况。
4.评估体系与持续迭代：介绍了如何告别“凭直觉”发布代码，通过创建包含各种边缘测试用例的“黄金数据集”（Golden data set）来进行系统评估。工作坊还演示了如何利用 LLM 作为裁判（LLM-as-a-judge）进行在线和离线评分，并在捕获到真实的生产环境故障后，修复提示词、验证效果并实现闭环迭代的“飞轮效应”（Flywheel）。

---

*本文档由 WorkBuddy 自动生成*
