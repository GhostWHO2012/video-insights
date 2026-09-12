# 翻译参考资料
项目：How Anthropic Builds： Lessons from Labs — Mike Krieger, Anthropic.audio.mp3
更新时间：2026-09-08 12:10:00

## 内容背景
- 原视频标题：How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic
- 视频链接：https://www.youtube.com/watch?v=qqrk7CtkuIw
- 频道：AI Engineer
- 发布时间：2026-08-27
- 视频时长：26:10
- 视频主题：Anthropic Labs 的产品构建方式、Claude/Claude Code 的使用方式、AI 时代的任务委派、代码评审瓶颈、快速试错组织机制、垂直 AI 与团队心理健康。
- 嘉宾：Mike Krieger，Instagram 联合创始人，Anthropic Member of Technical Staff，曾任 Anthropic 首席产品官，后转入 Labs 做个人贡献者。
- 场景：AI Engineer 活动现场访谈。主持人与 Mike Krieger 讨论他从 CPO 转为 IC 后如何使用 Claude、Anthropic Labs 如何组织项目，以及 AI 产品团队如何在更快的构建速度下保持判断力。
- 核心观点：
  1. 现在使用模型的方式正在从“拆小任务并委派”转向“描述目标状态，让模型自己推进并解释取舍”。
  2. 很多人仍然按过去的限制来提需求，真正的变化是要敢于对 AI 提出更大胆、更不按常规的要求。
  3. Claude Code 已经能承担大规模工程迁移，例如把数十万行 Python 在一个周末迁移到 TypeScript 并完成验证。
  4. AI 生成代码后的瓶颈不只是 code review 的时间，而是人类能否理解改动的意图、取舍和系统影响。
  5. Anthropic Labs 用两周一次的“persevere or pivot”节奏推进项目，快速原型、内部上线、early access，不行就关停。
  6. Labs 内部把项目方向称为 bets，团队围绕 bet 临时组建，bet lead 不一定管理任何人。
  7. Claude Design、Tag、Skills、Claude Code artifacts 等产品形态体现了 Claude 从聊天工具向可执行工作环境演进。
  8. 在大模型公司快速迭代的时代，创业公司仍然可以依靠垂直领域理解、用户洞察和快速行动建立优势。
  9. 金融等高风险场景需要在灵活性与可验证性、审计日志、数据来源追踪之间找到平衡。
  10. 高强度工作中，领导者应该能把压力、失望和脆弱表达出来，让团队更真实地讨论问题并继续交付。
- 翻译方向：偏 AI 产品、工程实践、组织设计和创业讨论。中文要自然、有工程感，专名和产品名尽量保留英文，避免把 Labs、bet、artifact、skill 等术语过度中文化。

## 人物身份/职业背景
| 英文名 | 中文参考 | 身份/职位 | 相关背景 | 翻译注意 |
|---|---|---|---|---|
| Mike Krieger | Mike Krieger | Instagram 联合创始人；Anthropic Member of Technical Staff；Anthropic 前首席产品官 | 负责/参与 Anthropic Labs 相关构建工作 | 默认保留英文名，不强行音译 |
| Tariq | Tariq | 活动中被主持人提到的演讲者 | 曾提出 be unreasonable 的表达 | 保留英文名 |
| Chris Lovejoy | Chris Lovejoy | 医疗健康/垂直 AI 相关嘉宾 | 与 Anthropic healthcare efforts 有关 | 保留英文名 |
| Carol Robbins | Carol Robbins | Stanford Touchy Feely 课程相关人物 | 主持人提到 AIE 开场分享 | 保留英文名 |

## 公司/产品/工具名
| 名称 | 类型 | 中文参考/说明 | 统一译法建议 |
|---|---|---|---|
| Anthropic | AI 公司 | Claude 开发方 | 保留 Anthropic |
| Anthropic Labs / Labs | 团队/组织机制 | Anthropic 内部偏实验、快速原型和探索的构建团队 | 保留 Labs 或译“Labs 团队”，不要频繁译成“实验室” |
| Claude | AI 助手/模型 | Anthropic 的 AI 助手 | 保留 Claude |
| Claude Code | 编程 agent / 代码工具 | 用于代码生成、迁移、审查和工程工作 | 保留 Claude Code |
| Claude Design | 产品/能力 | 与设计、artifact、可交互输出有关 | 保留 Claude Design |
| Claude Code artifacts | 产品能力 | 帮助解释 PR 意图、取舍和架构影响的说明性 artifact | 保留 Claude Code artifacts 或译“Claude Code artifacts 产物” |
| Tag | 产品/内部工具 | 可在 Slack 中 @ Claude 来委派任务 | 保留 Tag |
| Skills | 产品能力 | 可复用的 Claude/Codex 能力或工作流 | 保留 Skills / skill |
| Fable | 模型/内部代号 | 视频中提到刚重新启用、比人更聪明的模型/能力 | 保留 Fable |
| Mythos | 模型/内部代号 | 与 Fable 同时出现的内部快照/模型代号 | 保留 Mythos |
| Instagram | 产品/公司 | Mike Krieger 联合创办的照片社交产品 | 保留 Instagram |
| Burbn | 早期产品 | Instagram 前身产品 | 保留 Burbn |
| Slack | 协作工具 | 团队消息工具 | 保留 Slack |
| Git | 版本控制工具 | 代码工作流相关 | 保留 Git |
| Bun | JavaScript 运行时/工具链 | TypeScript 部署方案相关 | 保留 Bun |
| Python | 编程语言 | Instagram 和 Labs 项目相关 | 保留 Python |
| TypeScript | 编程语言 | 迁移目标语言 | 保留 TypeScript |
| PHP | 编程语言 | Instagram 代码迁移玩笑/对比 | 保留 PHP |
| Midjourney | 图像生成产品 | 用于类比多人协作式提示和委派 | 保留 Midjourney |
| Google Photos | 照片产品 | 用于创业公司与大公司竞争类比 | 可译“Google 的照片产品”或保留 Google Photos |
| Stanford Touchy Feely | 课程 | Stanford GSB 人际动力学课程 | 保留 Touchy Feely，首次可说明是 Stanford 课程 |

## 核心术语与统一译法
| 英文/概念 | 建议译法 | 说明 |
|---|---|---|
| build / builder | 构建 / 构建者 | 产品和工程语境，不要译成“建筑” |
| CPO / chief product officer | 首席产品官 / CPO | 首次可写“首席产品官（CPO）” |
| IC / individual contributor | 个人贡献者 / IC | 指非管理岗贡献者 |
| member of technical staff | Member of Technical Staff / 技术员工 | 是职位/头衔，不要译成泛泛的“技术团队成员” |
| Labs | Labs / Labs 团队 | 多指 Anthropic Labs，不要机械译“实验室” |
| be unreasonable | 大胆提出高要求 / 提出超出常规的要求 | 不是“不讲道理”或“无理取闹” |
| ask small | 只敢问小问题 / 把需求提得太小 | 指受旧产品限制影响 |
| task delegation | 任务委派 | |
| express the end state | 描述最终状态 / 说明目标状态 | AI 时代提示方式变化 |
| trade-offs | 取舍 | |
| go and cook on it | 自己琢磨并推进 / 自己打磨 | 口语表达 |
| port Python to TypeScript | 把 Python 迁移到 TypeScript | 大规模代码迁移语境 |
| codebase | 代码库 | |
| deployable | 可部署 | |
| dynamic workflow setup | 动态工作流设置 / 动态工作流 | |
| runtime configuration | 运行时配置 | |
| feature flag / knob | 功能开关 / 调节旋钮 | Instagram 扩展经验中的“knob”可译“可调开关” |
| Tag Claude in Slack | 在 Slack 里 @ Claude / tag Claude | 保留 tag 的产品/动作语感 |
| multiplayer delegation | 多人协作式委派 | 类比 Midjourney 的多人提示协作 |
| code review | 代码审查 / code review | 技术语境可保留 code review |
| review bottleneck | 评审瓶颈 / 审查瓶颈 | |
| comprehension bottleneck | 理解瓶颈 | 指人类能否理解大规模 AI 改动 |
| pull request / PR | PR / pull request | 可保留 PR |
| artifact | artifact / 说明性产物 | 不要泛泛译“工件” |
| intent and tradeoffs | 意图和取舍 | |
| persevere or pivot | 继续推进还是转向 | Anthropic Labs 两周评审机制 |
| pivot | 转向 | |
| wind down / shut down | 逐步关停 / 关掉 | 项目不行就结束 |
| bet / bets | bet / 探索方向 / 项目假设 | Labs 内部项目单位，不是金融下注 |
| bet lead | bet lead / 项目负责人 | 不一定管理人 |
| pod | 小组 / pod | 围绕 bet 组建的临时团队 |
| ad hoc group | 临时小组 | |
| early access | early access / 早期访问 | 产品试用阶段 |
| Project Unship | Project Unship | Slack 频道名，讨论从产品中删掉什么 | 保留英文，不译成“项目未发货” |
| skillified | 做成 skill / skill 化 | 不要译成“技能化”太生硬 |
| vertical AI | 垂直 AI | |
| domain knowledge | 领域知识 | 创业公司优势 |
| adoption and user love | 采用率和用户喜爱 | |
| finance track | 金融赛道 / 金融方向 | |
| evals | 评估 / evals | AI/金融场景下可保留 evals |
| barometer | 风向标 / 晴雨表 | |
| just-in-time analyses | 即时分析 | |
| dashboard | 仪表盘 | |
| verifiability | 可验证性 | |
| audit logging | 审计日志 | |
| data provenance | 数据来源追踪 / 数据血缘 | 金融场景更自然用“数据来源追踪” |
| burnout | 倦怠 / 职业倦怠 | |
| 996 | 996 工作制 | 保留 996，必要时译“996 工作制” |
| verbalize emotions | 把情绪说出来 / 表达情绪 | 领导力语境 |
| vulnerable | 脆弱 / 坦诚暴露脆弱 | 不要译成“易受攻击” |
| keep shipping | 持续交付 / 继续把东西做出来 | |

## ASR 易错词校正
| ASR 可能误识别 | 正确形式 | 说明 |
|---|---|---|
| Mike Kruger / Kriger / Krieger | Mike Krieger | 嘉宾名 |
| Anthropic lab / anthropic labs | Anthropic Labs / Labs | 保留 Labs |
| technical team member | Member of Technical Staff | 职位名 |
| Claude coat / Claude cold / Claude code | Claude Code | 工具名 |
| Claude design | Claude Design | 产品名 |
| Fable / fable | Fable | 模型/内部代号，保留 |
| Mythos / mythos | Mythos | 模型/内部代号，保留 |
| tag / Tag | Tag | 产品/动作，保留 |
| project unhip / unship | Project Unship | 结合上下文是“删/下线功能”的频道名 |
| bun / BUN | Bun | JS 运行时/工具链 |
| Typescript / type script | TypeScript | 语言名 |
| Python / python | Python | 语言名 |
| PHP / p h p | PHP | 语言名 |
| IC / icy | IC | 个人贡献者 |
| CPO | CPO | 首席产品官 |
| PR / pull request | PR / pull request | 代码审查语境 |
| artifact / artifacts | artifact / artifacts | 保留，不译“工件” |
| persevere or pivot | persevere or pivot | 机制名，可译“继续推进还是转向” |
| bets / bet | bets / bet | Labs 项目单位 |
| Chris Lovejoy | Chris Lovejoy | 人名 |
| Anterior / interior | Anterior | 医疗 AI 公司名，ASR 可能误作 interior |
| Carol Robbins | Carol Robbins | 人名 |
| Touchy Feely | Touchy Feely | Stanford 课程名 |

## 翻译风格规则
- 整体风格：AI 工程实践 + 产品组织访谈，中文要清楚自然，有工程和产品语感。
- 专名处理：Anthropic、Claude、Claude Code、Claude Design、Labs、Tag、Skills、Fable、Mythos、Bun、Python、TypeScript、Slack、Project Unship 等默认保留英文。
- “Labs”多数情况下保留为 Labs 或译“Labs 团队”，不要大量译成“实验室”，否则会显得像物理实验室。
- “be unreasonable”统一处理为“大胆一点 / 大胆提出高要求 / 提出超出常规的要求”，不要译成“不讲道理”。
- “bet / bets”在 Labs 语境中是项目假设或探索方向，不是金融下注。
- “artifact”在 Claude Code 语境中建议保留 artifact，可写“说明性 artifact”或“artifact 产物”，不要机械译“工件”。
- “skillified”可译“做成 skill”，比“技能化”自然。
- 技术字幕要短句优先；复杂概念如 code review bottleneck、data provenance、verifiability 可以保留术语但要保证中文顺。
- 访谈语气偏口语，允许“对”“是啊”“我觉得”等自然口语，但避免低模型常见的长句硬接。
- 涉及创业公司与大模型公司竞争时，语气保持中性，不额外加入评论。
- 涉及 burnout、996、mental health 时，翻译要稳，不要轻佻，也不要把“vulnerable”译成“易受攻击”。

## 待确认
- 当前参考基于 YouTube 元数据、简介、原版时间轴和已下载英文字幕整理。
- Fable、Mythos、Tag、Project Unship 属于视频内出现的产品/内部代号，若后续官方资料确认拼写不同，需要再统一替换。
- Chris Lovejoy 所属公司/背景在 ASR 中可能被识别为 interior，结合医疗 AI 语境暂按 Anterior 处理。

## 参考资料来源
- 视频标题：How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic
- 视频链接：https://www.youtube.com/watch?v=qqrk7CtkuIw
- YouTube 简介：AI Engineer 视频简介
- 原版时间轴：YouTube chapters / yt-dlp 元数据
