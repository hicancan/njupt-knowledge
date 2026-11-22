---
title: 《Java程序设计》课后编程练习第1次作业
kind: 习题
course: Java软件开发
term: 2020-2021-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0302281C%E3%80%91JAVA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/Course%20Materials%20%5B2020-2021-2%5D/01%20Lectures%20Assignment/JAVA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E7%AC%AC1%E6%AC%A1%E4%BD%9C%E4%B8%9A.pdf
---


# 《Java程序设计》课后编程练习第1次作业

本文按南京邮电大学计算机学院 2021 年 2 月作业原件整理。两项练习的目标来自原件；下面的验证方法和故障定位是整理者补写。提交说明只对应 2020—2021 学年第二学期。

相关知识点：[HelloWorld 程序结构](../../../topics/Java开发/HelloWorld程序结构.md)，[Java 平台与 JVM](../../../topics/Java开发/Java平台与JVM.md)。

## 练习 1：让第一个程序真正跑起来

原件要求准备 JDK 和 NetBeans，新建 Java 项目，创建 `HelloWorldApp.java`，编译出字节码，再运行并查看输出。原件使用默认包，本例也不写 `package`。即使项目用其他名称，运行的入口仍然是 Java 类，不是项目名称。

**参考解答**

```java
public class HelloWorldApp {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

在源文件目录可以用命令行独立检查，不依赖 NetBeans 的菜单版本：

```sh
mkdir out
javac -d out HelloWorldApp.java
java -cp out HelloWorldApp
```

预期输出是一行 `Hello World!`。编译器读取的是源文件，所以给它 `HelloWorldApp.java`；第三行用 JVM 启动已经编译的类，所以给类名 `HelloWorldApp`，不要带 `.class` 后缀。

## 练习 2：区分保存、编译、构建和运行

原件要求在磁盘找到源文件与编译结果，再观察项目完整构建前后的变化；命令行运行是选做项。若 NetBeans 项目属性提供「在保存时编译」，可以按原件暂时关闭它，看清保存和手动编译各自产生什么。

```mermaid
flowchart LR
  S["保存源文件：HelloWorldApp.java"]
  C["编译：HelloWorldApp.class"]
  B["构建：按项目配置打包"]
  R["运行：查找入口 main"]
  S --> C
  C --> B
  C --> R
  B -->|"若生成可执行 JAR"| R
```

**参考解答**　记录文件路径和内容变化，比记菜单或固定目录更可靠。老式 NetBeans 普通 Java 项目常见 `src/`、`build/classes/` 和 `dist/`；使用别的构建方式时，产物也可能位于 `target/` 或 `build/`。不是每种项目都会生成可直接启动的 JAR。对照观察时先保留旧输出，再重新编译，最后重新运行：

| 操作 | 可核验的证据 | 尚不能说明什么 |
|---|---|---|
| 保存源文件 | 磁盘上的 `.java` 内容已更新 | 字节码未必已更新 |
| 独立编译 | 生成 `HelloWorldApp.class` | 程序尚未运行，也未必构建了分发包 |
| 构建项目 | 运行该项目的构建目标，查看日志与输出目录 | 生成的 JAR 不一定声明了入口 |
| 运行 | 输出窗口出现当前入口类的预期文本 | 输出正确不等于已经生成分发包 |

> [!TIP]
> 看到==源文件已改但运行还在打印旧文本==，先用明确的输出目录重新编译，再用 `-cp out` 启动对应类；若重新编译前后的输出不同，就是磁盘上的旧字节码仍在被运行。

> [!WARNING]
> 如果能找到 `.class` 却提示无法找到主类，优先检查当前目录、类路径根和类名。若后来给程序加了包，入口也要同步改成完整类名；单纯把 `.class` 移到任意目录不能修复包名与位置不匹配的问题。

**补充**　若构建产物是明确设了入口的 JAR，可以用 `java -jar <产物.jar>` 验证；若报缺少主清单属性，检查构建中是否配置了 `Main-Class`，不要把这个错误误判为源码无法编译。

## 当年的提交要求

原件只要求提交练习 1 的运行截图（JPG 或 PNG），不提交练习 2；提交窗口示例同时显示源代码编辑区和输出窗口，以便确认运行的是哪个类。原件要求截图名包含学号、姓名和作业序号，且在课程指定的群文件夹提交。原件所列截止时间为 2021 年 3 月 3 日，不是现行通知。
