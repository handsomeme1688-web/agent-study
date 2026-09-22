# D25 选修：同一业务的另一种表示

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- 主教材Dialogue_System.py状态及建图范围，见日卡。
- Graph API官方补充：https://docs.langchain.com/oss/python/langgraph/graph-api

## 今日只学以下内容
### 1. 先认出教材三个结构
TypedDict定义State；节点读取状态返回更新；add_edge连接先后关系；compile生成可运行图。
教材示例业务是搜索助手，依赖额外搜索服务；本日不运行它的真实Tavily业务。
### 2. 自己只迁移已有循环
State保留messages/steps/answer/status；节点调用已有model与execute。
条件边决定继续工具/再次决策/结束；自己的预算仍要显式检查。
### 3. 不加范围
不换模型，不换语料，不加多Agent、checkpoint数据库或长期记忆。
四个固定假模型场景两版比较；结论继续用while也合格。
### 4. 跳过
主线未过，使用start_day.py 25 --skip-optional，仅记录后置，不生成未完成的框架测试阻塞CI。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
