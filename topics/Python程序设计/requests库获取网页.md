---
title: 使用requests库获取网页源代码
requires: [Python程序设计/网络爬虫基本原理]
---

# 使用requests库获取网页源代码

---
title: 使用requests库获取网页源代码
requires: [Python程序设计/模块与包, Python程序设计/字符串]
---

如果让你用 Python 把某个网页上的文字“搬”下来，你会怎么做？手动复制粘贴显然无法批量处理。网络爬虫的第一步，就是==让程序像浏览器一样向服务器发送请求，并拿到返回的网页源代码（HTML）==。`requests` 库正是为此而生的第三方库。

## 它是什么与为什么需要

`requests` 是 Python 中用于发送 HTTP 请求的第三方库。网页本质上是一段 HTML 格式的文本，浏览器收到这段文本后将其渲染成我们看到的页面。爬虫要提取数据，必须先拿到这段原始文本。

> [!IMPORTANT]
> `requests.get(url)` 会向指定 URL 发送 HTTP GET 请求，返回一个 `Response` 对象，其 `.text` 属性即为网页源代码字符串。

相比 Python 内置的 `urllib` 库，`requests` 的 API 设计更人性化，几行代码即可完成请求、解码和读取，是实际开发和课程实验中的首选。

## 交互流程

一次完整的网页获取过程，本质上是客户端与服务端的 HTTP 交互：

```mermaid
sequenceDiagram
    participant P as Python脚本
    participant S as Web服务器
    P->>S: "GET / HTTP"
    Note over S: 查找资源
    S-->>P: "200 OK + HTML"
    Note over P: 存入.text
```

## 怎么做

使用前需确保已安装该库（终端执行 `pip install requests`）。核心步骤只有三步：导入库、发请求、取源码。

```python
import requests

url = "https://www.njupt.edu.cn"
response = requests.get(url)      # 发送 GET 请求，获得 Response 对象
html = response.text              # 提取网页源代码（字符串类型）

print(html[:100])                 # 打印前100个字符预览
```

> [!TIP]
> 记忆口诀：“一导二 get 三 text”。`response` 对象除了 `.text`，还有 `.status_code`（状态码，如 $200$ 表示成功）、`.encoding`（编码方式）等常用属性。

## 相近概念对比

初学者常将 `requests` 与其他获取网页的方式混淆，它们的区别如下：

| 方案 | 性质 | 特点 | 适用场景 |
| :--- | :--- | :--- | :--- |
| `requests` | 第三方库 | API 简洁，自动处理很多底层细节 | ==静态网页源码获取== |
| `urllib` | 标准库 | 无需安装，但写法繁琐 | 不允许装第三方库时 |
| `Selenium` | 第三方库 | 驱动真实浏览器，能执行 JS | 动态渲染网页 |

> [!NOTE]
> `requests.get()` 只能获取服务器直接返回的 HTML 源码。如果网页内容是靠 JavaScript 动态加载出来的（如部分瀑布流页面），`.text` 里拿不到这些数据，此时才需要用到 `Selenium` 等工具。

## 常见的坑

> [!WARNING]
> **中文乱码**：`requests` 默认根据 HTTP 响应头猜测编码，但经常猜错（比如把 UTF-8 猜成 ISO-8859-1），导致 `response.text` 出现乱码。解决办法是手动指定：`response.encoding = 'utf-8'`，或者直接使用 `response.content.decode('utf-8')`。

> [!CAUTION]
> **反爬拦截**：很多网站会检查请求头。如果不加 `headers`，默认的 User-Agent 是 `python-requests/x.x.x`，极易被服务器识别为爬虫并返回 $403$ 错误。务必伪装成正常浏览器：

```python
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(url, headers=headers)
```

## 完整示例

下面是一个包含异常处理的规范写法，能够稳定获取南京邮电大学官网的源码并验证是否成功：

```python
import requests

url = "https://www.njupt.edu.cn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()   # 若状态码不是 200，抛出异常
    response.encoding = response.apparent_encoding  # 智能推断正确编码
    html = response.text
    print(f"获取成功，源码长度：{len(html)}")
except requests.RequestException as e:
    print(f"请求失败：{e}")
```

> [!IMPORTANT]
> 写爬虫时务必加上 `try...except` 捕获网络异常，并用 `timeout` 设置超时时间，否则一旦目标网站无响应，你的程序就会一直卡死挂起。
