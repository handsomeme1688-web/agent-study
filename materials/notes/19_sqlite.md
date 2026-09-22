# D19 补课：连接、参数与事务

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Python sqlite3 Tutorial、placeholders和transaction control：https://docs.python.org/3.12/library/sqlite3.html

## 今日只学以下内容
### 1. 两张表
sessions: id文本主键、owner_id、created_at。
messages: id整数主键、session_id、role、content、created_at；session_id关联sessions。
### 2. 参数化
SQL写VALUES (?, ?, ?)，值通过execute(sql, params)传入；不使用字符串拼接SQL。
插入it's fine后必须读到原样文本。
### 3. 事务
本课程把一次成功问答的user与assistant消息当作一个提交单元。
在同一连接中写两条，第二条失败必须回滚第一条。不能用两次各自提交的append_message冒充原子性。
### 4. 连接
每次操作在当前线程创建并关闭连接。用临时文件做重开测试，不拿个人会话当测试数据。
本轮不接ORM，不把小表查询速度称为生产性能。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
