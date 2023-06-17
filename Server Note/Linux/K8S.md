### 概念
#### 时光回溯
+ 传统部署：在物理服务器上运行应用程序
+ 虚拟化部署：在单个服务器上运行多台虚拟机，虚拟化可以使应用程序在不同的VM之间彼隔离，且能提供一定程度的安全性
+ 容器部署时代：容器之间可以共享OS，每个容器都具有自己的文件系统、CPU、内存和进程空间，与系统基础架构分离
#### K8S能做什么
 K8S提供一个可弹性运行分布式系统的框架
**服务发现和负载均衡**：可以使用DNS名称或自己的IP地址来暴露容器，进入容器的流量很大，K8S可以负载均衡分配网络流量
**存储编排**：K8S允许自动挂载选择的存储系统
**自动部署和回滚**，**自动完成装箱计算**，**自我修复**，**密钥与配置管理**
#### K8S对象
在 Kubernetes 系统中，**Kubernetes 对象**是持久化的实体
操作 Kubernetes 对象 需要使用 [Kubernetes API](https://kubernetes.io/zh-cn/docs/concepts/overview/kubernetes-api)。 比如，当使用 `kubectl` 命令行接口（CLI）时，CLI 会调用必要的 Kubernetes API； 也可以在程序中使用[客户端库](https://kubernetes.io/zh-cn/docs/reference/using-api/client-libraries/)， 来直接调用 Kubernetes API。
几乎每个 Kubernetes 对象包含两个嵌套的对象字段，它们负责管理对象的配置： 对象 **`spec`（规约）** 和对象 **`status`（状态）**。
**大多数情况下，你需要提供 `.yaml` 文件为 kubectl 提供这些信息**。 `kubectl` 在发起 API 请求时，将这些信息转换成 JSON 格式。
在想要创建的 Kubernetes 对象所对应的 `.yaml` 文件中，需要配置的字段如下：
- `apiVersion` - 创建该对象所使用的 Kubernetes API 的版本
- `kind` - 想要创建的对象的类别
- `metadata` - 帮助唯一标识对象的一些数据，包括一个 `name` 字符串、`UID` 和可选的 `namespace`
- `spec` - 你所期望的该对象的状态