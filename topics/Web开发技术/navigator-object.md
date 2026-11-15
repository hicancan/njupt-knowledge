---
title: navigator对象的使用
requires: [Web开发技术/js-built-in-objects]
---

# navigator对象的使用

## navigator 对象

> [!IMPORTANT]
> `navigator` 对象是浏览器提供的全局对象，==代表浏览器本身的状态与身份信息==，常用于判断用户使用的浏览器类型、版本、操作系统以及是否支持特定功能。

### 为什么需要 navigator

当你打开一个网页时，服务器其实不知道你用的是 Chrome 还是 Edge，是 Windows 还是 macOS，是桌面端还是手机端。这些信息对以下场景至关重要：

- **兼容性适配**：不同浏览器对 API 的支持程度不同，需要针对性地加载 polyfill 或提示升级
- **统计分析**：收集用户设备与浏览器分布，指导产品迭代
- **功能检测**：判断浏览器是否支持摄像头、地理位置、离线存储等能力

### 它能做什么

navigator 提供了几个最常用的属性：

| 属性 | 返回值示例 | 含义 |
|------|-----------|------|
| `navigator.userAgent` | `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ..."` | 浏览器发给服务器的完整身份字符串 |
| `navigator.appName` | `"Netscape"` | 浏览器名称（历史遗留，几乎所有浏览器都返回 Netscape） |
| `navigator.appVersion` | `"5.0 (Windows NT 10.0; Win64; x64) ..."` | 浏览器版本信息（也包含操作系统信息） |
| `navigator.platform` | `"Win32"` | 操作系统平台 |
| `navigator.onLine` | `true` / `false` | 浏览器是否联网 |
| `navigator.cookieEnabled` | `true` / `false` | 是否启用了 cookie |
| `navigator.language` | `"zh-CN"` | 浏览器首选语言 |

此外，`navigator` 还挂载了一系列现代 API 入口，如 `navigator.geolocation`（地理位置）、`navigator.mediaDevices`（摄像头麦克风）、`navigator.clipboard`（剪贴板）等。

### 怎么用：一个实用的浏览器/系统判断

下面这段代码从 `userAgent` 中解析出核心信息：

```javascript
function getBrowserInfo() {
    var ua = navigator.userAgent;
    var info = {};

    // 判断操作系统
    if (ua.indexOf("Windows NT 10.0") !== -1) {
        info.os = "Windows 10";
    } else if (ua.indexOf("Mac OS X") !== -1) {
        info.os = "macOS";
    } else if (ua.indexOf("Linux") !== -1) {
        info.os = "Linux";
    } else {
        info.os = "未知系统";
    }

    // 判断浏览器（注意顺序：Chrome 的 UA 也包含 Safari）
    if (ua.indexOf("Edg/") !== -1) {
        info.browser = "Edge";
    } else if (ua.indexOf("Chrome/") !== -1) {
        info.browser = "Chrome";
    } else if (ua.indexOf("Safari/") !== -1) {
        info.browser = "Safari";
    } else if (ua.indexOf("Firefox/") !== -1) {
        info.browser = "Firefox";
    } else {
        info.browser = "其他浏览器";
    }

    return info;
}

var myBrowser = getBrowserInfo();
console.log("系统: " + myBrowser.os + ", 浏览器: " + myBrowser.browser);
```

### 和相近概念的区别

> [!NOTE]
> **navigator × screen × location × history**
> - `navigator`：浏览器本身的属性（谁在访问）
> - `screen`：用户显示器的物理属性（分辨率、色深）
> - `location`：当前页面的 URL（地址栏里是什么）
> - `history`：浏览历史记录（从哪来、往哪去）

它们都是 `window` 对象的属性，但各自关心的维度完全不同。

### 常见的坑

> [!WARNING]
> **1. `userAgent` 可以伪造**
> 很多浏览器插件或爬虫都会修改 UA 字符串，==永远不要用 `userAgent` 做安全校验==（比如判断是否是真人用户）。

> [!WARNING]
> **2. 属性名大小写敏感**
> 是 `navigator.userAgent`，不是 `navigator.UserAgent`。JavaScript 中驼峰命名才是正确写法。

> [!WARNING]
> **3. 不要用 `appName` 和 `appVersion` 做判断**
> `navigator.appName` 在所有现代浏览器中都返回 `"Netscape"`，这是历史兼容性留下的残留，完全没有区分价值。判断浏览器请解析 `userAgent`。

> [!CAUTION]
> **4. `userAgent` 检测顺序不能随便改**
> Chrome、Edge、Safari 的 UA 字符串都包含 `"Safari"`，Chrome 和 Edge 都包含 `"Chrome"`。如果把 Safari 的判断写在 Chrome 前面，Chrome 会被误判成 Safari。==正确的检测顺序是：Edge → Chrome → Safari==。

### 算对了的例子

题目：请在打开的浏览器控制台中，编写 JavaScript 代码，获取并打印浏览器的以下信息：
1. 浏览器是否联网
2. 浏览器是否启用了 Cookie
3. 浏览器的首选语言

参考答案：

```javascript
console.log("是否联网: " + navigator.onLine);
console.log("是否启用Cookie: " + navigator.cookieEnabled);
console.log("首选语言: " + navigator.language);
```

执行结果示例（Chrome 中文版、Windows、联网状态）：

```
是否联网: true
是否启用Cookie: true
首选语言: zh-CN
