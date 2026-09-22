# D12 补课：本地向量库

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Qdrant官方客户端README的Local mode、create_collection、upsert、query_points：https://github.com/qdrant/qdrant-client

## 今日只学以下内容
### 1. 先3维玩具数据
使用内存collection、Cosine距离。点1=[1,0,0]、点2=[0,1,0]、点3=[.9,.1,0]。
查询[1,0,0]应返回1、3优先。先通过这条机械测试再接512维真实模型。
### 2. 正式索引
path使用日卡给出的workspace/qdrant；一次只开一个客户端进程，退出close。
collection维数从实际embedding_config读取，不把3维和512维混存。
Qdrant点ID使用整数或合法UUID；逻辑chunk_id保存在payload中。
同一个逻辑片段稳定生成同一个UUID，upsert后总量不应增加。
### 3. payload
chunk_id/source/revision/start_line/end_line/text。检索结果必须能回到原文。
更换语料版本或Embedding后重建当前小索引，不混用旧向量。
### 4. 数据文件
库内部会创建多个文件；你只指定顶层目录，不自行新建/编辑内部数据库文件。
本地开发测试不证明多worker或生产高并发。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
