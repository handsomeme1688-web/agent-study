# D08 补课：原生工具消息

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- 官方Function Calling，选择Chat Completions示例：https://developers.openai.com/api/docs/guides/function-calling

## 今日只学以下内容
### 1. 本作业明确使用的消息分支
工具定义放tools；助手响应里读取tool_calls。
每个call含id以及function.name和function.arguments；arguments仍需JSON解析和D5参数检查。
助手发出调用的完整消息先加入messages，再追加role=tool且tool_call_id相同的结果消息。
再请求模型得到普通文本答案；不能把第一次tool_calls当最终回答。
### 2. 先测三件事
手工夹具检查call_id对应；未知工具不能执行；一次多个调用仍受总工具次数限制。
超预算就明确终止流程，不能忽略未执行调用却继续声称全部处理完成。
### 3. 边界
Responses API使用另一套结果消息，不要把两套字段混起来。
本课程保留D6教学JSON主线；这天是独立协议适配实验，不要求全面迁移主项目。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
