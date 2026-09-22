# D04 补课：最小模型客户端

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Hello-Agents固定版本第4章指定行，见日卡。
- OpenAI Python SDK官方说明（timeouts/retries）：https://github.com/openai/openai-python

## 今日只学以下内容
### 1. 配置和请求分开
get_config只接收一个映射，返回api_key/base_url/model；不读文件、不发网络。
程序入口显式读取项目根目录的.env，再传环境映射给get_config。
.env.example只有变量名和空值。真实.env只留本地。
### 2. 本次作业相对教材的明确改动
教材示例think使用流式响应；本作业先使用stream=False，减少流式分支。
教材的宽泛except返回None；本作业要求区分配置、超时和响应格式问题。
使用自己账户已经可访问的兼容模型服务，不预设免费额度或指定某个新模型。
### 3. 最小客户端结构
在make_text_model中创建SDK客户端；设置timeout=30.0、max_retries=0。
返回一个model(messages)可调用对象，每次请求使用config中的model。
从非流式响应的choices[0].message.content取文本。空文本或没有choices要明确报错。
真实使用的供应商如不支持该接口形式，要记录差异，不把模拟结果标真实连接。
### 4. 证据
报告存模型ID、时间、成功/失败类别、脱敏文本、SDK版本；绝不保存api_key。
一条好回答不是唯一联网证据，记录HTTP/SDK调用确实成功；模型是否遵循“只回复”单独判断。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
