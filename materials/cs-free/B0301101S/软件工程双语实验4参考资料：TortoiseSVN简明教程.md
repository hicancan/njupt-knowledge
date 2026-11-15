---
title: 《软件工程（双语）》实验4参考资料：TortoiseSVN简明教程
kind: 实验
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验4参考资料/TortoiseSVN简明教程.pdf
---

# 《软件工程（双语）》实验4参考资料：TortoiseSVN简明教程

原件经识别和整理；“参考解答”是我们补的。

---
title: 软件工程（双语）实验4参考资料：TortoiseSVN简明教程（第1部分）
kind: 实验
course: 软件工程（双语）
source: 识别工具读出的《TortoiseSVN简明教程》第1-10页
---

# 软件工程（双语）实验4参考资料：TortoiseSVN简明教程（第1部分）

本资料整理自识别工具输出的《TortoiseSVN简明教程》前10页内容，主要涵盖TortoiseSVN简介、基本概念及安装与基础使用操作。

## 一、TortoiseSVN 简介

### 什么是 TortoiseSVN

TortoiseSVN 是 Subversion 版本控制系统的一个免费开源客户端，可以超越时间的管理文件和目录。文件保存在中央版本库，除了能记住文件和目录的每次修改以外，版本库非常像普通的文件服务器。你可以将文件恢复到过去的版本，并且可以通过检查历史知道数据做了哪些修改，谁做的修改。这就是为什么许多人将 Subversion 和版本控制系统看作一种“时间机器”。

某些版本控制系统也是软件配置管理 (SCM) 系统，这种系统经过精巧的设计，专门用来管理源代码树，并且具备许多与软件开发有关的特性 - 比如，对编程语言的支持，或者提供程序构建工具。不过 Subversion 并不是这样的系统；它是一个通用系统，可以管理任何类型的文件集，包括源代码。

### 名词解释

**检出工作副本**
你的版本库就像是一台时间机器，它记录了所有提交的修改，允许你检查文件或目录以及相关元数据的历史。通过一个 Subversion 命令你可以根据时间或修订号取出一个过去的版本（或者恢复现在的工作拷贝），然而，有时候我们只是想看看历史而不想回到历史。

**提交修改**
可以理解为上传修改文件的记录，就是把工作副本里面修改过的文件的记录上传到版本库里面。

**更新工作副本**
可以理解为下载最新版本库文件的记录，就是把版本库里面最新上传的文件记录下载到工作副本里面。

**锁定—修改—解锁**
许多版本控制系统使用“锁定—修改—解锁”机制解决这种问题，在这样的模型里，在一个时间段版本库的一个文件只允许被一个人修改。首先在修改之前，Harry要“锁定”住这个文件，锁定很像是从图书馆借一本书，如果Harry锁住这个文件，Sally不能做任何修改，如果Sally想请求得到一个锁，版本库会拒绝这个请求。Harry结束编辑并且放开这个锁之前，她只可以阅读文件。Harry解锁后，就要换班了，Sally得到自己的轮换位置，锁定并且开始编辑这个文件。

![锁定—修改—解锁机制示意图](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图1.jpg)

## 二、TortoiseSVN 安装

### 安装步骤

安装 TortoiseSVN 软件，鼠标左键双击 `TortoiseSVN-1.5.3.13783-win32-svn-1.5.2.msi`，如图所示进行安装。

![安装启动界面](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图2.jpg)

点击 **Next >**。



**End-User License Agreement**
Please read the following license agreement carefully.

**Copyright (C) 2003-2008 - Stefan Küng**

TortoiseSVN is free. You don't have to pay for it, and you can use it any way you want. It is developed as an Open Source project under the GNU General Public License (GPL). That means you have full access to the source code of this program. You can find it on our website at http://tortoisesvn.tigris.org

Should you wish to modify or redistribute this program, or any part of it, you should read the full terms and conditions set out in the license agreement before doing so. A copy of the license is available on our website.

If you simply wish to install and use this software, you need only be aware of the...

- [ ] I accept the terms in the License Agreement
- [ ] I do not accept the terms in the License Agreement

< Back | Next >

![安装路径选择](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图3.jpg)

![组件选择](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图4.jpg)

![安装进度](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图5.jpg)

出现提示，重新启动计算机安装完毕。

![安装完成重启提示](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图6.jpg)

### 安装 TortoiseSVN 遇到问题解决方法

安装 TortoiseSVN 不成功出现错误提示 “Service 'VisualSVNServer' failed to start. Verify that you have sufficient privileges to start system services.”，解决方法：

这是 Windows Installer 的问题，重新安装 Windows Installer 即可，如有安装问题请与管理员联系。

## 三、TortoiseSVN 使用

### 检出工作副本

大多数时候，你会使用 checkout 从版本库取出一个新拷贝开始使用 Subversion，这样会在本机创建一个项目的“本地拷贝”。

在 Windows 资源管理器里选择一个存放工作副本目录。右键点击弹出右键菜单，选择 **TortoiseSVN --> SVN Checkout …**

注：你首先要检出主线（trunk），这样版本库才知道你要接受管理的程序在磁盘哪个目录。看上去什么都没有发生，但实际上这个操作让版本库把你的项目目录纳入管理了在你硬盘的适当的位置（例：e:\test），目标文件夹点击右键，选择 **SVN Checkout…**

![选择检出目录](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图7.jpg)

然后就会弹出一个 Checkout 选项对话框，输入远程项目目录和本地工作目录，例：192.168.1.195 服务器的 svn 目录下的 root 版本库，远程项目地址为：`http://192.168.1.195/svn/root/trunk`

![填写检出信息](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图8.jpg)

点击 OK，就会弹出一个远程服务器要求验证的对话框，输入正确的用户名和密码。

![服务器验证](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图9.jpg)

![检出进行中](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图10.jpg)

检出成功后，会在“检出”目录出现绿色小勾，“检出”根目录也会出现 `.svn` 隐藏目录。

![检出成功状态](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图11.jpg)

### 提交修改

将你对工作副本的修改发送给版本库，称为提交修改。但在你提交之前确保你的工作副本是最新的。你可以直接使用 **TortoiseSVN --> Update**，或者，你可以先使用 **TortoiseSVN --> 检查修改** 看看哪些文件在本地或是服务器上已经有了改动。

如果你的工作副本是最新的，并且没有冲突，你就已经为提交做好准备了，选择你要的文件和/或文件夹，然后 **TortoiseSVN --> commit ......**

在你做了修改之后，你可以在项目文件夹下点击右键或者你修改的文件下点击右键，选择 **SVN Commit…**，这两者的区别在于，第一个可以一次提交你所做所有文件的修改，而第二个只是提交你所选的文件。

![选择提交文件](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图12.jpg)

点击 Commit 之后，就会弹出一个让你输入更改 log 的对话框：

![输入日志](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图13.jpg)

输入你所作的修改，然后点击 OK，就会开始向远程服务器提交修改。



提交文件成功！返回信息：“Finished!”表示文件已成功提交。点击“OK”按钮确定更新文件成功。

## 更新工作副本

更新多个项目在 Subversion 还不是原子操作，所以 TortoiseSVN 会首先找到版本库的 HEAD 修订版本，然后将所有项目更新到特定修订版本，防止出现混合修订版本的工作副本。如果只有一个项目被选中更新，或选中的项目来自不同的版本库，TortoiseSVN 只会更新到 HEAD。

在工作副本里面选定文件夹或文件，右键菜单 TortoiseSVN ---> Update。



cart.php category.php config_basic.php counter.php detail.php detail_ok.php detail_write.php download.php footer.php func_board.php goods.php goods_brand.php header.php index.php

打开(0)

EditPlus

Wopti 文件加密



瑞星杀毒

TortoiseSVN

添加到压缩文件(A)

添加到“alipay_payto.rar”(T)



压缩并 E-mail...

压缩到“alipay_Payto.rar”并 E-mail

发送到(N)

剪切(T) 复制(C)

创建快捷方式(S)

删除(D)

粉碎文件重命名 (M)

属性 (R)

Commit...

Diff with previous version
Show log
Repo-browser
Check for modifications
Revision graph

Update to revision..
Rename...
Delete
Get lock...

Branch/tag...
Switch...
Merge...

Blame...

Properties

Settings
Help
About
egister.pnp
egister_form.php
egister_ok.php
eply.php
earch.php



出现一个对话框，输入正确的用户名和密码即可向版本库提交你想更新文件的信息。

![图 5 输入用户名和密码](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图14.jpg)

更新文件成功！返回信息！“Completed”表示文件已成功更新；“At revision:3”表示更新文件版本号为 3。点击“OK”按钮确定更新文件成功。

![图 6 更新成功返回信息](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图15.jpg)

## 锁定

选择工作副本中你想要获取锁定的文件，然后选择命令 TortoiseSVN ---> Get lock…

![图 7 选择 Get lock](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图16.jpg)

出现一个对话框，允许你输入注释，这样别人知道你为什么锁定这个文件。注释是可选的，并且只用于基于 Subversion 的库。选择需要锁定的文件在复选框打勾，点击“确定”按钮锁定选择的文件。

![图 8 输入锁定注释](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图17.jpg)

出现一个对话框，输入正确的用户名和密码即可向版本库提交你想锁定文件的信息。

![图 9 输入用户名和密码](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图18.jpg)

锁定文件成功！返回信息！“Locked by admin”表示文件已被 admin 用户锁定；“alpay_payto.php”表示锁定文件的名称。点击“OK”按钮确定锁定文件成功。

![图 10 锁定成功返回信息](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图19.jpg)

## 释放锁定（取消锁定）

选择工作副本中你想要取消锁定的文件，然后选择命令 TortoiseSVN ---> Release lock…

![图 11 选择 Release lock](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图20.jpg)

出现一个对话框，选择需要取消锁定的文件在复选框里打勾，点击“确定”按钮。

![图 12 选择需取消锁定的文件](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图21.jpg)

出现一个对话框，输入正确的用户名和密码即可向版本库提交你想取消锁定文件的信息。

![图 13 输入用户名和密码](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图22.jpg)

取消锁定文件成功！返回信息！“Unlocked Finished!”表示文件已被解除锁定；“alpay_payto.php”表示解除锁定文件的名称。点击“OK”按钮确定锁定文件成功。

![图 14 取消锁定成功返回信息](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图23.jpg)

## TortoiseSVN 语言包安装

如果有英文不太好的朋友可以安装 TortoiseSVN 语言包支持中文。

Welcome to the Chinese, simplified Languagepack for TortoiseSVN Setup Wizard

![图 15 语言包安装向导](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图24.jpg)

Next

Cancel

Chinese, simplified Languagepack for TortoiseS...

Installing Chinese, simplified Languagepack for TortoiseSVN

Please wait while the Setup Wizard installs Chinese, simplified Languagepack for TortoiseSVN.

Status:

Cancel

![图 16 语言包安装成功](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图25.jpg)

Chinese, simplified Languagepack for TortoiseS...

安装完 TortoiseSVN 语言包，在空白处单击鼠标右键，在弹出的菜单选择“TortoiseSVN ---> Settings”。

![图 17 打开 Settings](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图26.jpg)

如下图所示，在出现的对话框选择“Language：中文（简体）”--- 鼠标左键单击“确定”按钮。

![图 18 TortoiseSVN 设置语言选项](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图27.jpg)

查看(V)

排列图标(I)

刷新(E)

自定义文件夹(F)..

粘贴(P)

粘贴快捷方式(S)

撤销重命名(U)
Ctrl+Z

SVN 检出 (K)...

TortoiseSVN

新建(W)

属性(R)

如图所示，TortoiseSVN 设置语言成功。

版本库浏览器 (R)

导出(X)...

在此创建版本库(Y)
导入(I)...

设置(S)

?帮助(O)

关于(B)

该页面允许你指定：在 TortoiseSVN 的主上下文菜单中哪些条目可以直接在鼠标右键菜单显示，哪些在 TortoiseSVN 子菜单显示。默认情况下很多项未被勾选，只在子菜单显示。

获得锁会有一个特别的情况，你可以将其提升到顶级菜单，但是大多数文件不需要锁定，这样做只是添加了混乱。然而，一个标记为 svn:needs-lock 属性的文件每次编辑前都需要那个操作，所以这个菜单会进入顶级菜单会比较方便。选定这个选项，会使设置 svn:needs-lock 属性的文件的 Get Lock 出现在顶级菜单中。

![图 19 TortoiseSVN 菜单设置](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图28.jpg)

| 菜单项 | 快捷键 |
| --- | --- |
| 查看 (V) |  |
| 排列图标 (I) |  |
| 刷新 (E) |  |
| 自定义文件夹 (F)... |  |
| 粘贴 (P) |  |
| 粘贴快捷方式 (S) |  |
| 撤销重命名 (U) | Ctrl+Z |
| SVN 检出 (K)... |  |
| SVN 版本库浏览器 (R) |  |
| SVN 导出 (X)... |  |
| SVN 在此创建版本库 (Y) |  |
| SVN 导入 (I)... |  |
| TortoiseSVN |  |
| 新建 (W) |  |
| 属性 (R) |  |

## 其它功能

### 回到置顶

点击回到置顶。

### 网页浏览

你可以使用该地址 https://192.168.1.195/svn/root/trunk/ 在网页上浏览项目，同样需要和前面一样的密码。

### Revert

取消上一次的操作（只针对客户端，服务端不做改动）。

![图 22 Revert 对话框](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图29.jpg)

### Revision Graph：版本示意图





![图 25 Revision Graph 示例](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图30.jpg)

![图 26 Revision Graph 版本关系](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图31.jpg)

![图 27 Revision Graph 分支示意](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图32.jpg)

### Show log：查看版本日志及不同版本间相互比较

![图 28 Show log 菜单](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图33.jpg)

![图 29 Show log 日志窗口](软件工程双语实验4参考资料：TortoiseSVN简明教程.assets/图34.jpg)

## 检查修改与版本比较

Check for modifications：同服务器上的项目版本进行比较，并可做相应的修改。

右键菜单（工作副本）中包含以下操作：

- Update
- Commit...
- Show log
- Repo-browser
- Check for modifications
- Revision graph
- Resolved...
- Update to revision...
- Revert...
- Clean up
- Get lock...
- Release lock
- Branch/tag...
- Switch...
- Merge...
- Export...
- Relocate...
- Add...
- Create patch...
- Apply patch...
- Properties
- Settings
- Help
- About

「检查修改」窗口（Working Copy - D:\upload）中各列含义如下：

| Path | Text status | Property status | Remote text status | Remote property status | Lock | Lock comment | Author | Revision | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| upload | normal |  |  |  |  |  | admin | 1 | 20... |
| admin | normal |  |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal |  |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal |  |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |
| admin/a... | normal | normal |  |  |  |  | admin | 2 | 20... |

窗口底部选项：

- Show unversioned files
- Show unmodified files
- Show ignored files
- Show properties

状态统计：normal=1574, non-versioned=0, modified=0, added=0, deleted=0, conflicted=0

## 小技巧

工作副本下 .svn 目录被删除了怎么办？

工作拷贝中的任何一个目录包括一个名为 .svn 的管理区域，通常列表操作不显示这个目录，但它仍然是一个非常重要的目录，无论你做什么，都不要删除或是更改这个管理区域的任何东西，Subversion 使用它来管理工作拷贝。

如果你不小心删除了子目录 .svn，最简单的解决办法是删除包含的目录（普通的文件系统删除，而不是 svn delete），然后在父目录运行 svn update，Subversion 客户端会重新下载你删除的目录，并包含新的 .svn。
