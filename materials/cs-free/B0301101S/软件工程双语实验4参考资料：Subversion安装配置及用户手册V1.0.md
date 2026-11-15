---
title: 《软件工程（双语）》实验4参考资料：Subversion安装配置及用户手册V1.0
kind: 实验
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验4参考资料/SVN安装配置及使用说明.pdf
---

# 《软件工程（双语）》实验4参考资料：Subversion安装配置及用户手册V1.0

原件经识别和整理；“参考解答”是我们补的。

## 第一章 Subversion 服务器及客户端软件安装

本章主要介绍 Subversion 软件在节点上的安装方法。

### 1.1 系统配置

运行 Subversion 软件 XP/2003 版本所需系统最低配置如下：
- 处理器：PIII 1GHz 或 PIV
- 内存：256M
- 网卡：10/100M
- 操作系统：Microsoft Windows XP SP2/2003/Vista

### 1.2 Subversion 服务器端安装

1）双击 `CollabNetSubversion-server-1.5.6-2.win32.exe`

2）点击“next”按钮，进入下一步

![CollabNet Subversion Server 1.5.6 Setup 欢迎界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图1.jpg)

3）点击“next”按钮，进入下一步

![许可协议界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图2.jpg)

4）默认勾选后，点击“next”按钮，进入下一步

![选择组件界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图3.jpg)

5）输入端口号和路径，点击“next”按钮，进入下一步

![端口和路径设置界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图4.jpg)

6）输入 Apache 的配置信息，点击“next”按钮，进入下一步

![Apache 配置界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图5.jpg)

7）输入安装路径，点击“install”按钮，进入下一步

![安装路径设置界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图6.jpg)

8）点击“finish”按钮，完成服务器端安装。

![安装完成界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图7.jpg)

### 1.2 Subversion 客户端安装——TortoiseSVN

#### 主程序安装

1）双击 `TortoiseSVN-1.5.6.14908-win32-svn-1.5.5.msi`

2）点击“next”按钮，进入下一步

![TortoiseSVN 安装向导欢迎界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图8.jpg)

3）选中“同意”，点击“next”按钮，进入下一步



4）点击“next”按钮，进入下一步

![TortoiseSVN 安装选项界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图9.jpg)

5）点击“install”按钮，进入下一步安装

![TortoiseSVN 安装过程界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图10.jpg)

6）点击“finish”按钮，完成安装。

![TortoiseSVN 安装完成界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图11.jpg)

#### 中文语言包安装

1）双击 `LanguagePack_1.5.6.14908-win32-zh_CN.msi`

2）点击“next”按钮，进入下一步

![中文语言包安装向导界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图12.jpg)

3）点击“finish”按钮，完成安装

![中文语言包安装完成界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图13.jpg)

#### 设置中文界面

1）在桌面任意位置，点击鼠标右键 -> TortoiseSVN -> Settings...

![TortoiseSVN 右键菜单](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图14.jpg)

2）选择 General -> Language 选择中文（简体），点击“确定”即可完成其中文化。

![TortoiseSVN 语言设置界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图15.jpg)

### 1.3 Subversion 客户端安装——AnkhSvn

#### 主程序安装

1）双击 `AnkhSvn-2.0.6347.433.msi`

2）选中“同意”，点击“Install”按钮，进入下一步

![AnkhSvn 安装向导界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图16.jpg)

3）等待安装，随后点击“finish”按钮，完成安装。

![AnkhSvn 安装完成界面](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图17.jpg)

## 第二章 Subversion 服务端配置说明

本章主要介绍 Subversion 服务端的配置。

本 Subversion 服务端，采用开源且应用最广泛的 CollabNet Subversion-server 的 1.5.6-2 版本进行配置。该版本秉承着稳定性高、安全性可靠，和有经过认证的加载项和插件配合开发工具等优点。

### 2.1 建立版本库

1) 运行 Subversion 服务器首先需要建立一个版本库（Repository），可以看作服务器上存放数据的数据库，在安装了 Subversion 服务器之后，可以直接运行。

如：在命令行模式中执行命令 `svnadmin create C:\svn\_repository` 就会在目录 `C:\svn\_repository` 下创建一个版本库。

我们也可以使用 TortoiseSVN 图形化地完成这一步：

在目录 `C:\svn\_repository` 下"右键 -> TortoiseSVN -> 再次创建版本库，然后可以选择版本库模式，这里使用默认即可，然后就创建了一系列目录和文件。

如图所示：

![版本库浏览器右键菜单](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图18.jpg)

关于 svnserve 命令及相应参数解释说明：

```
svnserve -help
usage: svnserve [options]
Valid options:
-d [--daemon]: daemon mode
后台模式
--listen-port ARG: listen port (for daemon mode)
监听端口（后台模式）
--listen-host ARG: listen hostname or IP address (for daemon mode)
监听主机名或 IP 地址（后台模式）
--foreground: run in foreground (useful for debugging)
在前台运行（调试用）
-h [--help]: display this help
显示本帮助
--version: show program version information
显示程序版本信息
-i [--inetd]: inetd mode
inetd 模式
-r [--root] ARG: root of directory to serve
服务的根目录
-R [--read-only]: force read only, overriding repository config file
强制只读；覆盖仓库配置文件
-t [--tunnel]: tunnel mode
隧道模式
--tunnel-user ARG: tunnel username (default is current uid's name)
隧道用户名（默认是当前 UID 对应的用户名）
-X [--listen-once]: listen once (useful for debugging)
监听一次（调试用）
--config-file ARG: read configuration from file ARG
将配置文件写入文件 ARG 中
--pid-file ARG: write server process ID to file ARG
将服务进程 ID 写入文件 ARG 中
--service: run as a windows service (SCM only)
作为 windows 服务运行（仅 SCM）
```

### 2.2 配置用户

1) 来到 `C:\svn\_repository\conf` 目录，修改 svnserve.conf，原始代码如下：

```
[general]
# anon-access = read
# auth-access = write
# authz-db = authz
# auth-access = write
# password-db = passwd
```

改为：

```
[general]
anon-access = none    //未通过验证的用户没有操作权限
auth-access = write   //通过验证的用户才能有读写的权限
authz-db = authz      //验证用户所使用的文件 authz
password-db = passwd  //验证用户所使用的文件 passwd
```

2) 然后修改同目录的 passwd 文件，去掉下面三行的注释：

```
[users]
# harry = harryssecret
# sally = sallyssecret
```

最后变成：

```
[users]
User1=password1   //以名值的方式存储用户名和密码“用户名=密码”
User2= password2
```

3) 修改同目录下的 authz 文件来设置访问权限

在 `[groups]` 下创建用户组，例如这里是

```
[groups]
Admin=admin
Developer=developer1,developer2
```

以上便创建了两个用户组，分别是 admin 和 developer 和其相应的组的成员。

设置访问路径

```
[/]
*=r
@admin=rw
```

如上所示，所有的用户对整个 svn 目录下的文件都可以读取，admin 组有读写的权限（“*”代表所有的用户，r 代表读，w 代表写）

可设置具体的版本库的访问权限如下：

```
[版本库 A:/]
@developer=rw
```

如上设置，表示所有 developer 组的成员对于“版本库 A”下边的所有文件都有读写的权限。



1. Subversion 不支持微软格式的 UTF-8 文件，不支持 unicode，仅支持标准 UTF-8，就是头部有一个 FF FE 的文件。
2. 用微软自带的“记事本”编辑出来的任何 unicode 格式文件，Subversion 均不认识。
3. 只要使用了 Subversion 支持的标准 UTF-8 文件，Subversion 就可以很好地实现对中文的支持，包括中文用户名、中文目录、中文组名。
4. 将权限文件改成 UTF-8 格式，使用的是 UltraEdit 的菜单 "ASCII to UTF-8(Unicode Editing)"。

### 2.3 运行独立服务器

在任意目录下运行：（如果提示找不到 svnserve 则检查 `%Subversion 安装目录%\bin` 是否已添加至环境变量 PATH）

```
svnserve -d -r C:\svn\_repository\
```

我们的服务器程序就已经启动了。如下图所示：

![svnserve 启动窗口](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图19.jpg)

（注：在此模式下，不可关闭此窗口，否则系统会关闭该服务）

附：将 svnserve 安装为系统服务

如果服务安装的有问题，你可能需要删除服务。要删除前面添加的服务，只需要运行 `sc delete svnservice`，`svnservice` 就是我们创建服务时使用的名字。

## 第三章 Subversion 版本库备份手册

版本控制最关键的一件事是保证数据的安全性，不能因为磁盘损坏、程序故障造成版本库无可挽回的错误，为此必须制定较完备的备份策略。在 Subversion 中，我们有三种备份方式：完全备份、增量备份和同步版本库。

### 3.1 完全备份

最常见和简单的备份就是直接使用拷贝命令，将版本库目录拷贝到备份目录上，就可以了。但是这样不是很安全的方式，因为如果在拷贝时版本库发生变化，将会造成备份的结果不够准确，失去备份的作用，为此 Subversion 提供了 `svnadmin hotcopy` 命令，可以防止这种问题。

如果要把 yxv3 备份到 `d:\svnrootbak` 目录下，只需要运行：

```
svnadmin hotcopy d:\svnroot\ yxv3 d:\svnrootbak\ yxv3
```

但是我们作为配置管理员，必须想办法优化这个过程，如果我们这个目录下有许多版本库，需要为每个版本库写这样一条语句备份，为此实现下面的脚本，备份一个目录下的所有版本库。

在 `D:\SVNROOT` 下创建了两个文件，prjBackup.bat：

这个文件仅仅是对 `svnadmin hotcopy` 的包装，然后是 backup.bat：

使用的时候，只需要修改 backup.bat 开头的三个路径，将两个脚本拷贝到 `SVN_ROOT` 下就可以了。根据以上的配置，你只需要运行 backup.bat，就可以把 `SVN_ROOT` 下的版本库都备份到 `BACKUP_SVN_ROOT` 里，并且存放在备份所在日期目录里，例如 `D:\svnrootbak\2006-10-22`。

虽然这部分工作很简单，可是必须有人定时地去执行这个操作（例如每周一凌晨），为了避免发生遗忘的情况，我们可以将这个操作加入到系统的 at 任务当中去，例如还是上面的环境，为了安装 at 任务，我们运行：

```
at 1:00 /every:M D:\svnroot\backup.bat
```

这样在每周一凌晨 1:00 都会执行这个备份过程。当然备份在本机也是不安全的，也许需要上传到别的机器，这个就要靠自己去实现了。

### 3.2 增量备份

尽管完全备份非常简单，但是也是有代价的，当版本库非常巨大时，经常进行完全备份是不现实的，也并不必要，但是一旦版本库在备份之间发生问题，该如何呢，这里我们就用到了增量备份。

增量备份通常要与完全备份结合使用，就像 oracle 数据库的归档日志，记录着每次 Subversion 提交的变化，然后在需要恢复时能够回到最新的可用状态。在我们这个例子中我们使用的是 `svnadmin dump` 命令进行增量的备份，使用方法是：

```
svnadmin dump yxv3 --revision 15 --incremental > dumpfile2
```

上面的命令实现了对修订版本 15 进行增量的备份，其中的输出文件 dumpfile2 只保存了修订版本 15 更改的内容。

为了记录每次提交的结果，需要使用一项 Subversion 的特性——钩子（hook），看看 yxv3 目录：

其中的 hooks 目录里存放的就是钩子脚本，我们在此处只使用 post-commit 钩子，这个钩子会在每次提交之后执行，为了实现我们的备份功能，我们在 hooks 下建立一个文件 post-commit.bat，内容如下：

通过这个脚本，可以实现 `D:\svnroot` 下的版本库提交时自动增量备份到 `D:\svnrootbak\delta`（确定这个目录存在），其中使用的 deltaBackup.bat 其实可以放在任何地方，只是对脚本的 `svnadmin dump` 的包装，内容如下：

以上两个脚本可以直接拷贝到 yxv3 的 hooks 目录下，不需要修改就可以实现 yxv3 的自动备份。

以上的操作已经 OK 了，现在需要做的是将完全备份和增量备份结合起来，也就是在完全备份后清理增量备份的结果，使之只保存完全备份后的结果。

当果真出现版本库的故障，就要求我们实现版本库的恢复操作了，这时要使用 `svnadmin load` 命令，同时也需要上次的完全备份。例如要把上次完全备份 backuprepo，和之后的增量备份 dumpfile：

```
svnadmin load backuprepo < dumpfile
```

可以解压 svnroot.rar 到 `d:\` 下，然后修改几个 bat 文件的 `SVN_HOME` 就可以使用了。

### 3.3 版本库同步

Subversion 1.5 增加了同步机制，可以实现一个版本库同另一个版本库的同步（但好像只是单向的），我们可以用来实现版本库的备份或镜像。

#### 3.3.1 对目标库初始化

```
svnsync init svn://localhost/project2 svn://localhost/project1
```

其中 project2 是目标的版本库，而 project1 是源版本库。其中的目标版本库必须为空，而且必须允许修订版本属性的修改，也就是在目标的版本库的 hooks 目录里添加一个文件 pre-revprop-change.bat，内容为空即可。

#### 3.3.2 同步 project2 到 project1

```
svnsync sync svn://localhost/project2
```

这时候 update 一下你的 project2 的一个工作拷贝，就会发现有了 project1 的所有内容。如果 project1 又有提交，这时候 project2 的版本库无法看到最新的变化，还需要再运行一遍 sync 操作，这样才能将最新的变化同步。需要注意的是，目标版本库只能做成只读的，如果目标版本库发生了变更，则无法继续同步了。

#### 3.3.3 同步历史属性的修改

因为同步不会更新对历史属性的修改，所以 svnsync 还有子命令 copy-revprops，可以同步某个版本的属性。

#### 3.3.4 钩子自动同步

希望在每次提交时同步，则需要在源版本库增加 post-commit 脚本，内容如下：

把以上内容存放为 post-commit.bat，然后放到版本库 project1 下的 hooks 目录下，这样 project1 每次提交，都会引起 project2 的同步。

## 第四章 客户端使用说明——TortoiseSVN

本章主要介绍 Subversion 客户端软件 TortoiseSVN 的使用方法。

TortoiseSVN 是最常用的 Subversion 客户端软件，它有效地集成在系统右键菜单中，增加了使用的方便性，尤其中文化后，更提升了掌握软件的速度。

### 4.1 初始化导入

对于 Subversion 来讲，服务端进行配置后，版本库第一次运行，会由项目经理进行第一次的导入操作。

来到我们想要导入的项目根目录，在这个例子里是 `D:\ZedGraphSampleCS\_v5.0.9`，目录下有若干个文件：

1) 右键 → TortoiseSVN → 导入...

2) 版本库 URL 输入 `svn://192.168.70.50/test`（此处版本库 URL 为 Subversion 服务端 IP 地址），点击确定。

![图 4-1 输入版本库 URL](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图20.jpg)

3) 系统提示输入用户名和密码，这里输入 user1，密码 password（此处用户名和密码均为第二章中所配置的“passwd”文件中的内容）。

![图 4-2 输入用户名和密码](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图21.jpg)

出现如下窗口表示已添加成功：

![图 4-3 导入成功](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图22.jpg)

至此初始的数据就已经全部导入到了我们刚才定义的版本库中。

### 4.2 SVN 检出

该操作可以将 SVN 服务端所保存的数据下载至个人工作平台，通常用于第一次链接该版本库。

来到我们想要导入的项目根目录，在这个例子里是 `D:\test`，该目录为空目录：

1) 右键 → SVN 检出...

| 菜单项 | 快捷键 |
| --- | --- |
| 查看(V) | |
| 排列图标(I) | |
| 刷新(E) | |
| 自定义文件夹(F)... | |
| 粘贴(P) | |
| 粘贴快捷方式(S) | |
| 撤销删除(U) | Ctrl+Z |
| SVN 检出(K)... | |
| TortoiseSVN | |
| 新建(W) | |
| 属性(R) | |

2) 版本库 URL 输入 `svn://192.168.70.50/test`（此处版本库 URL 为 Subversion 服务端 IP 地址；检出至目录为 `d:\test`），点击确定。

![图 4-4 输入版本库 URL 与检出目录](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图23.jpg)

通常情况下为最新版本，如需要其他版本，点击显示日志进行选择。

| 版本 | 操作 | 作者 | 日期 | 信息 |
| --- | --- | --- | --- | --- |
| 28 | | lzkuilei | 15:56:35, 2009年5月26日 | 初始化 |

初始化明细：

| 操作 | 路径 | 从路径复制 | 版本 |
| --- | --- | --- | --- |
| 已增加 | /test | | |
| 已增加 | /test/ZedGraph.dll | | |
| 已增加 | /test/ZedGraphSample | | |
| 已增加 | /test/ZedGraphSample/Form1.Designer.cs | | |
| 已增加 | /test/ZedGraphSample/Form1.cs | | |

### 4.3 工作平台中文件的修改及版本库的提交

下面以修改版本库属性为例进行演示。

关于定义必填日志选项，在配置管理员进行第一次导入后，需进行必填日志项的配置。

1) 选择版本库文件夹，右键 → 属性 → Subversion，点击“属性”，新建一个属性 `tsvn:logminsize`，赋值为：1。点击提交如下图操作即可。

![图 4-5 新建 tsvn:logminsize 属性](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图24.jpg)

修改后，版本库文件夹图标变为：

![图 4-6 文件夹图标变化](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图25.jpg)

表示文件夹或其中的文件与上次更新的版本库相比发生了改变。

2) 点击右键 → SVN 提交

| 菜单项 | 快捷键 |
| --- | --- |
| 查看(V) | |
| 排列图标(I) | |
| 刷新(E) | |
| 自定义文件夹(F)... | |
| 粘贴(P) | |
| 粘贴快捷方式(S) | |
| 撤销删除(U) | Ctrl+Z |
| SVN 更新(U) | |
| SVN 提交(C)... | |
| TortoiseSVN | |
| 新建(W) | |
| 属性(R) | |

弹出下列窗口，此时信息栏变为必填项。

提交 - `D:\test`

提交至：`svn://192.168.70.50/test`

信息：

![图 4-7 提交窗口](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图26.jpg)

变更列表（双击文件查看差异）：

☑ 全选/全不选(A)

确定(O)　取消(C)　帮助(H)

出现如下窗口表示已添加成功：

![已添加成功的提示窗口](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图27.jpg)



### 1）下图为对应的 TortoiseSVN 的图标概念

![TortoiseSVN 图标概念（1）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图28.jpg)

![TortoiseSVN 图标概念（2）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图29.jpg)

![TortoiseSVN 图标概念（3）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图30.jpg)





![TortoiseSVN 图标概念（6）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图31.jpg)

![TortoiseSVN 图标概念（7）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图32.jpg)

![TortoiseSVN 图标概念（8）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图33.jpg)

![TortoiseSVN 图标概念（9）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图34.jpg)

![TortoiseSVN 图标概念（10）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图35.jpg)

![TortoiseSVN 图标概念（11）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图36.jpg)

![TortoiseSVN 图标概念（12）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图37.jpg)

![TortoiseSVN 图标概念（13）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图38.jpg)

![TortoiseSVN 图标概念（14）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图39.jpg)

![TortoiseSVN 图标概念（15）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图40.jpg)

![TortoiseSVN 图标概念（16）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图41.jpg)



![TortoiseSVN 图标概念（18）](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图42.jpg)

### 2）增加文件、删除文件

增加文件，删除文件，对于系统来讲都是一次修改操作，所以与本节操作基本上同。

## 4.4 TortoiseSVN 的常规功能说明

本节主要叙述 TortoiseSVN 中的一些常规功能，右键 -> TortoiseSVN，具体如下图所示：

![右键 TortoiseSVN 菜单](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图43.jpg)

### 1）显示日志

该功能主要显示版本库中过往的版本更新记录，在操作中可以显示更改的详情。

| 版本 | 操作 | 作者 | 日期 | 信息 |
| --- | --- | --- | --- | --- |
| 31 |  | lzkuilei | 16:51:16, 2009年5月26日 | 增加文件 |
| 30 |  | lzkuilei | 16:50:10, 2009年5月26日 | dd |
| 29 |  | lzkuilei | 16:27:11, 2009年5月26日 | 将版本库信息选择为必填 |
| 28 |  | lzkuilei | 15:56:35, 2009年5月26日 | 初始化 |

### 2）版本库浏览器

即为版本库的浏览工具，可以直观地显示版本库中的受控文件。

| 文件 | 扩展名 | 版本 | 作者 | 大小 | 日期 |
| --- | --- | --- | --- | --- | --- |
| ZedGraphSample |  | 28 | lzkuilei |  | 2009-5 |
| ZedGraph.dll | .dll | 31 | lzkuilei | 296 KB | 2009-5 |
| ZedGraphSample.sln | .sln | 28 | lzkuilei | 935 字节 | 2009-5 |

### 3）检查更新

即更新为版本库中已变更的版本，并显示与本地工作平台不同的文件。

| 路径 | 文字状态 | 属性状态 | 远程文字状态 | 远程属性状态 | 锁定 | 锁定备注 | 作者 | 版本 | 日期 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 根据当前配置，没有文件显示。检查下面的配置项，察看未版本控制的、被忽略的或未修改的文件。为了察看远程修改，请点击“检查版本库”。 |  |  |  |  |  |  |  |  |  |

显示项与统计：

- 显示无版本控制的文件（V）
- 显示未修改的文件（M）
- 显示被忽略的文件（G）
- 显示属性（P）
- 最低显示版本：0
- 最高显示版本：0
- 常规＝15，无版本控制＝0，修改＝0，增加＝0，删除＝0，冲突＝0
- 刷新（R）、检查版本库（H）、确定

### 4）版本分枝图

主要作用即是显示分支与合并，可以直观地了解版本变化的过程。下图即为建立一个分支后的分枝图。

![建立分支后的分枝图](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图44.jpg)

### 5）已解决的

如多个用户编辑同一文件后，提交时，系统会自动判断冲突问题，并提示修改、比对，具体会在下一节中讲到。

### 6）更新至版本

即为更新到其中一个已控制的版本。

### 7）SVN 还原

当用户对工作平台的内容进行修改，且未提交至版本库时，可以选择此项，还原已修改的文件。

### 8）清理

当用户进行了一次版本稳定后，可以点击此项，系统将清除多余的文件。

### 9）获取锁定

用户可以对版本库中的文件或文件夹进行锁定，则其他用户暂时无法对该文件或文件夹进行操作。

### 10）解除锁定

与功能 9 对应，即释放锁定，使其他用户可以对文件进行编辑。

### 11）分支/标记

逻辑库的分支操作，常用于建立逻辑基线，下节会详细叙述。

### 12）切换

即切换至不同的分支或主线。

### 13）合并

与功能 11 相对应。

### 14）导出

将版本库中的文件，导出为不受控的文件或文件夹。

### 15）重新定位

即切换至不同版本库。

### 16）增加

如受控文件夹增加新的不受控文件后，可以选择此选项，将此文件添加至受控库。

### 17）创建补丁

当一个分支上的文件进行了修改，就可以进行该操作了。

### 18）应用补丁

与功能 17 相对应，可以将补丁应用于不同的分支/主线，作用并不大，通常采用合并操作。

### 19）属性

上节中所操作的即为该文件夹的属性。可以对文件夹进行权限管理的操作。

### 20）设置

TortoiseSVN 的设置窗口：

![TortoiseSVN 设置窗口](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图45.jpg)

### 21）帮助

TortoiseSVN 的帮助文件。

### 22）关于

关于 TortoiseSVN 的一些信息，如版本、内核版本等。

## 4.5 TortoiseSVN 的基线分支合并

### 4.5.1 基线

基线（Baseline）是软件文档或源码（或其它产出物）的一个稳定版本，它是进一步开发的基础。所以，当基线形成后，项目负责（SCM）的人需要通知相关人员基线已经形成，并且哪儿可以找到这基线了的版本。这个过程可被认为内部的发布。

至于对外的正式发布，更是应当从基线了的版本中发布。

基线是项目储存库中每个工件版本在特定时期的一个“快照”。

它提供一个正式标准，随后的工作基于此标准，并且只有经过授权后才能变更这个标准，建立一个初始基线后，以后每次对其进行的变更都将记录为一个差值，直到建成下一个基线。

参与项目的开发人员将基线所代表的各版本的目录和文件填入他们的工作区。

随着工作的进展，基线将合并自从上次建立基线以来开发人员已经交付的工作。变更一旦并入基线，开发人员就采用新的基线，以与项目中的变更保持同步。调整基线将把集成工作区中的文件并入开发工作区。

在 SVN 中基线通常的手段为物理备份与分支/合并相结合的，下面将详细叙述 TortoiseSVN 的分支与合并。

### 4.5.2 创建分支

选择你要创建分支的文件，右击 TortoiseSVN -> 分支/标记。

![选择“分支/标记”](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图46.jpg)

# Subversion 安装配置及用户手册 V1.0（实验参考资料）

本资料整理自《软件工程（双语）》实验 4 参考资料，涵盖 Subversion 分支合并、冲突处理及 AnkhSvn 插件使用指南。

## 一、分支操作与合并

### 创建新分支

在出现的窗口中填写相应的信息并点击“确定”。

![图 47](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图47.jpg)

默认的目标 URL 将会是你当前工作副本所处的源 URL。你必须给你的分支/标记编辑一个新路径来取代它。如果你忘记了你上一次使用的命名约定，可以用鼠标右键打开版本库浏览器来察看已经存在的版本库结构。

现在你必须选择要复制的源位置。在这里你有三个设置选项：

#### 版本库中的最新版本
新分支直接从仓库中的最新版本里复制出来。不需要从你的工作副本中传输任何数据，这个分支的建立是非常快的。

#### 在版本库中指定具体的版本
在仓库中直接复制建立一个新分支，同时你也可以选择一个旧版本。假如在你上周发布了项目时忘记了做标记，这将非常有用。如果你记不起来版本号，通过点击鼠标右键来显示版本日志，同时从这里选取版本号。和上次一样不需要从你的工作副本中传输任何数据，这个分支建立起来是非常快的。

#### 工作副本
新的分支是一个完全等同于你的本地工作副本的一个副本。如果你更新了一些文件到你的工作副本的某个旧版本里，或者你在本地做出了修改，这些改变将准确无误地进入副本中。自然而然地这种综合的标记会包含正在从工作副本传输到版本库的数据，如果这些数据还不存在的话。

### 合并分支 (Merge Branches)

选择右键菜单 `TortoiseSVN` → `合并...`。

![图 48](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图48.jpg)

在 **从** (From) 域输入文件夹在分支或标记中的完整 URL，它包含了你想应用到工作副本的修改。你也可以点击 `...` 浏览版本库，找到渴望的分支。如果以前已经从这个分支合并过，可以直接从包含历史的下拉列表选择以前使用的 URL。点击“合并”按钮，完成合并。

![图 49](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图49.jpg)

因为要将同一分支的版本范围合并到工作副本，所以要确保使用 **“从”** URL 检查框选中。在 **从版本** 域输入开始版本号。它是在你要执行合并的修改之前的版本号。切记为了合并，Subversion 将会创建一个差异，所以开始点务必准确。

例如，你的日志如下：

| 版本 | 注释 |
| :--- | :--- |
| 39 | Working on MyBranch |
| 38 | Working on trunk |
| 37 | Working on MyBranch |
| 36 | Create branch MyBranch |
| 35 | Working on trunk |
| 34 | Working on trunk |

如果要将 MyBranch 的修改合并到 trunk，应该选择 **36** 作为开始版本，而不是像你想的是 37。如果你选择 37 作为开始点，那么差异引擎将会比较结束点与版本 37 比较，这就丢失了版本 37 做的修改。

如果这听起来很复杂，不要担心，在 TortoiseSVN 中有更简单的方法：选择版本范围最简单的方法是，点击显示日志，列出最近的修改和日志。如果你要合并单个版本的修改，直接选取那个版本。如果你要合并多个版本，就选择范围（使用通常的 Shift 键）。点击确认，就会为你填写合并对话框的全部域，开始版本和结束版本。

当选择了检查框 **使用 “开始”URL**，只有按钮 **显示日志** 可用。这是因为显示日志对话框设置了全部开始和结束版本。所以你只用上面说的多项选择方法即可。

如果你已经从这个分支合并了一些修改，希望你在提交日志中注明最后一个合并的版本号。这时，你可以在工作副本上使用显示日志对话框跟踪日志。使用最后合并的版本号作为本次合并的开始版本。

例如，你已经合并了版本 37 到 39，那么本次合并你应该从版本 39 开始。

如果你没有使用显示日志对话框显示版本范围，那么你需要手工设置结束版本。在范围中输入你想合并的最后一个版本号。这经常是最新版本，尽管它不必是——你只想合并单个版本。如果其他用户可能提交，那么要小心使用最新版本。如果有人在你最近更新之后提交了，它指代的版本可能就不是你想的那样了。

### 合并冲突 (Merge Conflicts)

合并通常很复杂，如果分支与最新版本差别很大，合并经常会出现冲突。发生冲突时文件夹和文件的图标就会带有警告标志，同时会多 `.working` 文件和两个压缩包文件。

![图 50](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图50.jpg)

发生冲突的内容会有标记，你可以打开文件找到以 `<<<<<<<` 开头的行，根据需要修改。格式如下：

```text
<<<<<<<filename
你的修改来自版本库中的代码
>>>>>>> revision
```

也可以通过选中文件右击 `TortoiseSVN` -> `编辑冲突`，进行修改。

![图 51](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图51.jpg)

在比较页面根据需要选择想要的内容，右击在弹出的窗体中选择所需要的，“保存”。

![图 52](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图52.jpg)

这样文件的图标就没有警告符号了，刚才有冲突引起的多余的文件也没有了，这表示冲突已经修改好了，剩下的就是更新了。

![图 53](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图53.jpg)

如果你不信任合并操作，可以在允许它修改你的工作副本之前预览效果。有三个额外的按钮可以帮着你预览：

1.  **预检**：演习运行执行合并操作，但是根本不修改工作副本。它显示在真实的合并中要修改的文件列表，还告诉你哪里会出现冲突。

    | 操作 | 路径 | MIME 类型 |
    | :--- | :--- | :--- |
    | 冲突 | D:\myProjects\project1\trunk\1.txt | - |

2.  **比较差异**：创建差异文件（切记合并基于差异），显示你的工作目录哪些行将要被修改。因为这是统一差异（补丁）文件，所以离开上下文，它经常很难读。但是对于小的修改，由于它将所有修改在一起显示，因此很有用。

3.  **准差异**：差异显示修改文件列表。双击任一文件启动差异察看器。不像比较差异，它显示具有前后关系的详细修改信息。像比较差异那样，你看到的是开始版本和结束版本之间的差异。它不显示应用此改变之后，你的工作版本如何改变。

## 二、客户端使用说明——AnkhSvn

本章主要介绍了 Subversion 中 VS.net 2005&2008 插件 AnkhSvn 的使用方法。

AnkhSvn 是最常用的 VS.net 2005&2008 插件，其有效的集成于 VS.net 2005&2008 中，作为 Subversion 的辅助，增加了其使用的方便性，虽然版本为英文，但由于与 AnkhSvn 操作类似，上手并不存在困难。

### 初始化导入

对于 Subversion 来讲，服务端进行配置后，版本库第一次运行，会由项目经理进行第一次的导入操作。

1) 打开 Microsoft Visual Studio 2005&2008 -> 打开一个项目，在右侧解决方案资源管理器中选择所要导入的项目，点击鼠标右键。如需导入整个解决方案，则选择 `Add Solution to Subversion`；如导入单个项目，则选择 `Add Selected Projects to Subversion`。

**解决方案资源管理器右键菜单：**

| 菜单项 |
| :--- |
| 生成解决方案 (B) |
| 重新生成解决方案 (R) |
| 清理解决方案 (C) |
| 批生成 (T)... |
| 配置管理器 (O)... |
| 项目依赖项 (S)... |
| 项目生成顺序 (I)... |
| 添加 (D) |
| 设置启动项目 (A)... |
| Add Solution to Subversion... |
| Add Selected Projects to Subversion... |
| Subversion |
| 粘贴 (P) |
| 重命名 (M) |
| 属性 (R) |

2) Repository Url 输入 `svn://192.168.70.50/`，点击 Create 按钮，建立项目文件夹（此处版本库 URL 为 Subversion 服务端 IP 地址），点击确定。

![图 54](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图54.jpg)

**Add to Subversion 对话框内容：**

*   **Project Name:** ZedGraph
*   **Repository Path:** svn://192.168.70.50/test/
*   **Local Folder:** D:\My Documents\Downloads\zedgraph\_v5.0.9
*   **Options:** Add trunk Folder for Project
*   **Project will be created in:** svn://192.168.70.50/test/ZedGraph/

3) 点击 OK，弹出填写日志项。

![图 55](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图55.jpg)

界面下侧出现如下提示框，点击 Commit，进行提交。已添加成功后，此窗体内容自动清空。至此初始的数据就已经全部导入到了我们刚才定义的版本库中。

### SVN 检出

该操作可以将 SVN 服务端所保存的数据下载至个人工作平台，通常用于第一次链接该版本库。

来到我们想要导入的项目根目录，在这个例子里是 `D:\test`，该目录为空目录：

1) 打开 Microsoft Visual Studio 2005&2008 -> 文件 -> Subversion -> Open from Subversion..

![图 56](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图56.jpg)

2) 点击添加 Url，输入 Subversion 服务地址 `svn://192.168.70.50/`，添加完成后，选择需要检出的文件版本，点击 OK 进行检出。（此处版本库 URL 为 Subversion 服务端 IP 地址；检出至目录为 `d:\test`），点击确定。

![图 57](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图57.jpg)

通常情况下为最新版本，如需要其他版本，点击 Type 进行选择。

![图 58](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图58.jpg)

### 工作平台中文件的修改及版本库的提交

下面以修改代码内容为例进行演示。

## 5.4 AnkhSvn 的常规功能说明

### 常用功能 1

本节主要叙述 AnkhSvn 中的一些常规功能，在已打开的项目上点击右键→Subversion，具体如下图所示：

| 项目 |
| --- |
| 解决方案“ZedGraphSample”(1 个项目) |
| ZedGraphSample |
| 刷新(F) |
| 生成(U) |
| 重新生成(E) |
| 清理(N) |
| 发布(B)... |
| 添加(D) |
| 添加引用(R)... |
| 添加 Web 引用(E)... |
| 查看类关系图(V) |
| 设为启动项目(A) |
| 调试(G) |
| Update to Latest Version |
| View Project History |
| Subversion |
| Project File |
| 剪切(T) |
| 粘贴(P) |
| 移除(V) |
| 重命名(M) |
| 卸载项目(L) |
| 属性(R) |

### 1）Update to Specific Version 更新至版本…

该功能主要功能为更新工作平台中特定版本已变更的内容，默认为最新版本。

![更新至版本](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图59.jpg)

### 2）Lock 锁定

用户可以对版本库中的文件或文件夹进行锁定，则其他用户暂时无法对该文件或文件夹进行操作。锁定后，图标自动变为解锁。

### 3）Compare 比较差异

对选定的文件及版本进行比较差异。

![比较差异](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图60.jpg)

### 4）Unified Diff 合并差异

对代码间的差异进行合并。

![合并差异](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图61.jpg)

### 5）Annotate 追溯

追溯文件至一历史版本。

![追溯](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图62.jpg)

### 6）Subversion Properties Subversion 属性

该代码的文件夹的 Subversion 属性。可以对文件夹进行权限管理的操作。

![Subversion 属性](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图63.jpg)

### 7）Branch Project 分支

逻辑库的分支操作，常用于建立逻辑基线。

Log Message:

![分支](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图64.jpg)

### 8）Switch Project 切换

即切换至不同的分支或主线。

![切换](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图65.jpg)

### 9）Merge Project 合并

与功能 7 相对应。

![合并](软件工程双语实验4参考资料：Subversion安装配置及用户手册V1.0.assets/图66.jpg)

当用户进行了一次版本稳定后，可以点击此项，系统将清除多余的文件。

### 11）Refresh Status 更新版本

更新为版本库中已变更的版本。

### 常用功能 2

本节主要叙述 AnkhSvn 中的一些常规功能，在已打开的项目上点击右键→Project Files，具体如下图所示：

| 项目 |
| --- |
| 解决方案资源管理器 - ZedGraphSample |
| 解决方案“ZedGraphSample” (1 个项目) |
| ZedG |
| 刷新(F) |
| 生成(U) |
| 重新生成(E) |
| 清理(N) |
| 发布(B)... |
| 添加(D) |
| 添加引用(R)... |
| 添加 Web 引用(E)... |
| 查看类关系图(V) |
| 设为启动项目(A) |
| 调试(G) |
| Update to Latest Version |
| View Project History |
| Subversion |
| Project File |
| 剪切(T) |
| 粘贴(P) |
| 移除(V) |
| 重命名(M) |
| 卸载项目(L) |
| 属性(R) |

基本与前一小节所述相同，但面向的对象为项目文件，其中 View History 为浏览版本历史。

## 第六章 注意事项

本章主要介绍了 Subversion 的一些注意事项。

### 版本号的解释

SVN 系统中的版本号准确应该叫做“修订版本号”，每当版本库接受了一个提交，文件系统进入了一个新的状态，叫做一次修订（revision），每一个修订版本被赋予一个独一无二的、递增的自然数，这个自然数就是修订版本号。

受控项目中任何一个受控文件/文件夹进行了修改提交操作，项目的版本号就会提升一次，没有进行修改的文件/文件夹其版本号不会发生变化。受控项目每一个状态都包含项目的所有文件/文件夹，引起该次版本号增加的即修改了的文件/文件夹保存新副本，没有发生修改的文件/文件夹保存引用，因此项目中的文件/文件夹可能与项目的版本号不同。
