# D05 补课：JSON决策契约

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Python json.loads：https://docs.python.org/zh-cn/3.12/library/json.html#json.loads

## 今日只学以下内容
### 1. 两种消息，不是一个大列表
{"type":"tool","name":"search_docs","arguments":{"query":"工具 执行","k":3}}
{"type":"final","answer":"资料不足","citations":[]}
这两行是两个独立样例，一次只解析其中一行。
### 2. 校验顺序
先json.loads；检查顶层是dict；检查type；检查允许字段；再查名称与参数。
tool顶层只允许type/name/arguments；final只允许type/answer/citations。
search_docs只收query/k；read_chunk只收chunk_id；其他名称和字段拒绝。
缺省k补3，缺省citations补[]；字符串不能冒充整数，bool也不能冒充整数。
### 3. 分发职责
dispatch不能因为调用方是模型就信任输入；必须再校验后调用已登记函数。
不要使用eval、exec、globals、动态import去执行模型写的函数名。
参数错误发生时，Mock执行器应当assert_not_called。
### 4. 范围
这是本课程教学JSON，不是供应商原生工具协议。原生tool_calls在D8单独实验。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
