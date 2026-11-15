---
title: 《软件工程（双语）》实验4参考资料：Subversion 安装与使用（课件）
kind: 课件
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验4参考资料/SVN安装及使用.pptx
---

# 《软件工程（双语）》实验4参考资料：Subversion 安装与使用（课件）

原件的每一页，下面附识别出的文字。

### SUBVERSION 安装与使用

![第 1 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第1页.webp)

原文：

SUBVERSION 安装与使用

### 单元目标

![第 2 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第2页.webp)

原文：

单元目标

了解版本控制系统

□ 理解版本控制系统的重要性与优点

Subversion 配置安装与使用

2

### 为何需要版本控制系统？

![第 3 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第3页.webp)

原文：

为何需要版本控制系统？

□ 帮助我记住我干了些什么

□ 帮助我记录谁动了我的奶酪，如何动的

□ 帮助我从错误中恢复

□ 帮助我获知与他人的冲突内容

□ 帮助我管理多个项目

3

### 简单工作原理

![第 4 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第4页.webp)

原文：

简单工作原理

客户端

在工作文件夹中处理文件把编辑好的文件
check in到服务端

从服务端的数据库中把文件check out到本地编辑

服务端

数据库建立在服务端

4

### 主流版本控制软件介绍

![第 5 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第5页.webp)

原文：

主流版本控制软件介绍

Subversion (SVN)

□ Starteam

ClearCase (CC)

☐ CVS (Concurrent Versions System)

Visual SourceSafe (VSS)

5

### 主流版本控制软件介绍

![第 6 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第6页.webp)

原文：

主流版本控制软件介绍

Subversion

是一种开放源码的全新版本控制系统，支持可在本地访问或通过网络访问的数据库和文件系统存储库。不但提供了常见的比较、修补、标记、提交、回复和分支功能性，Subversion 还增加了追踪移动和删除的能力。此外，它支持非ASCII 文本和二进制数据，所有这一切都使 Subversion 不仅对传统的编程任务非常有用，同时也适于 Web 开发、图书创作和其他在传统方式下未采纳版本控制功能的领域。

- Starteam

是一个集合了版本控制、构建管理（Build Management）和缺陷跟踪系统为一体的软件，并且具有强大的图形界面，易学易用；但管理复杂、维护困难。2002年底被Borland公司收购。

6

### 主流版本控制软件介绍

![第 7 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第7页.webp)

原文：

主流版本控制软件介绍

◆ Visual SourceSafe (VSS)

简单易用、方便高效、与Windows操作系统及微软开发工具高度集成。

◆ Concurrent Versions System ( CVS )

是开发源码的并发版本系统, 它是目前最流行的面向软件开发人员的源代码版本管理解决方案。它可用于各种平台，包括 Linux 、Unix和 Windows NT/2000/XP等等

ClearCase(CC)

是ROSE构件的一部分，目前最牛的配置管理工具，主要应用于复杂的产品发放、分布式团队合作、并行的开发和维护任务。可以控制Word、Excel、PowerPoint、Visio等文件格式，对于不认识的格式可以自己定义一种类型来标识。

7

### 在SVN中的几个重要概念

![第 8 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第8页.webp)

原文：

在SVN中的几个重要概念

Repository

□ 版本库

■ SVN核心，数据中心仓库

文件共享

■ 共享信息，避免干扰

□ 锁定-修改-解锁

\- 在同时间里间用户独占使用资源

\- 锁定可能导致管理问题

\- 锁定可能导致不必要的线性化开发

\- 锁定可能导致错误的安全状态

8

### 在SVN中的几个重要概念

![第 9 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第9页.webp)

原文：

在SVN中的几个重要概念

□ 拷贝-修改-合并

9

### SVN体验

![第 10 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第10页.webp)

原文：

SVN体验

10

### SVN配置安装与使用

![第 11 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第11页.webp)

原文：

SVN配置安装与使用
<table><tr><td rowspan="2">VisualSVN Server
Repositories
FirstExperience
SeconderyRepo
branches
tags
trunk
Users
Groups</td><td>branches (https://WIN-9P2ZTWIH2RA:8443/svn/SecondaryRepo/branches)</td></tr><tr><td>Name
There are no items to show in this view.</td></tr></table>

11

### 各项说明

![第 12 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第12页.webp)

原文：

各项说明

文件(F) 操作(A) 查看(V) 帮助(H)

VisualSVN Server

Repositories

Users

Groups

\- Repositories: 数据仓库管理

□ Users:用户管理

Groups:组管理

### Repositories说明

![第 13 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第13页.webp)

原文：

Repositories说明

VisualSVN Server

文件(F) 操作(A) 查看(V) 帮助(H)

Create New Repository...

Browse
Properties...

新建(N)
所有任务(K)

刷新(F)

点击Create

帮助(H)

Create New Repository

Repository Name: test

Repository URL: https://Cooltinywolf:8443/svn/test

□ Create default structure (trunk, branches, tags)

You can find recommendations on repository layout in the VisualSVN Help Center.

OK

Cancel

☐ 项目、文档保存在数据仓库中。在Repositories 中建立新的数据仓库，用来保存项目。保存路径是安装时选择的Repositories文件夹

### 创建数据仓库成功

![第 14 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第14页.webp)

原文：

创建数据仓库成功

VisualSVN Server

VisualSVN Server Repositories

Users

Groups

### 获取地址

![第 15 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第15页.webp)

原文：

获取地址

□ 将获得的地址共享，地址为

https://Cooltinywolf:8443/svn/test/

### VisualSVN Server Repositories

![第 16 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第16页.webp)

原文：

VisualSVN Server Repositories

Create User...

新建(N)

查看(V)

刷新(F)
导出列表(L)...

帮助(H)

点击Create

User name:

litianlei

Password:

\*\*\*\*\*\*\*\*\*\*

Confirm password:

\*\*\*\*\*\*\*\*\*\*

User name and password are case sensitive.

OK

Cancel

□ Users为对用户的管理，添加用户、删除用户、更改密码等操作在此进行

Users说明

VisualSVN Server

Create New User

×

### 用户创建成功

![第 17 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第17页.webp)

原文：

用户创建成功

VisualSVN Server

文件(F) 操作(A) 查看(V) 帮助(H)

VisualSVN Server

Repositories

Users

Groups

Users

Name

yantingguan

xiehantnig

litianlei

### VisualSVN Server

![第 18 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第18页.webp)

原文：

VisualSVN Server

点击Properties

Everyone

Add...

Remove

确定

取消

应用(A)

\- 在每个文件夹上点击右键，选择Properties就会出现权限管理界面，下面有对应的权限

权限管理

Properties for /svn/

? ×

### 点击Properties

![第 19 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第19页.webp)

原文：

点击Properties

□ 子文件夹会继承父文件夹的权限

Add...

Remove

确定

取消

应用(A)

权限管理

? ×

### 权限管理

![第 20 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第20页.webp)

原文：

权限管理

□ 可以将最顶层文件夹的Everyone权限取消在子文件夹上依次添加想要的权限

### SVN配置安装与使用

![第 21 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第21页.webp)

原文：

SVN配置安装与使用

21

21

### SVN配置安装与使用

![第 22 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第22页.webp)

原文：

SVN配置安装与使用

22

22

### SVN配置安装与使用

![第 23 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第23页.webp)

原文：

SVN配置安装与使用
<table><tr><td colspan="7">https://WIN-9P2ZTWIH2RA:8443/svn/SeconderyRepo - Repository Browser</td></tr><tr><td colspan="7">URL: https://WIN-9P2ZTWIH2RA:8443/svn/SeconderyRepo/trunk/SeconderyRepo Revision: HEAD</td></tr><tr><td rowspan="3">https://WIN-9P2ZTWIH2RA:8443/svn/Secondery branches
tags
trunk
SeconderyRepo
TopDir</td><td>File</td><td>Extension</td><td>Revision</td><td>Author</td><td>Size</td><td>Date</td></tr><tr><td>TopDir</td><td></td><td>2</td><td>test1</td><td></td><td>2009/3/5 16</td></tr><tr><td>TopTxt.txt</td><td>.txt</td><td>2</td><td>test1</td><td>0 bytes</td><td>2009/3/5 16</td></tr></table>

23

### SVN配置安装与使用

![第 24 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第24页.webp)

原文：

SVN配置安装与使用

□ 开始共享文件操作

24

### SVN配置安装与使用

![第 25 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第25页.webp)

原文：

SVN配置安装与使用

□ 给文件添加内容

25

### SVN配置安装与使用

![第 26 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第26页.webp)

原文：

SVN配置安装与使用

□ 回溯取得我的历史版本

26

### SVN配置安装与使用

![第 27 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第27页.webp)

原文：

SVN配置安装与使用

□ 撤消文档修改

27

### SVN配置安装与使用

![第 28 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第28页.webp)

原文：

SVN配置安装与使用

□ 删除共享目录文件

28

### SVN配置安装与使用

![第 29 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第29页.webp)

原文：

SVN配置安装与使用

□ 文档的冲突与合并

29

### SVN配置安装与使用

![第 30 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第30页.webp)

原文：

SVN配置安装与使用

□ 分支或标签

\- Branch: 从当前或历史版本库中演化出另一个功能或设计有较大变更的开发版本
- 从定制项目中演化生成一个可通用的产品化开发版本
- 从产品开发演化出面向不同应用对象的开发版本

\- Tag: 基于同一项目或产品稳定代码设置的识别标识

▪ 里程碑代码

\- 功能测试实现代码

▪ 版本升级代码

30

### SVN配置安装与使用

![第 31 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第31页.webp)

原文：

SVN配置安装与使用

□ 创建版本分支

31

### SVN配置安装与使用

![第 32 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第32页.webp)

原文：

SVN配置安装与使用

□ 创建版本版本标签

32

### SVN配置安装与使用

![第 33 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第33页.webp)

原文：

SVN配置安装与使用

定位我的本地拷贝

■ 场景：我们已经创建了一个分支，我们给现在的开发版本创建了一个标识，在Branch和Tags中各自维护了一个版本代码。

需求：如果我本地只想维护一个工作目录，该如何切换版本库呢？

33

### SVN配置安装与使用

![第 34 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第34页.webp)

原文：

SVN配置安装与使用

□ 使用Switch功能切换版本库

Switch To Branch / Tag

Switch:

D:\FirstRepo

To URL:

https://WIN-9P2ZTWIH2RA:8443/svn/FirstRepo/trunk

Revision

HEAD revision

Revision

Show log

OK

Cancel

Help

34

### SVN配置安装与使用

![第 35 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第35页.webp)

原文：

SVN配置安装与使用

回 回顾

■ 创建版本库

■ 共享项目目录和项目文件

■ 提取文件

■ 跟踪操作项目库中的文件和状态

■ 维护现有项目库结构

\- 分支，标签，合并及冲突处理

■ 版本切换

35

### 回滚到指定版本

![第 36 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第36页.webp)

原文：

回滚到指定版本

<table><tr><td>Action</td><td>Path</td><td>Copy from path</td><td>Revision</td></tr><tr><td>Modified</td><td>/</td><td></td><td></td></tr><tr><td>Added</td><td>/WindowsApplication11</td><td></td><td></td></tr><tr><td>Added</td><td>/WindowsApplication11/Form1.Designer.cs</td><td></td><td></td></tr><tr><td>Added</td><td>/WindowsApplication11/Form1.cs</td><td></td><td></td></tr><tr><td>Added</td><td>/WindowsApplication11/Program.cs</td><td></td><td></td></tr><tr><td>Added</td><td>/WindowsApplication11/Properties</td><td></td><td></td></tr></table>

### 用VC6.0开发，如果是第一次上传项目点击如下项

![第 37 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第37页.webp)

原文：

用VC6.0开发，如果是第一次上传项目点击如下项

test

打开(0)
资源管理器(X)
在这里打开命令行窗口
搜索(E)...

共享和安全(H)...

TortoiseSVN

添加到压缩文件(A)...
添加到 "test.rar"(T)
压缩并 E-mail...
压缩到 "test.rar" 并 E-mail

扫描病毒(S)

Expression Media Import

发送到(N)

剪切(T)
复制(C)

创建快捷方式(S)

删除①)

重命名(M)

属性(R)

Repo-browser

Export...

Create repository here

Import...

Settings
? Help
About

### Repository

![第 38 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第38页.webp)

原文：

Repository

URL of repository:

https://Cooltinywolf:8443/svn/vc/

Import message

Recent messages

□ Include ignored files

OK

Cancel

Help

通过指定的地址上传项目

- □ ×

### 要获取项目点击Checkout

![第 39 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第39页.webp)

原文：

要获取项目点击Checkout

### 填写指定地址，点击OK

![第 40 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第40页.webp)

原文：

填写指定地址，点击OK

Checkout

Repository
URL of repository:

https://Cooltinywolf:8443/svn/vc/

Checkout directory:

D:\test\test

Checkout Depth

Fully recursive

V

Omit externals

Revision

HEAD revision

Revision

Show log

OK

Cancel

Help

### PBAT.rc.bak

![第 41 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第41页.webp)

原文：

PBAT.rc.bak
BAK 文件
15 KB

文件Checkout 完成

msxml.tlh
Typelib Generate..
54 KB

PBAT.ncb
VC++ Intellisens..
1,025 KB

Util.h
C/C++ Header
1 KB

### 对要更改的文件加锁

![第 42 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第42页.webp)

原文：

对要更改的文件加锁

打开(0)

PBAT. ncb

iew.cpp
source

PBAT.opt  
OPT 文件  
53 KB

PBATView.h
C/C++ Header
3 KB

Edit with Notepad++
打开方式 (H)

发送到(N)

剪切(T)

属性(R)

Diff with previous version

Show log

Repo-browser

Settings
? Help
About

### 图标改变

![第 43 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第43页.webp)

原文：

图标改变

VII

msado15.tli
Typelib Generate...
75 KB

BatchThread.cpp
C++ Source
3 KB

BatchThread.h
C/C++ Header
1 KB

msxml.tlh
Typelib Generate...
54 KB

PBAT.h
C/C++ Header
2 KB msxml.tli
Typelib Generate.
53 KB

PBATView.cpp
C++ Source
14 KB

PBAT.opt  
OPT 文件  
53 KB

PBATView.h
C/C++ Header
3 KB

### 对项目操作前先检查是否有锁

![第 44 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第44页.webp)

原文：

对项目操作前先检查是否有锁

### litianleiPBAT.h

![第 45 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第45页.webp)

原文：

<table><tr><td>Path</td><td>Text sta...</td><td>Property sta...</td><td>Remote text sta...</td><td>Remote property sta...</td><td>Lock
litianlei</td></tr><tr><td>PBAT.h
res/Thumbs.db</td><td>normal
modified</td><td>normal</td><td></td><td></td><td></td></tr></table>

如果文件有锁则不要对其操作

Working Copy - D:\321

- - -

### 确保在本机编译通过，然后提交

![第 46 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第46页.webp)

原文：

确保在本机编译通过，然后提交

<table><tr><td>查看(V)</td><td></td></tr><tr><td>排列图标(I)刷新(E)</td><td></td></tr><tr><td>自定义文件夹(F)...</td><td></td></tr><tr><td>粘贴(P)粘贴快捷方式(S)撤销重命名(U) Ctrl+Z</td><td></td></tr><tr><td>SVN Update</td><td></td></tr><tr><td>SVN Commit...</td><td></td></tr><tr><td>TortoiseSVN</td><td></td></tr><tr><td>新建(W)</td><td></td></tr><tr><td>属性(R)</td><td></td></tr></table>

### 显示日志

![第 47 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第47页.webp)

原文：

显示日志

Repo-browser
Check for modifications
Revision graph

Resolved...
Update to revision...
Revert...
Clean up
Get lock...
Release lock

查看(V)

排列图标(I)
刷新(E)

Branch/ $\underline{\text{tag}}$ ...
Switch...
Merge...
Export...
Relocate...

自定义文件夹(F)...

粘贴(P)
粘贴快捷方式(S)
撤销重命名(U) Ctrl+Z

\+ Add...

Create patch...
Apply patch...
Properties

Settings
? Help
About

新建(⑧)

属性(R)

### 日志列表

![第 48 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第48页.webp)

原文：

日志列表

<table><tr><td>Action</td><td>Path</td><td>Copy from path</td><td>Revision</td></tr><tr><td>Modified</td><td>/PBAT.clw</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.ncbi</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.opt</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.plg</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBATView.cpp</td><td></td><td></td></tr></table>

### 回滚到指定版本

![第 49 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第49页.webp)

原文：

回滚到指定版本

<table><tr><td>Action</td><td>Path</td><td>Copy from path</td><td>Revision</td></tr><tr><td>Modified</td><td>/PBAT.clw</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.ncbi</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.opt</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBAT.plg</td><td></td><td></td></tr><tr><td>Modified</td><td>/PBATView.cpp</td><td></td><td></td></tr></table>

### 文档上传

![第 50 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第50页.webp)

原文：

文档上传

打开(0)
资源管理器(X)
在这里打开命令行窗口
搜索(E)...

共享和安全(H)...

SVN Checkout...

TortoiseSVN

Repo-browser

添加到压缩文件(A)...

Export...

添加到“document.rar”(T)

压缩并 E-mail...

Create repository here

压缩到“document.rar”并E-mail

Import...

扫描病毒(S)

Expression Media Import

Settings
? Help
About

发送到(N)

剪切(T)

复制(C)

创建快捷方式(S)

删除①)

重命名(M)

属性(R)

\- 第一次上传文档时，在文档上层的文件夹上点击右键TortoiseSVN->Import

### Repository

![第 51 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第51页.webp)

原文：

Repository

URL of repository:

https://Cooltinywolf:8443/svn/PublicDocuments/南京GIS

Import message

Recent messages

□ Include ignored files

OK

Cancel

Help

□ 上传至指定目录

...

文档上传

Import

- □ ×

### 文档下载

![第 52 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第52页.webp)

原文：

文档下载

查看(V)

排列图标(I)
刷新(E)

粘贴(P)
粘贴快捷方式(S)
撤销重命名(U) Ctrl+Z

SVN Checkout...

Repo-browser

新建(Ⅱ)

Export...

属性(R)

Create repository here
Import...

Settings
? Help
About 查看(V)

### 排列图标(I)

![第 53 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第53页.webp)

原文：

排列图标(I)

Repository

刷新(E)

URL of repository:

粘贴(P)

https://Cooltinywolf:8443/svn/PublicDocuments/南京GIS

Checkout directory:

粘贴快捷方式(S)

撤销重命名 (U)

Ctrl+Z

D:\南京GIS

SVN Checkout...

TortoiseSVN

Checkout Depth

Fully recursive

新建(⑧)

Omit externals

属性(R)

Revision

HEAD revision

Revision

Show log

OK

Cancel

Help

文档迁出

×

南京GIS

### 打开 (0)

![第 54 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第54页.webp)

原文：

打开 (0)
资源管理器 (X)
在这里打开命令行窗口
搜索 (E)...

共享和安全(H)...

√ SVN Update

SVN Commit...

TortoiseSVN

添加到压缩文件(A)...

添加到“南京GIS.rar”(T)

压缩并 E-mail...

压缩到“南京GIS.rar”并E-mail

扫描病毒(S)

Expression Media Import

发送到(N)

剪切(T)

复制(C)

粘贴(P)

创建快捷方式(S)

删除①)

重命名 (M)

属性(R)

Commit to:
https://Cooltinywolf:8443/svn/PublicDocuments/南京GIS

Message:

Recent messages

Changes made (double-click on file for diff):

Path

Extens

No files were changed or added since the last commit. There's nothing for TortoiseSVN to do here...

III

Show unversioned files

>

Select / deselect all

0 files selected, 0 files total

□ Keep locks
□ Keep changelists

OK

Cancel

Help

图15G

文档迁入

Commit - D:\南京GIS

- □ ×

...

### SVN配置安装与使用

![第 55 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第55页.webp)

原文：

SVN配置安装与使用

□ 团队模式下的SVN集成应用

■ 场景：我的团队使用Eclipse开发工具平台  
我们搭建了SVN版本服务器  
我们需要在开发平台中直接操作版本项目代码

■ 方法：使用Eclipse开发平台版本管理插件 Subclipse
▪ 安装方法

\- Eclipse Update: http://subclipse.tigris.org/update\_1.4.x

\- 解压安装：http://subclipse.tigris.org/servlets/ProjectDocumentList?folderID=2240

BP: 强烈建议使用本地压缩包方式安装插件

55

### SVN配置安装与使用

![第 56 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第56页.webp)

原文：

SVN配置安装与使用

□ 安装配置Eclipse SVN插件

■ 环境: Eclipse 3.4 [en] + Subclipse1.4.X

■ 步骤:

■ Help -> Software Updates....

Add Site....

Archive....

定位 site-1.4.8.zip 存储路径

Install....

BF: 使用本地安装包的好处是无需再通过网络进行远程文件提取，所有安装文件都在压缩包内，正个过程是在本地进行。成功或失败很快可知。如果使用远程更新，可能需要祈祷网络或远程更新文件状态良好。

56

### SVN配置安装与使用

![第 57 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第57页.webp)

原文：

SVN配置安装与使用

设置SVN配置信息

type filter text

\- □ ×

+General

常规 SVN 设置：

□ 将版本比较显示到对话框中 (C)

替换时删除未加入版本控制的资源(R)

□需要时列举受影响的路径

在远程历史记录视图中显示标记

□ 显示过期目录

√ JavaHL: Commit across multiple projects atomically

√ Automatically share nested projects

缺省日志消息数（0=全部）25

为本地文件注释使用快速比较模式

○是 ○否 ●提示

Commit resources with errors

○是 ○否 ◎提示

-Commit resources with warnings

\- 是 ○ 否 ○ 提示

-SVN 接口：

+Web

Client: JavaHL (JNI) 1.5.6 (r36142)

\+ Web Services

+·XDoclet

+·XML

配置位置：

使用缺省配置位置

使用目录：

浏览...

Restore Defaults

Apply

OK

Cancel

57

### SVN配置安装与使用

![第 58 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第58页.webp)

原文：

SVN配置安装与使用

设置SVN操作视图

SVN 资源
SVN SubestTxt.txt revision graph

\- b++

SubestTxt.txt revision graph

SubestTxt.txt 2 和 8 的比较

<table><tr><td>SubestTxt.txt 2</td><td>SubestTxt.txt 8</td></tr><tr><td>中华人民共和国成立于一九四九年十月一日我们的领袖毛主席教导我们,我们的教育方针应该</td><td>中华人民共和国成立于一九四九年十月一日</td></tr></table>

58

### SVN配置安装与使用

![第 59 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第59页.webp)

原文：

SVN配置安装与使用

从SVN工作视图中检出项目

59

### 总结

![第 60 页](软件工程双语实验4参考资料：Subversion-安装与使用课件.assets/第60页.webp)

原文：

总结

□ 版本控制的必要性

□ SVN提供基于资源管理器的客户端操作方式

□ SVN使用版本库的方式管理文件

□ SVN文件的不同操作状态

□ 使用SVN进行代码分支与版本标签管理

■ 强烈冲突的概念和解决方法

□ 使用Subclipse进行集成环境版本控制操作

60
