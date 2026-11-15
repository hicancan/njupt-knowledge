---
title: 统一资源定位符（URL）的结构解析与本地文件URL构建规则
requires: [Web开发技术/www-concept]
---

# 统一资源定位符（URL）的结构解析与本地文件URL构建规则

## URL 的结构解析

URL（Uniform Resource Locator，统一资源定位符）用于标识互联网上的文档或资源；不同资源由不同 URL 区分。HTTP 请求行中的 `HTTP_method URL HTTP_version` 也依赖它说明“请求哪个资源”。

一般可写为：

$$
\text{scheme://object-address:port/path-to-document}
$$

其中 **scheme** 表示协议，**object-address** 表示对象地址或主机名，**port** 是服务端口号，**path-to-document** 是资源路径。主机名若包含各级域名直至根域，可称为 **FQDN（完全限定域名）**；考试按课件表格填写时，`FOOD.COM` 通常即作为该主机的 FQDN。

以 `HTTP://FOOD.COM:8080/RECIPES/BROCCOLI/` 为例：

| 组成部分 | 内容 |
|---|---|
| scheme（协议） | `HTTP` |
| object-address（对象地址/主机名） | `FOOD.COM` |
| port number（端口号） | `8080` |
| FQDN（完全限定域名） | `FOOD.COM` |
| path-to-document（文档路径） | `/RECIPES/BROCCOLI/` |

```mermaid
flowchart LR
    A["scheme：HTTP"] --> B["主机：FOOD.COM"]
    B --> C["端口：8080"]
    C --> D["路径：RECIPES/BROCCOLI/"]
```

> [!IMPORTANT]
> ==先按 `://` 找协议，再按第一个 `:` 找端口，最后按主机后的 `/` 找路径。== 协议名和主机名通常不区分大小写，但路径是否区分大小写取决于服务器及其文件系统，不应随意改大小写。

## 本地文件 URL 的构建

本地文件可使用课件给出的形式：

```text
FILE://PATH-TO-DOCUMENT
```

例如，本地文件路径为 `D:\web\chapter1\index.html`，可写成：

```text
file:///D:/web/chapter1/index.html
```

这里 `file` 是协议，三个 `/` 中前两个属于 `://`，第三个表示本地路径的起点；Windows 路径中的反斜杠 `\` 应改为 `/`。若文件位于 `/home/student/web/index.html`，则对应：

```text
file:///home/student/web/index.html
```

> [!WARNING]
> `FILE://PATH-TO-DOCUMENT` 是格式示意，不能原样保留 `PATH-TO-DOCUMENT`，也不要把 Windows 路径直接写成 `file://D:\web\index.html`。本地文件 URL 只描述本机位置，通常不能让别人通过互联网访问该文件。

## URL 字符与路径规则

URL **不能包含任意字符**。空格以及分号、冒号、和号等特殊字符不能随意直接出现，需要时须进行特殊编码，常见形式是百分号编码，如空格编码为 `%20`。因此，手工拼接 URL 时不能简单地在路径中插入空格。

判断 URL 指向目录还是文件，可先看路径末尾：==以 `/` 结尾通常表示目录，否则通常表示文件==。例如 `/RECIPES/BROCCOLI/` 指向目录，而 `/RECIPES/BROCCOLI.HTML` 指向文件。不过，服务器配置也可能改变实际映射，不能仅凭扩展名机械判断。

URL 路径也**不必从服务器文档根路径的物理位置开始写**。它通常从 Web 服务器对外公布的 URL 根路径 `/` 开始，再由服务器映射到文档根目录；例如 URL 中的 `/RECIPES/A.HTML` 不等于客户端磁盘上的绝对路径，也不意味着必须写出服务器上的 `C:\...` 或 `/var/www/...`。

| 问题 | 结论 |
|---|---|
| 任意字符都能出现在 URL 中吗？ | 不能，空格及部分特殊字符须编码 |
| 如何判断目录或文件？ | 通常看末尾是否有 `/`，并注意服务器配置 |
| 路径必须写出服务器文档根的物理路径吗？ | 不需要，写的是对外的 URL 路径 |

> [!TIP]
> 解题口诀：**协议看 `://`，端口看冒号，路径看斜杠；目录常带尾斜杠，特殊字符先编码。**
