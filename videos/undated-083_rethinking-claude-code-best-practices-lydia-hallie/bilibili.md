# 模型进化后 我们该如何与 Agent 协作 | Lydia Hallie

B站视频：https://www.bilibili.com/video/BV191sg6UE47/

https://www.youtube.com/watch?v=vlfCjWuv4es
原视频标题：Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic
原视频链接：https://www.youtube.com/watch?v=vlfCjWuv4es
主讲人：Lydia Hallie，Anthropic 技术人员
频道：AI Engineer
时长：17 分 31 秒
语言：英语 → 简体中文

模型越来越强，过去为 Claude Code 写下的许多“最佳实践”，可能反而在限制它。以前，开发者需要守着一两个会话，反复纠正模型、批准命令；现在，一个人可以让多个 Agent 长时间并行工作。人不再盯着每一步，该怎样保证它们做对事、不越界？

Lydia Hallie 用具体案例重新梳理了分工：项目里哪些知识仍要写进 CLAUDE.md，哪些旧指令应该清理；自动模式、拒绝规则、沙箱和云端环境分别解决什么问题；又该如何通过测试、hooks、CI 和主会话编排，让 Agent 在无人盯守时也能验证结果。适合正在使用 Claude Code、尝试多 Agent 并行开发的观众。

看点
1. 模型升级后，为什么旧的提示词和操作习惯可能拖累 Claude Code？
2. CLAUDE.md 应该保留哪些模型无法从代码中发现的信息？
3. 自动模式能处理日常审批，但哪些操作必须设置硬性限制？
4. 为什么批准运行测试，不等于测试进程可以安全访问所有文件？
5. 用明确的验收条件、hooks 和 CI，让 Agent 自己发现并修复问题。
6. 多个会话同时工作时，如何让一个主会话负责拆分任务和检查结果？

时间轴（依据原视频章节）
00:00 开发方式如何演变
02:14 重新思考最佳实践
04:11 管理自动模式
05:30 安全边界与运行环境
08:16 云端隔离环境
10:53 如何验证 Agent 的工作
14:00 用 CI 和 PR 扩展协作
15:10 多会话编排与总结
