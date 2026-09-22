# D06 补课：先用假模型做循环

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Hello-Agents固定版本 code/chapter4/ReAct.py 指定行，见日卡。
- unittest.mock：https://docs.python.org/zh-cn/3.12/library/unittest.mock.html

## 今日只学以下内容
### 1. 分成四次实现
第一版只支持model直接返回final。
第二版支持tool后final；工具返回值必须加入下一轮messages。
第三版支持错误出口：bad_decision、timeout、tool_error。
第四版加步数上限step_limit，以及独立调用不共享历史。
### 2. ScriptedModel是什么
它不是模型效果测试，而是按你给的顺序返回固定响应的函数对象。
先喂一个tool字典，再喂final字典；打印第二次收到的messages确认工具结果已出现。
今天可以把工具观测作为带标签的user消息回填；不能伪造缺tool_call_id的原生tool消息。
### 3. 计数约定
steps是实际调用model的次数；第一次调用即1。
max_steps=2时最多问两次模型；第2次仍要工具则执行后结束为step_limit。
工具执行次数与模型轮次不是同一字段。D15再增加业务工具预算。
### 4. 不能靠循环上限解决的事
一次网络调用已经阻塞时，max_steps不能打断它。网络请求还需客户端自身timeout。
记录工具名、参数摘要、结果状态即可；不要求记录模型内部推理。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
