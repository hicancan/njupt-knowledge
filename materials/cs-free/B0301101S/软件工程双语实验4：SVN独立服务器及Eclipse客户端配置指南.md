---
title: 《软件工程（双语）》实验4：SVN独立服务器及Eclipse客户端配置指南
kind: 实验
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验4参考资料/svn独立服务器及eclipse客户端配置.doc
---

# 《软件工程（双语）》实验4：SVN独立服务器及Eclipse客户端配置指南

原件经识别和整理；“参考解答”是我们补的。

---
title: 软件工程（双语）实验4：SVN独立服务器及Eclipse客户端配置指南
kind: 实验
course: 软件工程
source: 《软件工程（双语）》实验指导书
---

# 软件工程（双语）实验4：SVN独立服务器及Eclipse客户端配置指南

本资料整理自《软件工程（双语）》实验指导书，内容涵盖Subversion (SVN) 独立服务器的安装、配置以及 Eclipse 客户端插件的安装与项目版本控制操作。

## 一、服务端配置

### 1. 安装 Subversion

例如使用 `Setup-Subversion-1.6.15.msi`安装包，按缺省方式安装即可。

### 2. 创建 SVN 服务根目录

在资源管理器中创建 SVN 服务根目录，例如：`D:\svn\Repositories`

### 3. 建立代码版本仓库

进入 DOS 窗口，执行以下命令：

```bash
svnadmin create d:\svn\Repositories\repository
```

该命令会在根目录 `d:\svn\Repositories\` 下生成一个叫 `repository` 的目录，目录结构如下：

- conf
- db
- hooks
- locks
- format
- README.txt

### 4. 启动服务

#### (1) 命令行启动

```bash
svnserve -d -r D:\svn\Repositories
```

**注：**
- `-d` 参数效果同于 `--daemon`，告诉 svnserve 以守护进程方式运行，这样在手动终止之前不会退出。
- `-r` 参数效果同于 `--root`，告诉 svnserve 将会在端口 3690 等待请求，设置根位置来限制服务器的访问目录，从而增加安全性和节约输入 svnserve URL 的时间。

如果不加 root 参数，服务 URL 为：`svn://localhost/svn/repository`
而如果加上 root 参数，服务 URL 为：`svn://localhost/repository`

通常 SVN 服务器都是远程的，所以记得将 `localhost` 换成实际的 SVN 服务器的 IP。

另外，DOS 窗口不能关，否则服务将停止。不要关闭命令行窗口，关闭窗口会把 svnserve 停止。

#### (2) 批处理文件启动

（原文略）

### 5. 配置用户和权限

#### (1) 编辑配置文件

编辑 `d:\svn\Repositories\repository\conf` 下的 `svnserve.conf`，去掉 `password-db=passwd` 前的注释。

#### (2) 修改用户密码文件

修改同目录下的 `passwd` 文件，在 `[users]` 下加上授权用户和密码，如：

```ini
[users]
Username1 = password1
```

## 二、客户端配置

### 1. 为 Eclipse 安装 SVN 插件

（略掉具体步骤）

### 2. 将本地项目上传到 SVN 服务器上

在本地 Eclipse 工程上右击，选择 **Team => Share Project**，按提示操作。

这个向导将帮助您将您的文件共享到 SVN 资源库。您的项目将会自动导入到 SVN 资源库中，同时会打开同步视图以允许您提交您的资源。

#### 创建新的资源库位置 (Create a new repository location)

![图 1](<资料名>.assets/图1.png) 创建新的资源库位置界面

#### 使用已有资源库位置 (Use existing repository location)

定义连接至现有 SVN 资源库所必需的位置和协议信息。

示例 URL：`svn://localhost/repository`

![图 2](<资料名>.assets/图2.png) 使用已有资源库位置界面

**注：** 上图的 URL 中，`localhost` 和 `repository` 都是变量，需根据实现情况来决定。`Localhost` 需换成 SVN 服务器的实际 IP；`repository` 是在 SVN 服务器上创建的版本仓库名，即本文开始部分“`svnadmin create d:\svn\Repositories\repository`”命令所指定的目录。

#### 选择 SVN 资源库中的文件夹名

选择 SVN 资源库中的文件夹名。

- 使用项目名称做为文件夹名
- 使用指定的模块名：

URL : `svn://localhost/repository/mini`

![图 3](<资料名>.assets/图3.png) 指定模块名界面

如上图，一步一步走完。这时候会建立本地项目与 SVN 服务器的关联。但本地文件却并不会马上上传到 SVN 服务器，需再执行一次提交即可将本地名为 `mini` 的项目放到 SVN 服务器中，建立起对该项目的版本控制。提交时会被要求输入用户名和密码，按照 SVN 服务器上 `passwd` 文件中配置的授权账号录入即可。

**注：** 可以将项目中不想提交的文件夹执行 **Team --> 添加到 .svn:ignore**，忽略在版本控制之外。

### 3. 从 SVN 服务器上检出项目工程

![图 4](<资料名>.assets/图4.png) 检出项目主界面

#### 创建新的资源库位置 / 使用现有的资源库位置

选择/新建位置。

示例选项：
- `http://192.168.1.167:88/svn/test1`
- `http://localhost/svn`
- `svn://192.168.1.167`
- `svn://localhost/repository`

![图 5](<资料名>.assets/图5.png) 选择资源库位置界面

选中 `svn://localhost/repository`，点击 Next。

#### 选择文件夹

选择要从 SVN 检出的文件夹。

显示文件夹列表：
- SVN
    - mini

![图 6](<资料名>.assets/图6.png) 选择检出文件夹界面

#### 选择检出方式

选择检出的方式。

选项包括：
- 做为新项目检出，并使用新建项目向导进行配置
- 做为工作空间中的项目检出

项目名称：`mini-web`
Revision: `Check out HEAD revision`
Depth: `Fully recursive`
其他选项：`Ignore externals`, `Allow unversioned obstructions`

![图 7](<资料名>.assets/图7.png) 检出配置界面

完成上面的系列步骤后，一个工程即从 SVN 服务器上被检出到开发者本地。
