# 翻译参考：Muse Deep-Dive — Mona Sarantakos（Lenny's Podcast）[WY0cdD4gNoQ]

## 基本信息
- YouTube 标题：Muse Deep-Dive: Behind the most successful consumer AI product launch this year | Mona Sarantakos（本地文件夹名是旧标题“Meta’s Muse: How we launched the most successful consumer product this year”）
- 频道：Lenny's Podcast，2026-11-15 发布，约 87 分钟。访谈形式：主持人 Lenny Rachitsky，嘉宾 Mona Sarantakos。
- 中文标题建议：Muse 深度复盘：今年最成功的 AI 消费级产品是怎么做出来的｜Mona Sarantakos（Meta）

## 人物
| 英文 | 中文处理 | 身份 | 注意 |
|---|---|---|---|
| Mona Sarantakos | 保留英文 | Meta Superintelligence Labs 产品副总裁、Muse 产品负责人；在 Meta 约 10 年，做 PM 20 多年；这是她第一次上播客 | 首次出现可注“（Muse 产品负责人）” |
| Lenny Rachitsky / Lenny | 保留英文 | 主持人，Lenny's Newsletter / Lenny's Podcast | — |
| Nat Friedman / Nat | 保留英文 | Meta Superintelligence Labs 产品负责人，前 GitHub CEO；最早拉团队试用 OpenClaw | ASR 写成 NAT |
| Alex Wang（Alexandr Wang） | 保留英文 | Meta 首席 AI 官，前 Scale AI CEO；负责模型（Muse Spark） | 节目里叫 Alex Wang，注意和 Alex Cornell 区分 |
| Mark Zuckerberg / Mark / Zuck | 保留英文 | Meta CEO；提出“个人超级智能” | 首次可注“（Meta CEO）” |
| Alex Cornell | 保留英文 | Muse 首席设计师（设计总监），做了第一个原型和 Jolly | — |
| Christine Awad | 保留英文 | Muse 工程经理，团队里最爱用 Muse 购物的人 | ASR 写成 Christina Wadd |
| Tarek | 保留英文 | Muse 技术负责人、核心架构师 | — |
| Nan Yu | 保留英文 | 前 Linear 产品负责人，现在在 OpenAI | 引用他的话：PM 要像客户一样感受痛苦 |
| Fu / Quinn | 保留英文 | 两位员工给自己的 Muse 起的名字 | 两个 Muse 在群聊里“泄密”、吵架的故事 |

## 产品 / 公司 / 名词
| 英文 | 统一译法 | 说明 |
|---|---|---|
| Muse | 保留 Muse | Meta 的个人 AI 智能体 App，2026-09-08 上线，约 10 天后登上美区 App Store 免费榜第一。首次注“（Meta 的个人 AI 智能体）” |
| Muse Spark | 保留 Muse Spark | Meta 超级智能实验室的首个模型系列，2026 年 4 月发布；Muse 背后的模型。ASR 写成 MuseSpark |
| Meta AI | 保留 Meta AI | Meta 原有的 AI 助手产品。ASR 写成 MetAI |
| Meta Superintelligence Labs (MSL) | Meta 超级智能实验室 | 也说 the lab / the superintelligence org |
| personal superintelligence | 个人超级智能 | Zuckerberg 2025 年的公开信《Personal Superintelligence》 |
| OpenClaw | 保留 OpenClaw | 开源的个人 AI 智能体，跑在自己的电脑（Mac Mini、树莓派）上。ASR 多处写成 open cloud / the open claw。首次注“（开源个人智能体）” |
| Grok Bot / Claude Duet / Dots | 保留英文 | 同期的个人智能体产品：SpaceXSI 的 Grok Bot、Anthropic 的 Claude Duet、OpenAI 的 Dots。ASR 把 Grok Bot 写成 grokbach |
| Mac Mini / Raspberry Pi | Mac Mini / 树莓派 | 跑 OpenClaw 的设备 |
| Jolly / Jolly Bot | 保留 Jolly | Muse 顶部的毛绒小动物头像，最初是临时占位；名字来自设计师给女儿起的昵称 Jolly Bug |
| harness | 运行框架（harness） | 让模型变成智能体的外壳 |
| agent / agentic | 智能体 / 智能体能力（很强） | “way more agentic” 译“智能体能力强得多” |
| Sentinel | Sentinel（哨兵） | 独立于 Muse 核心智能体之外的安全兜底系统 |
| dreaming / study | “做梦”/“学习” | Muse 在后台持续思考用户目标的功能，首次可加引号 |
| goals tab | “目标”标签页 | — |
| zero basing | 归零重建 | 推倒重来 |
| dogfooding | 内部试用 | — |
| alpha testers | 外部 alpha 测试用户 | — |
| red teaming | 红队测试 | — |
| eval / eval bar | 评测 / 评测门槛 | 章节：Evals: structure, hierarchy, and ownership |
| benchmarks | 基准测试 | — |
| agent swarms | 智能体集群 | 用来挖掘用户洞察 |
| synthetic data | 合成数据 | — |
| agentic commerce | 智能体购物（代理式电商） | 章节名 |
| activation / word of mouth | 激活 / 口碑传播 | — |
| ambient agents | 常驻后台的智能体 | — |
| financial betterment | 改善个人财务 | — |
| H1 brief | 上半年规划简报 | — |
| Spirit Week | 学校“精神周” | 美国学校每天换主题着装的活动 |
| charm | charm（挂坠式设备） | Meta 即将推出的挂坠式 AI 小设备 |
| main chat / side chat | 主对话 / 侧边对话 | Muse 只用一个主对话的设计争议（“主对话派”和“侧边对话派”） |
| ideas tab | “灵感”标签页 | 预置的入门任务包 |
| cron | cron（定时任务） | — |
| UXR panel | 用户研究（UXR）小组 | 3 月开始的长期用户研究小组 |
| Workplace | Workplace（Meta 内部协作平台） | 类似内部版 Facebook 群组 |
| let them cook | 放手让他们干 | 内部口号 |
| Muse leads group | Muse 负责人小组 | — |
| Tamagotchi | 电子宠物 Tamagotchi | 比喻“照看智能体” |
| Menlo Park | 门洛帕克（Meta 总部） | — |

## 内部口号（保留英文 + 中文）
- “Trust is a must” → 信任是刚需（押韵，意思是没有信任就没人用）
- “The claw is the law” → Claw 即法则（Nat Friedman 写的文档标题，意思是 OpenClaw 代表的方向就是准则）

## 赞助商（片中口播保留原文）
- WorkOS：企业级功能（SSO 单点登录、SCIM、RBAC、审计日志），AgentAuth、auth.md、Airlock。
- DX：AI 时代的工程效能平台。

## 章节（YouTube 描述）
00:00 预告｜01:24 开场与背景｜02:14 和早期智能体度过的一个周末｜09:08 七个月的上线时间线｜14:07 “Claw 即法则”｜15:53 领导层对 Muse 的影响｜23:37 Jolly 的由来｜29:53 优先场景和一个购物惊喜｜35:03 智能体购物｜38:03 智能体集群与合成数据｜42:48 评测：结构、层级与归属｜46:37 激活与口碑｜51:09 设计上的押注｜57:04 原型文化与两个互相竞争的 Muse｜1:01:54 PM 角色的变化｜1:09:05 Muse 的第一个原型｜1:10:37 差点没跑通的董事会原型｜1:12:00 团队规模与文化｜1:20:55 接下来：常驻智能体与改善财务

## 关键事实（不要改动含义）
- Muse 2026-09-08 上线，约 10 天后登上美区 App Store 免费榜第一；嘉宾说“从想法到上线用了七个月”，Lenny 对比 Grok Bot、Claude Duet、Dots 只用了几个月。
- 起点：1 月底 / 2 月初 Nat Friedman 发消息让大家试 OpenClaw；Mona 周末用树莓派搭起来，第二个周一早上收到它整理的学校通知简报，觉得“很神奇”。
- 三个阶段：先搞清楚产品是什么；然后在可靠性、安全、隐私安全上花了大部分时间；中间不断做内部试用和外部 alpha 测试。
- 嘉宾说上线后“到目前为止没有出过灾难性问题”，不要译成“从没出过问题”。

## 识别错误（ASR）统一修正
- open cloud / the open claw → OpenClaw
- MetAI → Meta AI；MuseSpark → Muse Spark；Meta Super Intelligence Labs → Meta Superintelligence Labs
- grokbach → Grok Bot；NAT → Nat；work os → WorkOS
- news knows / music can（指 Muse）→ Muse knows / Muse can
- president（指先例）→ precedent；crash catch phrase → catchphrase
- 全小写段落里的人名、产品名恢复大小写：Mark、Nat、Alex、Muse、Meta、Jolly
- you should try views / talk to your views → Muse；feed into our emails → evals；this formed were critical → these swarms
- Christina Wadd → Christine Awad；open clock → OpenClaw；data different production → data from production
- break evals → build evals；a linear head of product → Linear's head of product；Facebook live → Facebook Live
- many IMUs → Meta AI, Muse；onboarding float → flow；ambi → ambient；in between fees → in-between phase
- charm：结尾提到“有个 charm 会发布，一个小设备”，指挂坠式的 AI 设备，开头的 charm devices 也是它；译“charm（挂坠式设备）”

## 翻译风格
- 访谈口语，简体中文自然、直接；嘉宾语速快、口头禅多（like、you know、kind of），中文适度保留口语感但不逐字翻口头禅。
- 产品名、人名保留英文；首次出现的英文专名加括号中文注释，之后不再加。
- 字幕短句，中英文同时切换。
