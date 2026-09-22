# 评测补课：题目、原始输出与人工分数

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- 主教材第12章的评估价值、效率/鲁棒性及人工验证，固定行范围见日卡。
- 本讲义的题型配比、指标口径是原计划沿用的教学设计，不是官方Benchmark。

## 今日只学以下内容
### 1. 题集字段
qid、question、type、expected_points、gold_evidence、should_abstain。
gold_evidence里的source/revision/start_line/end_line指原文，而不是可变分块ID。
开发20题=12单片段+4跨片段+4无答案；留出10题=6+2+2。
### 2. 人工核证顺序
先写5题；逐题打开原文找到结论；再补满30题。
跨片段题至少两处不同证据。无答案仅说明限定材料不足，不断言整个世界没有。
同一事实换个说法的题不要拆到开发和留出两边。
### 3. 原始结果字段
qid、mode、config_hash、retrieved_ids、answer、citations、status、duration_ms、model_calls、tool_calls、usage。
没有token用量写null，不写0。失败结果也保存一条。
### 4. 评分记录
每条评分写qid/mode/points_met/citations_supported/abstention_ok/reason。
任务成功必须满足预先要点与必要引用；无答案按正确说明不足判。
开发集任务成功分母20；留出分母10；证据召回只在可回答题上计算。
Citation ID确实存在，不等于原文语义真的支持结论。
### 5. 对照
关键词与向量RAG保持同一回答模型、提示、语料、题目，只换检索器。
先写逐题记录，再汇总。没有提升也保留结果，不删除失败题。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
