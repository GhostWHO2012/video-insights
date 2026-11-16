翻译参考资料

原视频标题：All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI
原视频链接：https://www.youtube.com/watch?v=O_zcc6Xl12g
官方演讲页：https://ai.engineer/code/2026/talks/lauren-tan
参考译名：代码都是烂活（除了我的）｜Lauren Tan
主讲人：Lauren Tan（昵称 Potato，SpaceXSI 首席工程师，参与 Grok Bot 开发）
发布频道：AI Engineer
视频时长：17 分 31 秒

内容主线
这场演讲讨论如何让编码智能体在大量提交代码的同时维持质量。Lauren 的重点不是让智能体写更多代码，而是改造智能体工作的环境：把好的设计放进代码库，把重复出错的模式变成可执行的约束，再让智能体运行软件并验证行为。她用 Grok Bot 团队的开发实践说明这种方法。

演讲先介绍“信任金字塔”：优先改善代码库、API 和架构，其次使用 lint、类型、编译器与测试等确定性检查，再增加运行时和形式化验证；文字规则、AGENTS.md 和 Skills 仍有用途，但不能替代能自动执行的约束。随后以 Dune 框架、React 的 useEffect 限制、Electron 主进程与渲染进程的边界、功能地图、状态图和 UI 测试为例，说明怎样把反复出现的问题从人工审查中移走。

最后的数字是讲者报告的团队实践：她本人上个月向生产环境提交约 3,000 个 PR；Grok Bot 团队约 11,000 个 PR；回滚比例约 0.5%；10 月约 227 人至少贡献过一个 PR；稳定版客户端约每天发布一次。个人数字和团队数字不能混为一谈，也不能把回滚率译成全部缺陷率，或说这些数字证明所有团队都能复制同样结果。

人名、机构与产品
Lauren Tan：首次写 Lauren Tan（SpaceXSI 首席工程师），之后用 Lauren；Potato 是她的昵称，不是另一位讲者。
SpaceXSI：按视频标题和官方演讲页保留原文，不擅自改成 SpaceX、xAI 或 SpaceXAI。
Grok Bot：产品名保留英文。SpaceXSI 自己的产品页（x.ai/bot、x.ai 博客 Introducing Grok Bot）和招聘页都写作 Grok Bot；ai.engineer 演讲页写的 Graphbot 是笔误。自动字幕的 grokbot、gopbot、Graphbot 统一为 Grok Bot。
Dune：团队为 Grok Bot 创建的客户端框架，保留英文；不要译成“沙丘”。
Cursor：产品名保留英文。
pstack：Lauren 提到的工具／插件名，保留小写；自动字幕可能误听为 PAC、potato stack。相关链接：https://github.com/cursor/plugins/tree/main/pstack
Bombadil：用于 UI 的基于性质的测试工具，保留英文。
React、Electron、TLA+、Lean：技术名保持原样。useEffect、AGENTS.md、electron-main、electron-renderer 保持代码形式。

术语统一
slop：低质量、粗糙或难以维护的代码；标题中是带讽刺意味的说法。正文可依语气译为“烂代码”“粗糙代码”，不要机械地译成“泔水”。
agent／coding agent：智能体／编码智能体；说的是能操作代码和工具的软件智能体，不是人工代理。
pull request／PR：拉取请求／PR；不要译成“采购单”。
revert rate：回滚比例或回退比例；约 0.5% 是 PR 被回滚的比例，不等同于系统的完整缺陷率。
trust pyramid：信任金字塔；重点是把强约束放在代码库和确定性检查中。
deterministic check：确定性检查；如 lint 规则、类型检查、测试，能重复执行并明确拒绝不合规改动。
lint rule：静态检查规则；不要笼统译成“提示词规则”。
runtime verification：运行时验证；让智能体实际运行应用并检查行为。
formal verification：形式化验证；TLA+ 用于模型检查，Lean 用于证明选定算法或性质。不要说整个产品都经过形式化证明。
feature map：功能地图；从用户视角列出应用功能，帮助智能体找到正确位置。
statechart：状态图／状态机图；展示界面状态和转换，不等于单张截图。
property-based testing：基于性质的测试；这里涉及 UI 测试。
fuzzing：模糊测试；自动输入或探索应用以寻找异常。
software factory：软件工厂；指在可靠基础上自动化反复构建、测试和修复流程。

容易误译的论点
1. Lauren 强调先改善代码库和验证机制，再扩大自动化；不要写成“写更长的 AGENTS.md 就能解决质量问题”。
2. 限制 useEffect 是她们团队产品代码中的局部架构选择，不是说 React 的 useEffect 在任何项目中都不该使用。
3. 她批评的是把不良架构的临时补丁写进注释或规则，让后续智能体继续模仿；不要概括为“所有注释、文档和 Skills 都无用”。
4. Electron 主进程与渲染进程的例子说明目录结构与 lint 如何约束跨边界导入，避免卡顿；不要把它译成完全禁止进程通信。
5. 视频、截图、状态图和验证结果用于审查运行效果；并非所有代码都已无需人工判断。
6. 形式化验证、UI 性质测试和自动合并是不同层次的实践，不能说每个 PR 都有完整的数学证明。
7. 结尾的团队数据是 Lauren 在演讲中报告的成果；翻译时保留“大约”“约”等限定语。

官方视频简介中的时间轴（原视频相对时间）
00:00 把烂代码变成可靠产出
02:03 信任金字塔与代码库质量
05:00 Dune 与可执行的架构约束
06:56 用 lint 规则替代解释性注释
09:40 运行时验证与功能地图
10:50 形式化验证与 UI 测试
11:51 把更多算力用于验证
13:32 团队 11,000 个 PR 与约 0.5% 回滚比例
15:11 先打好基础，再建设软件工厂

字幕翻译要求
使用自然的简体中文保留现场演讲的幽默和强调。首次出现的英文人名、机构、产品和重要术语可用“英文原名（简短中文解释）”，之后保留原文。不要把 ASR 对 Grok Bot、PR、lint、pstack 等词的误识当成专名。保留个人与团队指标、局部做法与一般建议之间的区别。

补充（核对官方演讲页 https://ai.engineer/code/2026/talks/lauren-tan 与字幕后）
- 官方页列出 Lauren Tan 为 Principal Engineer、昵称 Potato；字幕里统一写 Potato。
- ai.engineer 演讲页把产品写作 Graphbot，但 SpaceXSI 官方产品页、博客和招聘页都写作 Grok Bot，以公司官方写法为准。
- Bret Taylor（ASR 误作 Brett）：以“一个周末重写 Google Maps”闻名的工程师。
- ASR 把 agents 误识成 Asians（#59）、prose 误识成 pros（#24）、AGENTS.md 拆成 agents, MD（#25、#30–31），已改。
- Cindy：推文作者，原文只说了名字，保留不加注。
- Chrome DevTools Protocol、VS Code、Next.js 也在演讲中出现，保持原名。


首次出现的英文专名加括号注释（字幕中只在第一次出现时加）
Potato（Lauren Tan 的昵称）；Grok Bot（AI 智能体应用）；SpaceXSI（SpaceX 旗下 AI 公司，原 xAI）；PR（代码合并请求）；
Bret Taylor（Google 地图联合创建者）；API（接口）；lint（代码检查）；bug（程序缺陷）；Skills（技能包）；
AGENTS.md（写给智能体的说明文件）；Next.js（React 网页框架）；Electron（桌面应用框架）；React（前端界面库）；
useEffect（副作用钩子）；Cursor（AI 编辑器）；electron-renderer（渲染进程）；electron-main（主进程）；
markdown（文本标记格式）；setTimeout（延时执行）；requestAnimationFrame（下一帧执行）；requestIdleCallback（空闲时执行）；
VS Code（微软代码编辑器）；JavaScript（脚本语言）；major GC（垃圾回收）；Chrome DevTools（开发者工具）；CLI（命令行工具）；
token（词元）；TLA+（形式化规格语言）；Lean（定理证明器）；UI（用户界面）；Bombadil（一个 UI 测试库）；statechart（状态图）；pstack（Potato Stack）。
不加注：Dune（句子里已直接说明是客户端框架）；Cindy（只知道是推文作者，没有可靠信息）；Lauren（演讲者本人）。
