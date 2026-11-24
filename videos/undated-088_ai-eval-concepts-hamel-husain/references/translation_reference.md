# 翻译参考：AI Eval Concepts Explained in 15 Minutes

## 基本信息
- 视频：https://www.youtube.com/watch?v=3rlYBCDK0K4（YouTube 页面本次没能打开，标题取自文件名）
- 讲者：Hamel Husain（频道 Hamel Husain，已用 YouTube 官方嵌入接口确认；与 Shreya Shankar 合开 AI 评测课程）。视频里没报名字，字幕里不出现人名
- 时长：约 14 分 24 秒；形式：单人讲解 + 幻灯片，面向刚接触评测的人
- 讲解贯穿一个例子：电商 AI 助手帮用户**取消订单**

## 内容结构（按时间）
1. 开场：做 AI 产品要能衡量好坏；做一个评测入门
2. 产品专属评测 vs 基础模型基准测试：基准测试像 SAT、智商测试（MMLU、Terminal-Bench、Humanity's Last Exam），常用帕累托图展示（纵轴性能、横轴成本）；换成产品专属评测，帕累托前沿会完全不同
3. trace：一次用户会话里 AI 看到的全部内容（提示词、上下文、工具调用及结果、子智能体）；要给代码埋点、存进数据库、用 trace 查看器人工看
4. 标注与错误分析：描述哪里出错（例：取消失败却告诉用户“已取消”）→ 让 AI 帮忙把失败归类（虚假确认、订单搞错、漏转人工）→ 细化分组 → 先计数
5. trace 抽样：从探索（随机抽样，找“未知的未知”）到聚类、数据分析（轮数、延迟、工具调用数，找离群值）；刚开始多探索，但永远保留一定探索
6. 合成数据：用处有限，不要先用；只合成用户输入，再跑真实系统记录 trace；按场景生成（发货前/后、订单不明确、订单号不明确）；要像真实用户一样“乱”（“请取消蓝色那个”）；RAG 检索的反向生成：从文档生成问题
7. 自动化评测：本质是给 trace 打分，可离线也可接生产数据流；方式：写代码断言、分类器（决策模型或普通分类器）、LLM 评审；推荐二元评分（通过/不通过），不要 1–5 分或 0–100 分
8. 信任自动化评测：以人工标注为标准答案（AI 可以先提标签再人工确认）；两类错误：漏报、误报；数据分三份：训练集（给评审提示词当示例）、开发集（约 40%，调提示词、对齐人和评审）、测试集（最后检查有没有过拟合）
9. 部署：CI/CD、监控生产流量、护栏（拦在请求-响应路径上，挡住不安全内容）
10. 陷阱：通用指标（4.2 vs 4.5 vs 3.9 没有意义）→ 要测产品具体、可行动的失败；评测有成本，不是什么都建：先观察或复现问题、看是否需要反复迭代、设定上线门槛并编码进评测
11. 用评测改进产品：每次改提示词或代码就跑评测；可以让智能体自动爬坡优化，但要小心刷指标、要人工审提示词、要在没见过的测试用例上检查；换小模型：设定最低质量线，在质量不降的前提下降成本
12. 结尾：没讲的还有检索评测等；推荐下一期“AI 评测梯队榜”

## 术语表
| 英文 | 中文 | 首次出现注释 / 说明 |
|---|---|---|
| evals | 评测 | 首次：评测（evals） |
| product-specific evals | 产品专属评测 | — |
| foundation model benchmarks | 基础模型基准测试 | — |
| SAT / IQ test | SAT（美国高考）/ 智商测试 | — |
| MMLU | MMLU | 首次：MMLU（多学科知识测试） |
| Terminal-Bench | Terminal-Bench | 首次：Terminal-Bench（命令行任务测试） |
| Humanity's Last Exam | “人类最后的考试” | 首次保留英文：Humanity's Last Exam（人类最后的考试）；ASR 写成 Humanities |
| Pareto chart / frontier | 帕累托图 / 帕累托前沿 | — |
| LLM | LLM | 首次：LLM（大语言模型） |
| trace | trace | 首次：trace（完整调用记录） |
| trace viewer | trace 查看器 | — |
| instrument your code | 给代码埋点 | — |
| sub-agents | 子智能体 | — |
| annotate | 标注 | — |
| error analysis | 错误分析 | — |
| taxonomy | 分类体系 | — |
| false confirmations / wrong orders / missed handoffs | 虚假确认 / 订单搞错 / 漏转人工 | — |
| sampling / random sampling / clustering | 抽样 / 随机抽样 / 聚类 | — |
| unknown unknowns | 未知的未知 | — |
| outliers | 离群值 | — |
| synthetic data | 合成数据 | — |
| RAG / retrieval / corpus | RAG / 检索 / 文档库 | 首次：RAG（检索增强生成） |
| automated evals | 自动化评测 | — |
| grading | 打分 | — |
| classifier / decision model | 分类器 / 决策模型 | — |
| LLM as a judge | LLM 评审 | 首次：LLM 评审（LLM-as-a-judge）；ASR 写成 lm as a judge |
| binary scores / pass / fail | 二元评分 / 通过 / 不通过 | — |
| ground truth | 标准答案 | — |
| missed failures / false alarms | 漏报 / 误报 | — |
| train / dev / test set | 训练集 / 开发集 / 测试集 | — |
| overfit | 过拟合 | — |
| hill climbing | 爬坡优化（不断调优） | — |
| CI/CD | CI/CD | 首次：CI/CD（持续集成与部署） |
| guardrails | 护栏 | 首次：护栏（guardrails） |
| generic metrics | 通用指标 | — |
| actionable | 可行动的 | — |
| hack this metric | 刷指标 | — |
| low hanging fruit | 唾手可得的收益 | — |
| tier list | 梯队榜 | — |

## ASR 识别错误
- Humanities Last Exam → Humanity's Last Exam；Terminal Bench → Terminal-Bench
- an lm as a judge → an LLM as a judge（2 处）；CICD → CI/CD
- Emails are best for things → Evals are best for things
- your finish prompt → your finished prompt；have AI proposed labels → have AI propose labels
- 后半段大段无标点，按语义补标点和大小写

## 风格
- 教学讲解，清楚、口语、准确；例子（取消订单）前后一致
- 数字用阿拉伯数字：1 到 5 分、0 到 100、40%、4.2、4.5、3.9
- 不加注：AI、SAT 以外的常见词；电商
