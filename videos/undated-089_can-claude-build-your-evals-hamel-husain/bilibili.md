# 【中英双语】Claude 能直接帮你搭建 AI Eval 吗？| Hamel Husain

B站视频：https://www.bilibili.com/video/BV1vVykzzEiT/

https://www.youtube.com/watch?v=5ykulgyB8kk
原视频标题：Can Claude Build Your Evals?
原视频链接：https://www.youtube.com/watch?v=5ykulgyB8kk

Anthropic 推出可帮助设计评测的 Claude Skill：它会询问要测什么、挑选目标、编写评判器，再让人检查结果。Hamel Husain 和 Isaac Flath 把它用在一组他们熟悉的租房助手数据上，现场测试 100 段真实对话，看看自动设计 eval 的流程是否经得起检验。

结果并非一面倒：Claude 确实找出了一些细微的转人工失败；但它要求团队在读原始对话前就决定评什么，又把关键审阅工作放进 Markdown 文件，生成的部分代码评测还捆绑了太多条件。两人最终认为，这次流程不如先做一个好用的数据查看器、亲自读 trace，再决定写哪条 eval。适合关心 Claude Skill、AI 评测自动化与真实产品质量的观众。

时长：47 分 58 秒
语言：英语 → 简体中文
说话人：Hamel Husain、Isaac Flath
频道：Hamel Husain
发布时间：2026-10-13

看点（根据视频简介与字幕整理）
1. Claude 自动设计评测的流程，第一步为什么就引发争议。
2. 100 段真实租房助手对话中，模型到底找到了哪些问题。
3. “请求转人工却被反复追问”的案例，为什么需要看完整 trace。
4. 用 Markdown 文档审标签，会给人工核对增加什么阻力。
5. 把多种转接条件塞进一个代码评测，结果为何难解释。
6. 两人怎样逐条复核 Claude 的判定，并在过程中改变看法。
7. 最终评价针对这次实测流程，不应泛化成所有自动评测都无效。

时间轴（翻译自原视频简介，保留原时间点）
00:00 Anthropic 关于自动设计评测的文章
00:53 评测设计原则：哪些观点两人赞同
02:16 人类觉得困难的案例值得优先挑选吗
03:51 自动构建 eval 的 Skill 应怎样工作
08:30 租房助手的 100 条真实调用轨迹
10:24 把调用轨迹交给 Skill
11:24 Claude 先问应该评什么行为
14:37 Claude 找到了真实失败模式
16:46 这里应该展示原始调用轨迹
20:34 在 Markdown 文件中审阅标签
28:14 一个条件过多、容易失效的代码评判器
34:07 逐条审阅 Claude 的判定
37:00 未能完成转人工，需要单独评测
40:56 应该先建 eval，还是先看数据
46:02 本次实测结论
