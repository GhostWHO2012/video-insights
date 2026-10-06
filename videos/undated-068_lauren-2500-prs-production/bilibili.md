# 如何在一个月内将 2,500 个 PR 推上生产环境｜Lauren Tan

## 视频简介

Lauren Tan 分享了自己如何构建一套高信任度的 Agent 工程体系，并在一个月内将 2,500 个 PR（代码合并请求）推上生产环境。她认为，真正限制 Agent 规模化应用的不是模型能力，而是开发者能否信任 Agent 在无人监督时依然交付高质量成果。

内容从 Cursor 的性能调试经历展开，介绍 Control Glass、feature map、pstack 等工具和工作流，以及由代码库、静态检查、规则、skill 和人工规范组成的五级纠错体系。Lauren 还讲解了 Dune 框架，以及 Grok Bot 如何连接 Slack、Datadog、Sentry 等系统，形成自动发现问题、重现故障并创建 PR 的外循环。

原视频标题：Here's How I Shipped 2,500 PRs Last Month to Production

原视频链接：https://x.com/poteto/status/2102050467505430555

主讲人：Lauren Tan

注：原帖标题写的是 2,500 个 PR，演讲中口述的是 2,000 个 PR。本标题遵循原帖，字幕遵循实际口述。

## 看点

1. 为什么同时运行更多 Agent 不等于获得更高生产力
2. 如何从监督少量 Agent 扩展到约 100 个 Agent
3. Control Glass 如何让 Agent 操作并验证真实应用
4. 如何通过五级纠错体系建立对 Agent 的信任
5. Dune 如何用架构边界把正确做法变成默认路径
6. 如何通过外循环自动处理事件并创建 PR

## B站章节

00:00 2000个PR的起点
02:38 告别人工调试
05:11 建立Agent信任
08:42 自动验证应用
10:15 功能地图与记忆
13:20 pstack工作流
15:39 五级纠错体系
19:07 Dune约束框架
26:42 代码库就是记忆
32:43 自动化外循环

注：以上章节为根据字幕和提纲整理的自制章节，原视频未提供可直接复用的官方章节。
