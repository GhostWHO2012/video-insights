# 用 Claude Code 做好 AI 评估的 5 个步骤｜Shreya & Hamel

原视频：How to Build Better AI Evals with Claude Code in 5 Steps | Shreya & Hamel

YouTube：https://www.youtube.com/watch?v=bdMHQLvtVaQ

## 简介

这期是一个非常实用的 AI evals 入门和进阶案例。Peter Yang 邀请 Shreya Shankar 和 Hamel Husain，一起现场审查他为 AI skills 做的评估体系，并演示如何用 Claude Code / Codex 把真实反馈、失败案例和人的判断力转化成可复用的 evals。

视频最核心的观点是：好的 AI 评估不是让模型凭空写一堆规则，而是先看真实数据、真实输出和真实失败，再把人的品味、判断力和具体标准外化出来。Shreya 演示了一个 Error Discovery skill：让 agent 帮你读取样本、构建审查界面、聚类失败案例、记录人工反馈，再把这些反馈提炼成 rubric 和可运行的评估标准。

Hamel 也讨论了自动化 eval 工具的边界：Braintrust、Arize、LangSmith 这类工具能给你一个不错的 baseline，但真正需要产品判断、语境理解和“什么才算好”的地方，仍然离不开人工阅读和审校。对于正在做 AI 产品、agent 工作流、内容生成工具或企业 AI 应用的人，这期很适合用来理解 evals 到底该怎么落地。

## 看点

1. 为什么现在的 AI evals 和过去不一样
2. evals 的起点不是规则，而是真实数据
3. top-down evals 和 bottom-up evals 的区别
4. 为什么 AI 不擅长自己发现 bottom-up evals
5. 如何用 agent 辅助人工看数据
6. Shreya 的 Error Discovery skill 如何工作
7. 如何把失败案例变成 rubric
8. 自动化 eval 工具到底靠不靠谱
9. 为什么“人的品味”仍然是 AI 产品质量的核心
10. 如何把 evals 做成可复用的团队流程
