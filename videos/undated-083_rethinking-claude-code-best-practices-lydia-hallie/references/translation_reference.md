# 翻译参考资料
项目：Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic [vlfCjWuv4es]
更新时间：2026-11-17

## 内容背景
- 原视频标题：Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic
- 视频链接：https://www.youtube.com/watch?v=vlfCjWuv4es
- 频道：AI Engineer（技术演讲，非访谈）
- 发布时间：2026-11-12
- 视频时长：约 17:31
- 场景：Lydia Hallie 在 AI Engineer 的演讲。开场说明上午现场演讲设备故障，临时回家用电脑重录，所以是单人独白、口语化、有即兴停顿。主题是：模型变强后，一年前 Anthropic 自己总结的 Claude Code 最佳实践哪些该丢、哪些该留、哪些该转移给模型/harness/环境。
- 核心观点：
  1. 会话形态从「1 个人盯 1~2 个会话、每步审批」变成「人当几十个长时间运行会话的经理」，cross 从 2026 年 5 月每天约 2,500 次合并增长到 9 月每天 3 万次以上。
  2. 人退出循环的每个动作（把控方向、审批命令、拒绝、检查输出、启动会话）都必须由模型、harness 或运行环境接手。
  3. 用当前默认配置即可：Opus 5.5 + auto mode（2026 年 8 月起为默认权限模式）；CLAUDE.md 只写 Claude 从代码里看不到的东西，用 /doctor prompt-audit 清理旧指令。
  4. 安全：可撤销的交给模型，不可撤销的（丢掉未提交改动、把密钥读进 transcript）写成 deny rule；权限只管工具调用能不能跑，管不了跑起来后能碰到什么，副作用要靠 sandbox 或 cloud session 限制。
  5. 验证：沿途设置 pass/fail 验证点（测试、构建、截图）；必须执行的用 hooks；测试失败脚本要 exit code 2，Claude 才会回去修；最后 CI 兜底，按风险决定人工 review 量。
  6. 编排：一个主会话当 orchestrator 拆分任务、启动子会话（threads）、判定结果并打回返工；主会话用擅长判断的 Fable，干活的 threads 用 Opus。
- 翻译方向：偏 AI 工程实践 / Agent 工作流 / DevOps 安全。中文要口语、清楚、有工程感；保持技术术语英文原貌为主，不要过度意译。

## 人物身份/职业背景
| 英文名 | 中文参考 | 身份/职位 | 相关背景 | 翻译注意 |
|---|---|---|---|---|
| Lydia Hallie | Lydia Hallie | Anthropic 团队成员，Claude Code 团队，做开发者关系（开发者布道/技术写作） | 演讲者本人；开场说明是重录版本 | 保留英文名，不音译 |

## 公司/产品/工具名
| 名称 | 类型 | 中文参考/说明 | 统一译法建议 |
|---|---|---|---|
| Anthropic | AI 公司 | — | 保留 Anthropic |
| Claude | 大模型/AI 助手 | Anthropic 的模型家族 | 保留 Claude |
| Claude Code | 编程 agent 工具 | 演讲核心工具，终端/编辑器里写代码 | 保留 Claude Code；**ASR 大量误识为 Clock Code / cloud code / clot / Cloakhook，务必按此修正** |
| Opus 4.5 / Opus 5.5 | 模型版本 | 旧模型 / 当前主力日常模型 | 保留 Opus 4.5 / Opus 5.5（ASR 曾写成小写 opus，统一大小写） |
| Fable 5.2 / Fable | 模型版本 | 本周新发布，擅长自我验证和判断；被推荐做 orchestrator 主会话模型 | 保留 Fable 5.2 / Fable（ASR 曾写成小写 fable） |
| Claude Code Projects | 功能 | 仍有 beta 标记；orchestrator 相关能力 | 保留 Claude Code Projects（ASR 误识为 Cloakhook projects） |
| CLAUDE.md | 项目指令文件 | 应只写 Claude 从代码看不到的上下文 | 保留 CLAUDE.md；**ASR 误识为 CloudMD / cloud md，务必修正** |
| auto mode | 权限模式 | 2026 年 8 月起为默认权限模式；对读写之外的命令跑独立分类器 | 保留 auto mode（ASR 误识为 Automode / automotive） |
| --dangerously-skip-permissions | CLI 参数 | 旧的高风险跳过审批方式 | 保留完整参数原文（ASR 拆成 dangerously + skip remission） |
| /doctor prompt-audit | 斜杠命令 | 检查 CLAUDE.md 和 skills，标出新模型不再需要的指令 | 保留 /doctor prompt-audit（ASR 误识为 Dr. Prompt Audit） |
| deny rule | 权限规则 | 明确禁止某工具调用，优先于 auto mode 分类器 | 译「拒绝规则 / deny rule」，首次可并列 |
| sandbox | 隔离机制 | 操作系统层限制命令可读文件/可写目录/可访问主机，含子进程 | 译「沙箱 / sandbox」 |
| cloud session | 云端会话 | Claude 自己的机器、全新 repo 副本，合上电脑也继续跑 | 译「云端会话 / cloud session」，注意与 Claude 区分：ASR 多处把 Claude 听成 cloud |
| hooks | 机制 | 在特定节点由 Claude Code 执行的脚本，保证验证点一定运行 | 保留 hooks，或译「钩子 / hooks」 |
| CI / CI Autofix | 持续集成 | 每个 PR 跑同一套检查；Autofix 让 Claude 看到检查失败后自行修复 | 保留 CI / CI Autofix |
| merge when ready | 功能 | 检查全绿后 GitHub 自动合并 PR | 保留 merge when ready，可译「就绪即合并」 |
| orchestrator | 会话角色 | 主会话，拆分任务、启动并判定子会话 | 保留 orchestrator，可译「编排器 / orchestrator」 |
| threads | 会话 | orchestrator 启动的新会话，各自干活 | 保留 threads（此处不是论坛帖子/线程，是子会话） |
| work trees | git 概念 | git worktree，多会话各自独立目录 | 保留 work trees，可译「工作树 / work trees」 |
| MCP servers | 工具协议 | 在 sandbox 之外运行 | 保留 MCP servers（ASR 写成小写 mcp） |
| GitHub / GitHub token | 平台/凭据 | PR 合并平台；token 不进 git | 保留 GitHub / GitHub token |
| npm test | 命令 | 示例命令：命令本身无害，但会执行依赖里别人写的代码 | 保留 npm test |
| .env / SSH keys / API key / network secret | 敏感信息 | .env 和密钥不进 git；云端会话用 network secret 注入 API key，不发给模型 | 保留原文；network secret 可译「网络密钥」 |
| Antique / Scion | 内部系统 | Anthropic 自研代码评审界面 / 版本控制系统（博客背景，演讲未展开） | 保留原文 |
| Monorepo | 代码库 | Anthropic 单一大仓库 | 保留 monorepo，可译「单一代码库 / monorepo」 |

## 核心术语与统一译法
| 英文/概念 | 建议译法 | 说明 |
|---|---|---|
| in the loop / out of the loop | 在循环里 / 退出循环 | 指人在流程中是否参与每一步；全片高频，不要译成「在环中」 |
| steering | 把控方向 / 引导 | 人退出循环的动作之一 |
| approving commands | 审批命令 | 不要译「批准指令」 |
| verification | 验证 | 与 safety（安全）并列的两大主题 |
| verification points | 验证点 | 沿途设置的 pass/fail 检查 |
| harness | 框架 / harness | 承载模型的运行框架（权限、分类器、规则） |
| environment | 运行环境 | 与 model、harness 并列，三选一接手人的动作 |
| defaults | 默认配置 | "use the actual defaults"＝用当前默认配置 |
| intent | 意图 | understanding your intent＝理解你的意图 |
| code base | 代码库 | 统一写「代码库」 |
| go off track | 跑偏 | 旧指令让模型跑偏 |
| tool calls | 工具调用 | 不要译「工具电话」 |
| side effects | 副作用 | 权限管不到副作用 |
| disposable | 一次性的 / 用完即弃 | 云端机器 disposable，但 commit 和消息会留下来 |
| force push | 强制推送 | git 操作 |
| pass or fail | 通过/不通过 | 验证点返回值 |
| split that into tasks | 拆成多个任务 | 让每个任务有自己的测试 |
| reviewed by Claude first | 先由 Claude 审 | 强调不是写它的那个会话审，是新 context |
| fresh context | 全新上下文 | 独立 context 带来的客观性 |
| autofix | 自动修复 | CI Autofix |
| double check every bug it finds | 复核它找到的每个 bug | 另一组 agent 做二次确认 |
| exit code 1 / exit code 2 | 退出码 1 / 退出码 2 | **关键**：退出码 1 时任务仍被标记完成；要用退出码 2 才会让 Claude 回去修。ASR 把 exit code 2 识别成 "a to exit code"，务必修正 |
| linter | linter / 代码检查工具 | 保留 linter |
| test suite | 测试套件 | 整包测试 |
| context switching | 上下文切换 | 讲者自述不擅长 |
| compact / clear | 压缩 / 清空 | context 管理动作 |
| prompt audit | 提示词审计 | /doctor prompt-audit 的简称 |
| legacy source | 遗留代码来源 | 示例：仍在服务但没在代码里被引用的目录 |

## ASR 易错词校正
（完整逐条列表见同目录 ASR识别错误检查报告.md；下表为最高频项，供翻译前统一替换）
| ASR 误识别 | 正确形式 | 说明 |
|---|---|---|
| Clock Code / cloud code / clot / Cloakhook / Cloud Code | Claude Code | 最高频，全片约 25 处 |
| CloudMD / cloud md | CLAUDE.md | 配置文件名 |
| Dr. Prompt Audit | /doctor prompt-audit | 斜杠命令，不是人名 |
| dangerously + skip remission | --dangerously-skip-permissions | 被拆成两条 |
| Automode / automotive | auto mode | 权限模式 |
| end file / same end | .env / .env file | 环境变量文件 |
| exit with a one / a to exit code | exit with exit code 1 / exit code 2 | 技术含义相反，最高优先级 |
| stare at it | steer it | 语义不同 |
| sears it | steers it | 全片总结句 |
| proved everything | approved everything | 审批 |
| we ask you to | we ask it to | 指代 agent |
| mcp / ssh / github / api / ci / pr | MCP / SSH / GitHub / API / CI / PR | 大小写统一 |
| fable / opus | Fable / Opus | 模型名大小写 |
| Opus 5.5 / Opus 4.5 / Fable 5.2 | 同左 | 数字正确，勿改 |

## 翻译风格规则
- 整体风格：技术演讲、口语独白。中文要自然、直接、有工程感；保留必要英文术语，不要把所有术语都翻译成中文。
- 产品名、工具名、命令名、文件名、参数名一律保留英文原文：Claude Code、Opus 5.5、Fable、CLAUDE.md、auto mode、deny rule、hooks、CI、orchestrator、threads、.env、MCP、PR 等。
- "in the loop / out of the loop" 统一译「在循环里 / 退出循环」，是全片主线概念。
- "cloud" 与 "Claude" 必须区分：ASR 把大量 Claude 听成 cloud，翻译时按上下文还原为 Claude；只有明确讲云端会话/cloud session 时才译「云端」。
- "thread" 本片指 orchestrator 启动的子会话，不要译成论坛「帖子/线程」。
- "exit code 1 vs exit code 2" 是全片核心技术结论，必须准确，不能含糊译为「错误码」。
- 数字严格照权威来源：2,500（5 月）→30,000+（9 月）、14%（人发现危险命令）、89%（auto mode 拦截）、约 1/10 漏过、August（auto mode 成为默认）。
- 语气：演讲者有即兴、自嘲、口头禅（you know、I think、kind of），中译可适度口语化，但不要加戏。
- 字幕短句优先，技术解释不要塞成超长句。
- 人名默认保留英文（Lydia Hallie）。

## 参考资料来源
- 视频：AI Engineer 频道，2026-11-12，https://www.youtube.com/watch?v=vlfCjWuv4es
- 公开逐字稿：bestblogs.dev/en/video/bc18b4a28（英文全文，用于逐句核对 ASR 错误）
- 结构化笔记：sparsenotes.com/posts/2026/11/rethinking-claude-code-best-practices-lydia-hallie
- Anthropic 官方博客（核实 2,500→30,000 数字）：anthropic.com/research/redesigning-source-control（2026-10）
- ASR 识别错误逐条报告：同目录 ASR识别错误检查报告.md

---

# 补充：Claude 整理的翻译参考（官方演讲页、讲者页、Anthropic 文档）

## 基本信息
- 中文标题建议：重新思考 Claude Code 最佳实践｜Lydia Hallie（Anthropic）
- 场合：AI Engineer Code Summit 2026（AIE CODE），旧金山，2026 年 11 月 11 日主会场，约 17.5 分钟；AI Engineer 频道发布。
- 主讲人：Lydia Hallie，Anthropic Claude Code 团队技术人员（Member of Technical Staff），负责开发者体验与技术教育。此前任 Bun 开发者体验负责人（Bun 于 2025 年 12 月加入 Anthropic），也在 Vercel 做过开发者体验工程师；JavaScript Visualized、JavaScript Questions 的作者，与 Addy Osmani 合作创建 Patterns.dev。
- 官方演讲页：https://ai.engineer/talks/vlfCjWuv4es-rethinking-claude-code-best-practices

## 内容概要
演讲讨论：模型变强以后，Claude Code 的旧最佳实践该怎么调整。以前一次会话要人一直盯着：引导方向、逐条批准命令、拦危险操作、检查输出、自己开下一个会话。现在这些工作没有消失，而是“搬家”了：方向交给模型，批准交给自动模式，硬性限制交给拒绝规则，隔离交给沙箱或云端环境，检查交给测试、hooks 和 CI，开会话交给编排者（Projects）。
核心一句：旧的最佳实践都还在，只是换了位置（"they're all still there, but they've just moved"）。翻译时不要写成“旧做法全部作废”。

## 结构（官方演讲页章节）
1. 从纠正一个会话到管理几十个（0:00）
2. 只保留 Claude 自己发现不了的项目知识（3:14）
3. 为什么推送到预发布环境会在自动模式下被拦住（4:12）
4. 用“能不能撤销”来决定哪些需要拒绝规则（5:32）
5. 被批准的测试进程能读到什么？（7:16）
6. 给整个会话一台全新的机器（9:26）
7. API 迁移后，已登录用户还保持登录吗？（10:47）
8. 让检查失败阻止任务完成（12:21）
9. 让每个 PR 都经过同样的检查（13:25）
10. 让一个会话协调其他会话（15:10）

## 关键事实与数字（讲者报告，不要改动含义）
- Anthropic 内部：5 月约每天 2,500 个改动，9 月每天超过 30,000 个。官方页没定义 changes 指什么，译作“改动”，不要擅自写成 PR 或提交。
- 8 月的研究：明显危险的命令，人类只拦下约 14%；自动模式拦下 89%，仍有约十分之一漏过去。不要译成“自动模式绝对安全”。
- 自动模式从 2026 年 8 月起成为默认权限模式（Pro、Max、Team 套餐，8 月 14 日起）。
- 拒绝规则是唯一的硬性拦截，在分类器之前生效；判断标准是“出错了能不能撤销”。回滚代码可以撤销；丢弃未提交的改动、泄露密钥不能撤销。例子：给 .env 设拒绝规则，连 cat .env 也会被拦。
- 本地沙箱由操作系统限制子进程能访问的文件、目录和主机，只管 shell 命令，不管 Claude 自己的文件读写、MCP 服务器和 hooks。
- 云端会话：Claude 在自己的机器上拿到一份全新的仓库克隆，合上笔记本也能继续跑；API 密钥可以作为网络密钥（network secrets）添加；网络默认只放行软件包仓库和 GitHub。往外推送的操作（推送提交、通过连接器发消息）仍然需要拒绝规则。
- 验证：用“通过/失败”的检查点代替逐行看 diff。OAuth 登录迁移的例子：同一个提示词可能产生三种看似合理的结果，其中一种会把所有用户登出。
- Hooks：每次编辑后跑 linter，任务完成时跑相关测试，会话结束时跑完整测试套件。脚本要以退出码 2 退出，Claude 才会回去修；退出码 1 不够。
- CI 是最后一道防线；CI 自动修复（CI autofix）让 Claude 修复失败的检查；GitHub 的“Merge when ready”（检查通过后自动合并）不是默认开启。
- Anthropic 的代码审查阶梯：每个 PR 先由 Claude 用全新上下文审一遍，用一组智能体复核 bug；人工审查按风险加码：文档类不需要人审，普通改动一人审，高风险改动两人审。
- 编排：Claude Code Projects（演讲时为 beta）接收一个目标，拆成任务，每个任务开一个会话（thread），把没做完的工作退回重做。分工：Fable 5.2 负责判断和编排，Opus 5.5 负责执行。上下文压缩和清空都是自动的。
- 建议先试：给 Claude 一个大得多的任务；确保 CI 覆盖重要的东西；配好环境（网络、密钥、初始化脚本）；从云端开始；记下自己还在哪些环节“在回路里”，那就是下一步要自动化的地方。

## 术语表（首次出现用“英文（中文解释）”，之后保留英文或用中文）
- Claude Code：保留英文。Anthropic 的智能体编程工具。
- best practices：最佳实践。
- session：会话。cloud session：云端会话。thread：Projects 里的子任务会话，译“子任务会话”，不要译成“线程”。
- harness：运行框架（Claude Code 自身的程序外壳，负责权限、工具调用等）。
- steering：引导方向。approving：批准。
- permission prompt：权限确认（弹窗）。permission mode：权限模式。
- auto mode：自动模式（由独立分类器审查每个操作的权限模式）。
- classifier：分类器。
- deny rules：拒绝规则；allow rules：允许规则；ask rules：询问规则。
- --dangerously-skip-permissions / bypassPermissions：跳过全部权限确认（旧的“危险”做法）。
- reversibility：可撤销性。
- sandbox：沙箱（本地 shell 沙箱）。
- cloud environment：云端环境。network access：网络访问。network secrets：网络密钥。setup scripts：初始化脚本。
- package registries：软件包仓库（如 npm）。
- CLAUDE.md：保留原文（写给 Claude 的项目说明文件）。首次可注“（项目说明文件）”。
- skills：Skills（技能包）。
- /doctor prompt-audit：保留原文（提示词审计命令，检查 CLAUDE.md、skills 等是否还是为旧模型写的）。2026 年 9 月 25 日在 Claude Code 2.1.283 加入，别名 /checkup prompt-audit。
- hooks：hooks（钩子，在固定时机自动运行的脚本）。
- exit code：退出码。
- linter：代码检查工具（lint）。test suite：测试套件。
- CI：持续集成（CI）。CI autofix：CI 自动修复。
- Merge when ready：保留英文（GitHub 的“检查通过后自动合并”选项）。
- worktrees：git worktree（工作树）。现在每个会话有独立机器，不用再手动管。
- PR：PR（代码合并请求）。
- orchestrator：编排者。orchestrate：编排。
- Claude Code Projects：保留英文 Projects（多会话编排功能）。不要和 claude.ai 里旧的 Projects（知识库）混为一谈。
- context compaction：上下文压缩。
- effort / effort level：推理强度（Claude Code 的设置项）。
- MCP servers：MCP 服务器（模型上下文协议服务器）。
- connectors：连接器。
- staging：预发布环境。
- OAuth / login API migration：登录 API 迁移；keep users signed in：保持用户登录状态。
- .env：环境变量文件（常存放密钥）。uncommitted changes：未提交的改动。
- npm test：保留原文。
- 模型名：Opus 4.5（旧模型）、Opus 5.5、Fable 5.2，全部保留英文写法。

## 可能的识别错误（按出现时核对）
- Opus forty-five / four five → Opus 4.5；Opus five five / fifty-five → Opus 5.5；Fable five two / fifty-two → Fable 5.2。第三方摘要里出现过“Opus 55”“Fable 52”，都是同一类错误。
- cloud code / Claude code → Claude Code；Claude MD / cloud MD → CLAUDE.md。
- doctor prompt audit → /doctor prompt-audit。
- dot env → .env；O auth → OAuth；N P M test → npm test。
- MCB / MPC → MCP；work trees → worktrees；auto fix → autofix；merge when ready 大小写统一为 Merge when ready。
- Lydia Halle / Hallie 拼写统一为 Lydia Hallie。

## 准确性提醒
- 旧最佳实践“换了位置”，不是“失效”。
- 自动模式不是万无一失：约十分之一的危险命令仍会漏过；不可撤销的操作要靠拒绝规则兜底。
- 沙箱只限制 shell 命令；云端会话也不等于外发操作安全。
- “不用逐行看 diff”的前提是有通过/失败的检查，不是“不需要检查”。
- 人工审查是按风险分级，不是“取消人工审查”。
- 2,500 / 30,000 是 Anthropic 内部数据，不能推广成“所有团队都能达到”。

## 翻译风格
使用自然的简体中文，保留演讲口语感，句子简短。首次出现的英文专名、产品名、功能名用“英文（简短中文解释）”，之后保留原文。设置项、命令、文件名（CLAUDE.md、/doctor prompt-audit、npm test、.env、退出码 2）保持原样，不翻译。
