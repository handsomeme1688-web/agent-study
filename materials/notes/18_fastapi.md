# D18 补课：最小API与错误码

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- 请求体：https://fastapi.tiangolo.com/tutorial/body/
- 测试：https://fastapi.tiangolo.com/tutorial/testing/
- 请求校验错误：https://fastapi.tiangolo.com/tutorial/handling-errors/
- 同步与异步：https://fastapi.tiangolo.com/async/

## 今日只学以下内容
### 1. 两个文件职责
schemas.py放请求与响应模型；api.py放HTTP路由与依赖注入；service.py保留业务。
导入api模块不能立刻调用外部模型或下载Embedding。
### 2. 端点
GET /health返回{"status":"ok"}。
POST /query接受question/mode；question去空白后1..500；mode只允许三个值；额外字段禁止。
create_app(query_fn=假函数)用于测试；真实app在请求时调用service。
### 3. 来源差异明确记录
教材13.2.5的文字写输入格式不正确返回400。
本作业采用FastAPI默认请求验证错误422，并按官方错误处理文档和本机测试检查；不是把教材文字改写成422。
本作业额外规定模型超时返回504且只给脱敏提示。
### 4. 先同步
使用普通def路由包装同步业务；不能只把def改async就说非阻塞。
本地数据库访问先串行化，连接在使用线程创建和关闭；并发工程后置。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
