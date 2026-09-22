# D26 补课：容器的路径不同于宿主

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Dockerfile官方概念：https://docs.docker.com/build/concepts/dockerfile/
- bind mounts：https://docs.docker.com/engine/storage/bind-mounts/

## 今日只学以下内容
### 1. 路径映射
宿主项目：~/agent-study/repo-qa-agent。
镜像工作目录：/app；容器数据目录：/app/workspace。
宿主workspace/container-data挂载到/app/workspace；应用不能把宿主~/路径硬编码进镜像。
### 2. 最小构建思路
Python基础镜像→WORKDIR /app→COPY锁定依赖→pip install→COPY代码→启动一个worker。
不是完整答案；你必须填入实际锁定版本和可启动命令。
.env、.venv、workspace、Git目录排除；密钥只在运行时注入。
### 3. 先准备索引
镜像可包含公开data/chunks.jsonl；挂载目录初次为空时，应显式运行build_index准备Qdrant。
模型下载和缓存路径需要记录；无缓存/无网络的真实Embedding失败不能伪装成健康问答。
### 4. 重启验收
创建会话→停止容器→重新启动同名容器→同会话仍可读。
Docker不能安装可做干净venv复现，但容器栏保持未测。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
