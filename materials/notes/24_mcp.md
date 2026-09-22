# D24 补课：服务器和真正客户端

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- 官方服务端（2026-07-28版本）：https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
- 官方客户端（2026-07-28版本）：https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client

## 今日只学以下内容
### 1. 不照抄天气业务
教程14_weather_mcp_server.py用HelloAgents的MCPServer封装，读的是创建/注册/运行职责。
本课程包装自己的search_docs，使用官方SDK，不新增天气账户。
### 2. 版本必须一致
本次查阅的官方客户端教程要求Python MCP SDK 2.0或更高，示例使用Client。
它与很多旧文章的ClientSession示例不同；安装2.x时按此处固定官方文档，不混用两代API。
安装不成功或接口不符就记录版本差异，暂后置；不要整环境无差别升级。
### 3. 真正的客户端
客户端通过stdio启动子进程；进入连接上下文后list_tools，再call_tool；退出时关闭。
测试客户端不需要另一家LLM账户：只发现和调用工具即可验收协议。
子进程用sys.executable启动-m agent_lab.mcp_server，cwd为明确的项目根目录。
### 4. 标准输出
stdout给协议；调试日志写stderr。只暴露query/k，不暴露任意文件、会话或SQL。
直接调用Python检索函数不是MCP集成证据。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
