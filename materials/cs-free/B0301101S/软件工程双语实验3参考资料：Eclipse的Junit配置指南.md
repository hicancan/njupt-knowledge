---
title: 《软件工程（双语）》实验3参考资料：Eclipse的Junit配置指南
kind: 实验
course: 软件工程（双语）
source: cs-free:【B0301101S】软件工程（双语）/实验/软件工程（双语）-实验要求-24-25-2.7z/实验3参考资料/参考3 Eclipse的Junit配置.pdf
---

# 《软件工程（双语）》实验3参考资料：Eclipse的Junit配置指南

原件经识别和整理；“参考解答”是我们补的。

# Eclipse 的 Junit 配置指南

## 一、Eclipse 中 JUnit 的配置

### 1.1 创建变量 JUNIT 和 JUNIT_SRC

在 project 的 classpath 中添加 junit.jar。因此，建立一个新的 classpath 变量 `JUNIT`。选择 **Window -> Preferences** 菜单栏打开 Preferences 对话框，如图 1.1所示。展开 Java 结点，选择 **Build Path -> Classpath Variables** 项，如图 1.2 所示。

![图 1.1 Preferences 对话框](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图1.jpg)

![图 1.2 Classpath Variables 窗口](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图2.jpg)

然后点击 **New** 按钮打开 New Variable Entry 菜单，如图 1.3 所示。输入新的变量名：`JUNIT`，配置路径为 `junit.jar`。在 Eclipse 3.0.2 中，能够在 `/eclipse/plugins/org.junit_3.8.1/junit.jar` 下找到 `junit.jar`。然后点击 OK，如图 1.4 所示。

![图 1.3 New Variable Entry 对话框](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图3.jpg)

![图 1.4 创建 JUNIT 变量](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图4.jpg)

为了 debug 的需要，也要添加 JUnit 包的源代码。您将在 `/eclipse/plugins/org.eclipse.jdt.source_3.0.2/src` 目录中发现许多包的源代码的 JAR 文档。为 JUnit 源代码创建一个新的变量，按照上面创建 `JUNIT` 的步骤，但是此变量名为 `JUNIT_SRC`（通常在源代码变量前面添加前缀 `_SRC`）并且将他连接到 `/eclipse/plugins/org.eclipse.jdt.source_3.0.2/src/org.junit_3.8.1/junitsrc.zip`，如图 1.5 所示。

![图 1.5 创建 JUNIT_SRC 变量](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图5.jpg)

单击 OK 命令按钮，这样两个环境变量就创建完成，我们可以看见 `JUNIT` 和 `JUNIT_SRC` 两个变量，如图 1.6 所示。

![图 1.6 创建变量后的 Classpath Variables 窗口](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图6.jpg)

## 二、创建 JUnit 测试

### 2.1 创建 java 项目

新建一个 java 项目，点击 **File -> New -> Project**，选择 Java Project 项目，点击 Next，为项目起一个名称，例如 Student，如图 2.1 所示。

![图 2.1 创建 Student 项目](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图7.jpg)

创建 Student 类，右键单击 Student 这个项目名称，在快捷菜单中选择 **New -> Class**，在窗口中 Package 填入 `com.student`，Name 填入 `Student`，如图 2.2 所示。

![图 2.2 创建 Student 类](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图8.jpg)

### 2.2 建立 JUnit 测试

在创建 JUnit 测试之前一定要先导入 `junit.jar` 包。在 project “Student”上单击鼠标右键，选择 **Properties**，如图 2.3 所示。

![图 2.3 Properties 命令菜单](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图9.jpg)

然后打开 Properties for Student 的属性对话框，点击 **Java Build Path** 项和 **Libraries** 选项，如图 2.4 所示。

![图 2.4 Properties for Student 对话框](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图10.jpg)

再点击 **Add Variable** 命令按钮，进入 New Variable Classpath Entry 窗口，选择 `JUNIT` 变量，如图 2.5 所示。

![图 2.5 添加 JUNIT 变量](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图11.jpg)

点击 OK 命令按钮，完成 `JUNIT` 变量的添加。当我们展开一个 `JUNIT` 变量结点的时候，能够指定在何处寻找相关联的源代码和 Javadoc，如图 2.6 所示。

![图 2.6 展开后的 JUNIT 节点](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图12.jpg)

为了 JUnit 能使用其源代码，我们需要添加 JUnit 的源代码，也就是 `JUNIT_SRC` 变量，选择结点中的 Source attachment，再单击 edit 打开 Source Attachment Configuration 对话框，如图 2.7 所示。

![图 2.7 Source Attachment Configuration 对话框](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图13.jpg)

然后点击 **Variable** 按钮，如图 2.8 所示。再选择 `JUNIT_SRC` 变量，并点击 OK 关闭此对话框，如图 2.9 所示。

![图 2.8 Variable Selection 对话框](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图14.jpg)

![图 2.9 添加 JUNIT_SRC 变量](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图15.jpg)

这里我们已使 JUnit 的源代码能在 Eclipse 上使用。点击 OK 关闭 Student 的属性对话框。

现在我们可以看见在工程栏目中 Student 项目里已经有 `JUNIT` 这样一个结点，如图 2.10 所示。

![图 2.10 Student 工程项目](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图16.jpg)

### 2.3 创建 StudentTest 单元测试

为 Student 类创建 JUnit 测试。在左侧工程导航栏，右键单击 `Student.java`，在快捷菜单中选择 **New -> JUnit Test Case**，如图 2.11 所示。进入 New JUnit Test Case 窗口，如图 2.12 所示。

![图 2.11 选中的 JUnit Test Case 菜单命令](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图17.jpg)

![图 2.12 New JUnit Test Case 窗口](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图18.jpg)

在 New JUnit Test Case 窗口，选择我们需要的参数，然后点击 Next，在弹出窗口中选择自己需要测试的方法，再点击 Finish，如图 2.13 所示。

![图 2.13 选择测试的方法](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图19.jpg)

然后点击 Finish 命令按钮，这样我们 `StudentTest.java` 文件就创建完成了。我们现在可以为这个 testMain 方法添加相应的代码，再运行这个 JUnit 测试。右键单击 `StudentTest.java`，在快捷菜单中选择 **Run as -> JUnit Test**，如图 2.14 所示。这样我们就可以在左侧的 JUnit 窗口查看测试结果，如图 2.15 所示。

![图 2.14 运行 JUnit 测试](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图20.jpg)

![图 2.15 JUnit 测试 GUI 窗口](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图21.jpg)

### 注意：

如果运行 JUnit 测试之后但是没有出现 JUnit 测试 GUI 窗口，我们还要进行一些别的设置。选择 **Window -> Show View -> Other**，如图 2.16 所示。

![图 2.16 调出 JUnit 测试 GUI](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图22.jpg)

在 Show View 窗口，展开 java 结点，选择 **JUnit**，如图 2.17 所示。

![图 2.17 Show View 窗口](软件工程双语实验3参考资料：Eclipse的Junit配置指南.assets/图23.jpg)

最后单击 OK 命令按钮，我们就可以在左侧的窗口看见 JUnit 测试 GUI 窗口了。
