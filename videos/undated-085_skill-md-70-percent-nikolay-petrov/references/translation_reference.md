# 翻译参考：Your SKILL.md Is 70% Stuff the Model Already Knows — Nikolay Petrov, Intel

## 基本信息
- 视频：https://www.youtube.com/watch?v=yzx4IuEh_tU
- 频道：AI Engineer（AI 工程师大会官方频道），2026-11-11 发布，时长 14:00
- 讲者：Nikolay Petrov，Intel（英特尔）。ASR 拼成 Nikolai，官方写法是 **Nikolay**
- 形式：单人技术演讲，带幻灯片，讲者非英语母语，句子经常不完整、几乎不断句

## 内容要点（翻译时用来判断上下文）
1. Skill 分两类：**知识型**（教模型新东西）和**引导型/流程型**（不加新信息，只让动作流程可重复）。本次只讲知识型。
2. 常规验证方法是**评测（evals）**：同一组任务跑**两组对照（two arms）**，一组不加载 Skill，一组加载。例子：不加载 5 题做对 3 题，加载后 5 题全对。另外比较 token 用量和耗时。
3. Skill 能用之后想精简（省 token），逐行删改再重跑评测属于**暴力穷举**。
4. 他的方法借用 **FActScore**（一种评估事实准确性的方法，把文本拆成"原子事实"逐条核对）的思路：把 Skill 拆成 25～30 个 **atom（原子项）**，每个是一组"问题 + 期望答案"。原子项可以是一般性的 **proposition（命题）**，也可以是要求更明确的 **contract（契约）**。
5. 每个原子项也跑两组（有/无 Skill），由 **judge（评审模型）** 或 **panel of judges（评审团）** 打分，评审最好用别的模型家族；还要检查问题本身不会**泄露答案**。可以**不给工具**测模型内部知识，或者**给工具（如联网）**测实用情况。
6. 得到**四格结果矩阵**：
   - 有无 Skill 都答对 → Skill 没起作用，模型本来就会
   - 不加载能答对、加载后反而答错 → Skill **有害**，最该先改
   - 不加载答不对、加载后能答对 → 理想情况，**教会了模型新东西**
   - 两边都答不对 → Skill 写得不清楚
7. 热门 Skill 里有害项很少：Anthropic 官方 Skill 约 400 个原子项里只有 1 个；小众 Skill 更常见。
8. 可以按行/按原子项给 Skill **上色**，可视化哪些是新知识、哪些模型已经知道。
9. 成本：29 个 Skill 只花了约 **14 美元**（Sonnet 和 Haiku 调用，Sonnet 当评审）。
10. **宽松（lenient）** vs **严格（strict）** 检查：宽松看大意，严格看确切的键、参数、取值、步骤。**Opus** 宽松 70%，严格只有 **22%**。结论：新模型概念掌握得好，但仍需要给精确细节。
11. 比较了三个热门 Skill 仓库在不同模型上的结果：小模型整体理解更低；不同 Skill 差别很大；有些 Skill 本来就是"方向性"的，这不算坏事。
12. **novelty（新颖度）** 只是一个信号，是"优化的初始方向"（initial vector for optimization）；删掉已知内容后**必须重跑评测**确认结果不变。
13. 所有实验都用 **Docami**（他们的框架，用来比较和智能体、上下文相关的一切：Skill、AGENTS.md、MCP、工具）完成；它还能评估上下文影响、**路由（routing）**、对比 Skill 描述和命名。
14. 结尾：请大家写出更好的 Skill。

## 术语表
| 英文 | 中文 | 首次出现注释 / 说明 |
|---|---|---|
| skill / SKILL.md | Skill / SKILL.md | 首次：Skill（技能包）；保留英文 Skill，不译"技能" |
| agent | 智能体 | — |
| knowledge skill | 知识型 Skill | — |
| steering / process skill | 引导型 / 流程型 Skill | — |
| evals | 评测 | 首次：评测（evals） |
| two arms | 两组对照 | 一组不加载 Skill，一组加载 |
| tokens | token | 首次：token（词元） |
| brute force | 暴力穷举 | — |
| FActScore | FActScore | 首次：FActScore（事实性评测法） |
| atom | 原子项 | 首次：atom（原子项）；ASR 常听成 items |
| proposition / contract | 命题 / 契约 | — |
| judge / panel of judges | 评审模型 / 评审团 | — |
| leak answers | 泄露答案 | — |
| four outcomes matrix | 四格结果矩阵 | — |
| lenient / strict | 宽松 / 严格 | — |
| frontier models | 前沿模型 | — |
| Opus / Sonnet / Haiku | 保留英文 | 首次：Sonnet 和 Haiku（Anthropic 中小模型）；Opus（Anthropic 大模型） |
| novelty | 新颖度 | 首次：novelty（新颖度） |
| initial vector for optimization | 优化的初始方向 | — |
| AGENTS.md | AGENTS.md | 首次：AGENTS.md（智能体说明文件） |
| MCP | MCP | 首次：MCP（模型上下文协议） |
| Docami | Docami | 首次：Docami（评测框架）；拼写按发音，网上查不到这个名字 |
| routing | 路由 | 指 Skill 被触发、选中的过程 |
| repos | 仓库 | — |

## ASR 识别错误（已核对上下文）
- Nikolai → Nikolay；the fact score → FActScore；items（指拆出的条目时）→ atoms
- their（几乎全片，口音）→ the；they're no skill loaded → where no skill is loaded
- we skill with all link all five → with skill we're solving all five
- it's all some evals → it solves some evals；at the sense → in essence
- prevalent context → relevant context；this is much our expectations → this matches our expectations
- three popular rappers → three popular repos；you probably haven't come off those → you'll probably come across those
- revelation → evaluation；there also evolves → there are also evals
- the stage there we have / cases there we want / contracts there we put → where
- 全小写段落恢复大小写：GitHub、Anthropic、Opus、Sonnet、Haiku、MCP、AGENTS.md

## 风格
- 技术演讲，口语但准确；讲者句子不完整时按意思补全成通顺中文，不逐字硬译
- 数字保留阿拉伯数字：3/5、25～30 个、400 个、29 个、14 美元、70%、22%
- 不加注：广为人知的名字（GitHub、Anthropic、Intel）
