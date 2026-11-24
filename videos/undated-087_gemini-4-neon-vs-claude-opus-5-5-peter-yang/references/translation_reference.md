# 翻译参考：I Tested Gemini 4 Neon vs Claude Opus 5.5 (Full Breakdown)

## 基本信息
- 视频：https://www.youtube.com/watch?v=iYIWuI5WfUo（YouTube 页面本次没能打开，标题取自文件名，频道、日期按内容推断）
- 作者：Peter Yang，频道/网站 Behind the Craft（BehindTheCraft.com），做 AI 工具实测和教程，视频里叫自己的“个人网站”
- 时长：约 17 分 54 秒；形式：单人录屏实测，口语快，自动字幕大段全小写无标点
- 背景：Gemini 4 Neon 于 2026-11-18 发布，是 Gemini 4 家族的中档模型（Hydrogen 与 Carbon 之间）；Claude Opus 5.5 于 2026-09-22 发布

## 内容结构（按时间）
1. 开场：Neon 口碑很好，号称追上前沿；跑分上 Neon 除部分智能体编程任务外全面领先 Opus，但他不信跑分，用 5 个场景实测：3D 旅行视频、游戏、网站改版、写作、被反驳时能否坚持立场
2. Google 三个前沿模型：Carbon≈Fable、Neon≈Opus、Hydrogen≈Sonnet；他的看法：99% 时间用 Neon，Carbon 只用于审计巨型代码库、大规模迁移这类小众场景，Carbon 实在太慢
3. Google AI Ultra 口播：每月 100 美元，含 Carbon/Neon/Hydrogen、YouTube Premium 家庭版、全家 20TB 云存储（Google 相册、云端硬盘）
4. 场景 1 涩谷十字路口 3D 视频广告：Neon、Opus 都约 40 分钟，Carbon 73 分钟；排名 Opus > Neon > Carbon
5. 场景 2 3D 怪兽游戏（哥斯拉摧毁涩谷）：Opus 画面最好但更卡（MacBook M5 上也卡）；Neon 画质像 PS1 但流畅；Carbon 坏了
6. 场景 3 网站改版（BehindTheCraft.com）：Neon 尚可但字太多、爱画雷达图；Carbon 元素塞爆；Opus 最有创意（衣架式界面、抽屉）
7. 场景 4 写作：三篇盲评文章（题目：假设你是不再需要手写代码的软件工程师，写一篇反思）；他偏好 A（Neon）> C（Carbon）> B（Opus）；Neon 更简洁，Carbon 啰嗦
8. 场景 5 给建议并坚持立场：让模型看他的 YouTube 频道给一条增长建议，再用 5 种方式反驳（诉诸情绪、拿出相反数据、社会认同、编造假事实等）；三个模型都能守住立场，只有给真实数据时才让步；他更喜欢 Opus 的建议
9. 结论：除 3D 和设计外，Neon 是第一个日常使用追上 Opus 的模型；“最佳模型”几周一换，要保持谦逊；他目前的实验室排名：Claude 第一、Gemini 第二、ChatGPT 第三
10. 收尾：最持久的是自己的 AI 技能和工作流系统（他放在私有 GitHub 仓库，任何框架、任何模型都能用）；推广他的 AI 课程与赠码活动；下期讲 Google Antigravity

## 术语表
| 英文 | 中文 | 首次出现注释 / 说明 |
|---|---|---|
| Gemini 4 Neon / Neon | 保留英文 | 首次：Gemini 4 Neon（谷歌 Gemini 4 的中档模型） |
| Gemini 4 Carbon / Carbon | 保留英文 | 首次：Carbon（Gemini 4 最强档） |
| Gemini 4 Hydrogen / Hydrogen | 保留英文 | 首次：Hydrogen（Gemini 4 轻快档） |
| Claude Opus 5.5 / Opus | 保留英文 | 首次：Opus 5.5（Anthropic 的旗舰模型）；Claude 不注 |
| Fable / Sonnet | 保留英文 | 首次：Fable（Claude 顶级档）、Sonnet（Claude 中档） |
| daily driver | 主力模型 / 日常主力 | — |
| frontier | 前沿（模型） | — |
| benchmark scores | 跑分 / 基准测试成绩 | — |
| agentic coding | 智能体编程 | — |
| holding its ground / push back | 坚持立场 / 反驳 | — |
| Google AI Ultra plan | Google AI Ultra 套餐 | 首次加注：谷歌最高档 AI 订阅 |
| YouTube Premium Family Plan | YouTube Premium 家庭版 | 不注 |
| Shibuya Crossing | 涩谷十字路口 | 直接译，不保留英文 |
| Godzilla | 哥斯拉 | 直接译 |
| plasma breath / magma breath | 等离子吐息 / 岩浆吐息 | — |
| laggy | 卡顿 | ASR 写成 leggy |
| BehindTheCraft.com | 保留英文 | 首次：BehindTheCraft.com（作者的个人网站） |
| call to action | 行动号召按钮 | — |
| AI slop | AI 味儿的套话 | 写作评价语境 |
| Antigravity | Antigravity | 首次：Antigravity（谷歌的 AI 编程工具） |
| Claude Code | Claude Code | 首次：Claude Code（Anthropic 的命令行编程工具） |
| Claude Max | Claude Max | 首次：Claude Max（Claude 高级订阅） |
| Grok Bot | Grok Bot | 首次：Grok Bot（SpaceXSI 的 AI 智能体）；ASR 写成 GrubBot / grog bot |
| Logan | Logan | 首次：Logan（Gemini 产品负责人 Logan Kilpatrick） |
| harness | 运行框架 | — |
| skills and workflows | 技能和工作流 | — |
| periodic table | 元素周期表 | 指 Gemini 4 用化学元素命名 |

## ASR 识别错误
- cloud / clod / Cloud → Claude（多处）；clock code → Claude Code；new cloud max → Claude Max
- grog / GrubBot / grog bot → Grok / Grok Bot；chat GP → ChatGPT；gemline → Gemini；anti-gravity → Antigravity
- opus 55 → Opus 5.5；99 of my work → 99%；gazella's → Godzilla's；leggy → laggy
- saa / sab / sac → essay A / B / C；opa said → Opus said
- knowledge, work, and science → knowledge work, and science
- my favorite out of the week → my favorite hour of the week
- the type memos → use it to type memos
- it also has ground the second paragraph → it also held its ground in the second paragraph
- 全小写段落恢复大小写：Neon、Carbon、Hydrogen、Opus、Fable、Sonnet、Shibuya、Godzilla、MacBook M5、PlayStation

## 存疑
- “a lot of ring effects”：按上下文（湿地面反光、氛围感强）写成 rain effects（下雨效果）
- “There are only two big cloud open ai and grog launches”：意思是“只做 Claude、OpenAI、Grok 这几家的大发布”，英文改成 Only do the big Claude, OpenAI, and Grok launches
- “writing specs for those two”：写成 for those tools

## 风格
- 口语、轻松的实测评测；“I think” 适当省略，保留作者的主观判断语气
- 数字用阿拉伯数字：40 分钟、73 分钟、100 美元、20TB、99%
- 不加注：Google、YouTube、Claude、ChatGPT、OpenAI、GitHub、MacBook、PlayStation、Google 相册/云端硬盘
