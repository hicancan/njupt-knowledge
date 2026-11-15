---
title: 《Web技术（双语）》实验指导书
kind: 实验
course: Web技术（双语）
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/Web%E6%8A%80%E6%9C%AF%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf
---

# 《Web技术（双语）》实验指导书

原件经识别和整理；“参考解答”是我们补的。

## 第一章 Linux 下 LAMP 安装和配置

实验平台以 Ubuntu(一个开源 linux)为开发环境。本章主要说明如何在 Ubuntu 下配置 PHP 开发环境 LAMP。所谓 LAMP 指 Linux，Apache，Mysql，PHP。

### 一 安装过程

第一步：安装 Apache2：

```bash
sudo apt-get install apache2
```

第二步：安装 PHP 模块：

```bash
sudo apt-get install php5
```

第三步：安装 Mysql

```bash
sudo apt-get install mysql-server
```

第四步：其他模块安装：

```bash
sudo apt-get install libapache2-mod-php5
sudo apt-get install libapache2-mod-auth-mysql
sudo apt-get install php5-mysql
sudo apt-get install php5-gd
```

前两个很容易明白，要想 apache 能够解析 PHP，就需要借助这两个模块来找到 phpengine。第三个在 php 操作 mysql 数据库时用到，第四个 GD 库。

### 二 配置过程

基本上多有的配置都在 `/etc/apache2` 目录及其子目录下完成，故一定要搞清楚这个目录结构。

#### 第一步：apache根目录

安装完 apache2，根目录在 `/var/www` 下，可以通过 `http://localhost/` 测试一下是否好用。

当然也可以在该目录下新建一个文件 `test.html` 来试一试 `http://localhost/test.html`。

#### 第二步：PHP 解析问题

安装完，php 的解析有点问题，浏览 php 网页会保存，apache 没有将其解析为网页。Ubuntu 的 apache2 配置在 `/etc/apache2` 目录下。这个目录下有个 `apache2.conf` 文件，这个文件通过包含其他配置文件涵盖了所有的 apache2 系统配置信息。

php 解析部分在的配置在 `/etc/apache2/mods-available` 下的 `php5.conf` 和 `php5.load` 中，`apache2.conf` 文件中并没有将这两个文件包含进来，只要包含进去就可以。

在 `apache2.conf` 中找到

```text
#Include module configuration:
Include /etc/apache2/mods-enabled/*.load
Include /etc/apache2/mods-enabled/*.conf
```

在其后面添加

```text
Include /etc/apache2/mods-available/php5.load
Include /etc/apache2/mods-available/php5.conf
```

另外一种方法就是将这两个文件链接到 `mods-enabled` 目录下：

```bash
sudo ln -s /etc/apache2/mods-available/php5.load /etc/apache2/mods-enabled/php5.load
sudo ln -s /etc/apache2/mods-available/php5.conf /etc/apache2/mods-enabled/php5.conf
```

这一种方式更好一点，没有破坏 apache2 本身的配置结构。

#### 第三步 改变 apache2 的默认目录到当前的开发目录

apache2 的默认目录配置在 `/etc/apache2/sites-enabled/00default` 文件中。

找到该文件中的 `DocumentRoot` 项，将 `/var/www` 改为你的开发目录就 OK 了。

当然，还有一种方法就是不该边默认目录，只是在 `var/www` 下建立一个到你的目录的链接。

比如你的目录在 `/home/username/phptest`，那么你只要

```bash
sudo ln -s /home/username/phptest /var/www/phptest
```

这样你就可以通过 `http://localhost/phptest` 访问你的工作目录了。

[注意]链接文件名中不能含有“.”，否则 apache2 会将其当作为一个文件试图解析而无法达到链接目录的效果。

个人推荐用后一种方式，这样可以多个工作目录并行开发。

### 三 配置中常用命令

重启 apache

```bash
sudo /etc/init.d/apache2 restart
```

建立系统链接

```bash
sudo ln -s a b
```

## 第二章 Windows 下 WAMP 的安装和配置

本实验以 Windows 为开发环境。WAMP 就是 Windows、 Apache、 Mysql 和 PHP 集成安装环境。大家到 http://www.wampserver.com/ 下载相应的安装包后按照提示进行安装。

### 一 常见问题

安装 WAMP 后，如果 80 端口没有被占用，而且 WAMP 图标呈现黄色(服务没有完全启动)，那么看看你安装或使用的时候，有没有提示过 MSVCR100.dll 丢失的情况，如果有：

解决方案 1：在网上单独下载 msvcr100.dll 文件包后安装。

解决方案 2：安装 VC 的运行库。

### 二 使用方法

1、正常安装后，在桌面上会有一个 WampServer 的粉红色图标，双击后在有下脚托盘呈现一个绿色图标。

2、将绿色图标双击，会出现服务器的管理界面。我们可以清晰的看到第一个 Localhost 便是运行 `http://localhost/`，第二个 phpMyAdmin 是打开数据库，默认是不需要输入密码的直接就可以打开。而且默认的数据库用户名是 root，这个需要大家知道。然后第三个 www 目录便是你需要放置 php 程序文件的地方，安装好 wamp5 后默认里面会有一些文件存在，这些文件都可以将它删掉。

3、将自己编写的 test.html 或者 test.php 文件放到 www 指定的目录下后，在浏览器中输入 `http://localhost/test.html` 或者 `http://localhost/test.php`，即可以显示文件或者调用服务器脚本。

## 第三章 实验 1 客户端 HTML 脚本编写

### 一 实验目的

（1） 通过上机实践，熟悉 HTML 和 JavaScript 脚本实现技术。

（2） 加深对 Web 编程的认识。

### 二 相关章节

Introduction to XHTML

The Basics of JavaScript

JavaScript and HTML Documents

### 三 实验内容及要求

1 编写个人主页，要求包含如下信息。

（1） 标题“欢迎访问×××的主页”

（2） 个人简介，包含照片。

（3） 个人经历简介，以有序列表形式显示。

（4） 个人最喜欢的 4 本书，以无序列表显示。

（5） 个人兴趣简介，以段落文字方式显示，或者以列表显示。

（6） 列出 6 门主干课程成绩，以表格形式显示。如下示例

表 3.1：成绩显示格式

| 课程名 | 开课学期 | 任课教师 | 分数 |
| :--- | :--- | :--- | :--- |
| 高等数学 | 2012 秋季 | 张三 | 90 |
| 离散数学 | 2012 春季 | 李四 | 80 |

（7） 个人的朋友主页链接或者学校主页链接。

（8） 其它个人想表达的信息。

备注：（1）代码要求手工输入，不要用工具自动生成，本题目让大家了解 HTML文档的基本元素构成。（2）界面的字体、颜色、样式有大家自己决定。（3）通过多个页面相互链接来访问。

2 HTML 文件中嵌入 javascript 脚本实现输入 a，b，c 三个系数，计算方程的两个根并在页面上显示。

### 四 实验环境

硬件：微机

软件：window XP 或者 Ubuntu，浏览器 IE 或者 Firefox，编辑器 Editplus 或者记事本

### 五 实验指导

1、将 HTML 文档 xxx.html 直接放到 wamp 下的 www 目录下，通过在浏览器中输入 `http://localhost/xxx.html` 下即可以。

2、浏览器会提示“此网站使用脚本窗口向您索取信息。如果您信任….”，解决办法：Internet选项->安全->internet->自定义级别->脚本->允许网站用脚本窗口提示获得信息。选择启用

3、具体代码参见教材。

### 六 实验报告要求

实验报告的内容包括：

(1)实验名称

(2)实验目的

(3)实验内容

(4)实验环境

(5)实验过程，列出主要的 SQL 语句

(6)实验结果、分析与体会：包括实验结果分析，实验过程中所遇到的问题和解决的办法，解决问题的过程中得到的经验和体会。

## 第四章 实验 2 Web服务端脚本编写

### 一 实验目的

（1） 通过上机实践，熟悉 Apache服务器的安装和配置使用方法。

（2） 掌握 PHP 脚本语言，熟练运用 PHP 语言进行服务器端编程。

### 二 相关章节

Introduction to PHP

### 三 实验内容及要求

1 显示一个图书售卖界面，主要包括一下内容

（1）HTML 的标题为“Welcome to book seller”。

（2）页面内容第一行黑体显示“You are welcome”。

（3）标签提示“please input your name”，并创建输入框。

（4）标签提示“please input your address”，并创建输入框。

（5）标签提示“please input your zip”，并创建输入框。

（6）黑体显示“please fill in the quantity field of the following form”。

（7）表格分成四列，分别是“book”，“publisher”，“price”，“quantity”，其中包含的信息如表格所示

表 4.1 图书样表

| book | publisher | price | quantity |
| :--- | :--- | :--- | :--- |
| Web technology | Springer press | $5.0 | |
| mathematics | ACM press | $6.2 | |
| principle of OS | Science press | $10 | |
| Theory of matrix | High education press | $7.8 | |

（8）quantity 采用输入框输入。

（9）显示“payment method”

（10）用单选按钮显示四个支付方式选项“cash”，“cheque”，“credit card”。

（11）显示两个标准按钮，“submit”按钮和“reset”按钮。

2 当用户输入完各个内容并按下“submit”按钮后，通过脚本生成新的 HTML 页面。其中包含以下内容

（1）customer name

（2）customer address

（3）customer zip

（4）以表格形式显示订购图书信息，包含四列“book”，“publisher”，“price”，“total cost”，其中 total cost 通过脚本动态计算生成。未购买的图书不显示。

# Web 技术（双语）实验指导书

本资料整理自《Web 技术（双语）》实验指导书第 2 部分（第 10–21 页），主要包含实验环境、实验内容指导、MySQL 数据库操作详解及实验大纲要求。

## 第五章 实验 3 Web 数据库访问

### 一、实验目的

- 通过上机实践，熟悉用 PHP 语言访问 MySQL 数据库服务器的方法。
- 掌握 PHP 脚本语言，能熟练运用 PHP 语言进行服务器端编程。

### 二、相关章节

Database Access through the Web

### 三、实验内容及要求

#### 1. 显示一个图书售卖界面

承接上个实验，主要包括以下内容：

- HTML 的标题为“Welcome to book seller”。
- 页面内容第一行黑体显示"You are welcome"。
- 标签提示"please input your name"，并创建输入框。
- 标签提示"please input your address"，并创建输入框。
- 标签提示"please input your zip"，并创建输入框。
- 黑体显示"please fill in the quantity field of the following form"。
- 表格分成四列，分别是"book"，"publisher"，"price"，"quantity"，其中包含的信息如表 5.1 所示。

**表 5.1 图书样表**

| book | publisher | price | quantity |
| :--- | :--- | :--- | :--- |
| Web technology | Springer press | $5.0 | |
| mathematics | ACM press | $6.2 | |
| principle of OS | Science press | $10 | |
| Theory of matrix | High education press | $7.8 | |

- quantity 采用输入框输入。
- 显示"payment method"。
- 用单选按钮显示四个支付方式选项："cash"，"cheque"，"credit card"。（注：原文列举了三个，通常应为四个，此处按原文保留）。
- 显示两个标准按钮，"submit"按钮和"reset"按钮。

#### 2. 提交表单后的数据处理

在按下 submit 按钮后，完成 3 张数据库表的插入或者更改：

- name、address、zip 存到数据库的一个表中。
- 图书信息包括 book、publisher、price 存成一张表。
- 订单信息存成一个表，包括 name、book、quantity。

#### 3. 显示一个订单查询界面

主要包括以下内容：

- 标签提示"please input customer name"，并创建输入框。
- 显示"submit"按钮，点击后，从数据库中查询 name、book、publisher、quantity 并在 HTML 界面显示查询结果（感兴趣的同学也可以将每个客户的总金额计算并显示出来）。

### 四、实验环境

- **硬件**：微机
- **软件**：Apache, PHP 模块
- **编辑器**：vim 或者 gedit

### 五、实验指导

#### 1. 编写 main.html

主要包括以下内容：

- 采用 HTML 的 head 表示。
- 采用 `<h1>` 标签。
- 采用 `<tr></tr>` 中嵌套 `<td></td>`，`<td></td>` 中嵌套 `input` 标签实现。
- 表格采用 `table` 标签实现。
- 输入框采用 `input`。
- 用 `<input type="radio">` 实现单选按钮。
- 用 `<input type="submit">` 和 `<input type="reset">` 实现按钮。

#### 2. 编写 main.php

采用以下技术步骤：

- 用户的输入值采用 PHP 脚本的 `$_POST` 函数获取。
- 数量通过 `$_POST` 函数获取，动态计算生成。
- print 或者 printf 显示。
- 计算并显示"××has bought××books"（××分别指代客户名字和购买书的数量）。
- 计算并显示"××paid××"（这里××指代客户名字和总金额数）。
- 根据用户的选择显示"paid by××"（这里×指代用户选择的支付方式）。
- 将用户购买信息存入到文件中，每个客户包含三行信息，即上述三句话。
- 如果用户按的是"重置"按钮，则清除所有的输入信息。

#### 3. 文件写入注意事项

采用 `fopen`, `fwrite` 实现，注意换行的实现：

- 如果是 Windows 平台，字符串末尾加"\r\n"；
- 如果是 Linux 平台，字符串末尾加"\n"。

#### 4. 回显界面

直接回显一个与原来相同的界面。

#### 5. MySQL 中的数据库和表的创建

##### 5.1 MySQL 数据类型和表的创建

下面是可使用的各种 MySQL 数据类型：

| 类型分类 | 描述 |
| :--- | :--- |
| **数值类型** | |
| int(size), smallint(size), tinyint(size), mediumint(size), bigint(size) | 仅支持整数。在 size 参数中规定数字的最大值。 |
| decimal(size,d), double(size,d), float(size,d) | 支持带有小数的数字。在 size 参数中规定数字的最大值。在 d 参数中规定小数点右侧的数字的最大值。 |
| **文本数据类型** | |
| char(size) | 支持固定长度的字符串。(可包含字母、数字以及特殊符号)。在 size 参数中规定固定长度。 |
| varchar(size) | 支持可变长度的字符串。(可包含字母、数字以及特殊符号)。在 size 参数中规定最大长度。 |
| tinytext | 支持可变长度的字符串，最大长度是 255 个字符。 |
| text/blob | 支持可变长度的字符串，最大长度是 65535 个字符。 |
| mediumtext/mediumblob | 支持可变长度的字符串，最大长度是 16777215 个字符。 |
| longtext/longblob | 支持可变长度的字符串，最大长度是 4294967295 个字符。 |
| **日期数据类型** | |
| date (yyyy-mm-dd)<br>datetime (yyyy-mm-dd hh:mm:ss)<br>timestamp (yyyymmddhhmmss)<br>time (hh:mm:ss) | 支持日期或时间 |
| **杂项数据类型** | |
| enum(value1,value2,ect) | ENUM 是 ENUMERATED 列表的缩写。可以在括号中存放最多 65535 个值。 |
| set | SET 与 ENUM 相似。但是，SET 可拥有最多 64 个列表项目，并可存放不止一个 choice。 |

##### 5.2 主键和自动递增字段

每个表都应有一个主键字段。主键用于对表中的行进行唯一标识。每个主键值在表中必须是唯一的。此外，主键字段不能为空，这是由于数据库引擎需要一个值来对记录进行定位。

主键字段永远要被编入索引。这条规则没有例外。你必须对主键字段进行索引，这样数据库引擎才能快速定位给予该键值的行。

下面的例子把 personID 字段设置为主键字段。主键字段通常是 ID 号，且通常使用 `AUTO_INCREMENT` 设置。`AUTO_INCREMENT` 会在新记录被添加时逐一增加该字段的值。要确保主键字段不为空，我们必须向该字段添加 `NOT NULL` 设置。

#### 6. 把来自表单的数据插入数据库

现在，我们创建一个 HTML 表单，这个表单可把新记录插入到"Persons" 表。

当用户点击上例中 HTML 表单中的提交按钮时，表单数据被发送到 "insert.php"。"insert.php" 文件连接数据库，并通过 `$_POST` 变量从表单取回值。然后，`mysql_query()` 函数执行 INSERT INTO 语句，一条新的记录会添加到数据库表中。

#### 7. 从数据库表中选取数据

SELECT 语句用于从数据库中选取数据。

**语法**

注释：SQL 语句对大小写不敏感。SELECT 与 select 等效。

为了让 PHP 执行上面的语句，我们必须使用 `mysql_query()` 函数。该函数用于向 MySQL 发送查询或命令。

下面的例子选取存储在 "Persons" 表中的所有数据（* 字符选取表中所有数据）。

#### 8. 在 HTML 表格中显示结果

下面的例子选取的数据与上面的例子相同，但是将把数据显示在一个 HTML 表格中。

#### 9. 往 mysql 中插入中文乱码的问题解决办法

在 `mysql_query` 前加入下列三句话：

```php
mysql_query("set names utf8");
mysql_query("set character set utf8");
mysql_query("set character_set_results=utf8");
```

### 六、实验报告要求

实验报告的内容包括：

1. 实验名称
2. 实验目的
3. 实验内容
4. 实验环境
5. 实验过程，列出主要的 SQL 语句
6. 实验结果、分析与体会：包括实验结果分析，实验过程中所遇到的问题和解决的办法，解决问题的过程中得到的经验和体会。

## 实验大纲

- **课程编号**：B0301231C
- **实验课程名称**：Web 技术 (双语)
- **实验项目名称**：
    1. 客户端脚本编写
    2. Web 服务端脚本编写
    3. Web 数据库访问
- **实验类型**：验证性实验
- **实验类别**：专业■（基础□ 专业基础□ 专业■）
- **实验学时**：8
- **所涉及的课程及知识点**：本实验设计涉及课程《Web 技术（双语）》。涉及知识点：Java Web 应用的技术环境和开发工具，主要包括 JavaScript, PHP 和 MySql 访问。

### 一、实验目的

在本课程的实验中，通过设置三个密切相关的实验，让学生掌握，使学生进一步理解和掌握 Web 应用开发中的客户端编程、服务器端编程和在数据库访问技术。

### 二、实验内容

该实验内容主要包括：
1. 客户端脚本编写。让学生掌握如何利用 javascript 实现客户端编程。
2. Web 服务端脚本编写。以 PHP 为语言，掌握服务端编程技术。
3. Web 数据库访问。以 MySQL 为例子，让学生掌握在 web 编程中对数据库的访问技术。

### 三、实验仪器设备和材料清单

- **硬件**：微型计算机，计算机局域网络。
- **软件**：Win XP、Linux（ubuntu）、IE 或者 firefox 浏览器、Apache Web 服务器、MySQL。

### 四、实验要求

1. 掌握 JavaScript。
2. 掌握 PHP 技术。
3. 掌握 MySQL 使用技术。

### 五、实验报告要求

实验报告的内容：

1. 实验名称和目的。
2. 实验内容和环境（硬件、软件平台及调试工具）。
3. 实验步骤和现象。
4. 实验结果和分析。

**实验报告的要求**：实验报告以文本形式递交。实验报告要书写规范、文字简练、语句通顺、图表清晰。
