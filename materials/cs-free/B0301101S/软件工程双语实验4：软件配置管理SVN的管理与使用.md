---
title: 《软件工程（双语）》实验4：软件配置管理SVN的管理与使用
kind: 实验
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验4参考资料/Experiment 4 Software Configuration managementExercise and Reviews实验要求.pdf
---

# 《软件工程（双语）》实验4：软件配置管理SVN的管理与使用

原件经识别和整理；“参考解答”是我们补的。

## 一、实验目的

了解开源软件配置工具 SVN 的安装、配置和使用。

## 二、实验内容

本实验需要完成以下任务：

1. 安装 SVN 服务器端软件 Visual SVN Server 及配置
2. 安装 SVN 客户端软件 TortoiseSVN 及配置

## 三、实验步骤

### 1、安装服务器端 Visual SVN Server

![启动 Server 管理器](<实验四 软件配置管理SVN的管理与使用.assets/启动Server管理器.jpg>)

![启动初始界面](<实验四 软件配置管理SVN的管理与使用.assets/启动初始界面.jpg>)

### 2、安装客户端 TortoiseCVS

（建议：在另外一台机器上）

http://tortoisesvn.sourceforge.net/downloads

下载，直接点击下一步，安装完毕后，重启机器。

### 3、配置 SVN 服务器的用户、用户组和权限

![（注意：仓库的 URL）](<实验四 软件配置管理SVN的管理与使用.assets/仓库URL.jpg>)

![（注意：请分别创建两个用户）右键项目名称，设置访问权限](<实验四 软件配置管理SVN的管理与使用.assets/创建用户并设置权限.jpg>)

### 4、客户端链接服务器端

在客户端机器上，新建一个工作目录，比如 F:\MyProject

![右键文件夹，SVN 检出](<实验四 软件配置管理SVN的管理与使用.assets/SVN检出.jpg>)

![指定仓库的 URL 路径](<实验四 软件配置管理SVN的管理与使用.assets/指定仓库URL路径.jpg>)

（若仓库在本机，使用 file:///C:/SVN 类似地址；若仓库在远端服务器，则使用 https://IP:8443/svn 类似地址）

输入用户名和密码之后，显示类似如下界面，表示检出成功。

![检出成功](<实验四 软件配置管理SVN的管理与使用.assets/检出成功.jpg>)

### 5、SVN 常用功能操作

完成 svn 的添加、提交、更新、分支、合并等操作。

![添加文件](<实验四 软件配置管理SVN的管理与使用.assets/添加文件.jpg>)

![提交文件或文件夹](<实验四 软件配置管理SVN的管理与使用.assets/提交文件或文件夹.jpg>)

在 svn 客户端的项目文件夹中，使用不同图标来表示文件状态。

- A green check = file is identical to svn repository
- A Red "!" = file is different from svn repository
- A blue "+" means the file has been added to the repository, but it must still be committed.
- no mark at all = file is not in repository.

分支、合并等功能请参阅操作手册，自主完成。

## 四、参考资料

1. Visual SVN Server http://www.visualsvn.com/server/download/
2. Tortoisesvn http://tortoisesvn.sourceforge.net/downloads
