---
name: Linux编程
codes: [JS113701S]
former: [B0301371S]
---

# Linux编程

南京邮电大学《Linux编程》。章节和知识点由课件、历年复习提纲整理。

## 第1章 Linux系统概述与开发环境

- [Linux操作系统的特点与体系结构](../topics/Linux系统编程/Linux系统特点.md)
- [GCC编译器的使用与编译过程（预处理、编译、汇编、链接）](../topics/Linux系统编程/GCC编译器.md)
- [GDB调试器的基本命令与断点调试](../topics/Linux系统编程/GDB调试器.md)
- [Makefile的语法规则与make工具的使用](../topics/Linux系统编程/Makefile编写.md)

## 第2章 文件I/O编程

- [文件描述符的概念与标准输入输出错误（0、1、2）](../topics/Linux系统编程/文件描述符.md)
- [系统调用与C库函数的区别与联系](../topics/Linux系统编程/系统调用与库函数.md)
- [文件的打开open()与关闭close()系统调用](../topics/Linux系统编程/open和close.md)
- [文件的读写read()与write()系统调用](../topics/Linux系统编程/read和write.md)
- [文件偏移量设置lseek()系统调用](../topics/Linux系统编程/lseek定位.md)
- [文件访问权限与umask掩码](../topics/Linux系统编程/文件访问权限.md)
- [文件控制fcntl()函数（文件描述符复制、状态标志修改等）](../topics/Linux系统编程/fcntl函数.md)
- [I/O多路复用select()函数的使用](../topics/Linux系统编程/select多路复用.md)

## 第3章 进程控制与进程间通信

- [进程的概念、状态转换与PCB（进程控制块）](../topics/Linux系统编程/进程概念.md)
- [fork()系统调用创建子进程及其返回值](../topics/Linux系统编程/fork创建进程.md)
- [exec函数族替换进程映像](../topics/Linux系统编程/exec函数族.md)
- [wait()与waitpid()回收子进程及僵尸进程](../topics/Linux系统编程/wait和waitpid.md)
- [exit()库函数与_exit()系统调用的区别](../topics/Linux系统编程/exit和_exit.md)
- [无名管道pipe()的创建与半双工通信](../topics/Linux系统编程/无名管道pipe.md)
- [有名管道FIFO的创建与无亲缘关系进程通信](../topics/Linux系统编程/有名管道FIFO.md)
- [信号的概念、常用信号类型及signal()处理](../topics/Linux系统编程/信号机制.md)
- [sigaction()函数进行可靠的信号处理](../topics/Linux系统编程/sigaction函数.md)
- [信号集操作函数（sigemptyset、sigaddset）与信号屏蔽](../topics/Linux系统编程/信号集操作.md)

## 第4章 多线程编程

- [线程的概念及与进程的区别](../topics/Linux系统编程/线程概念.md)
- [pthread_create()创建线程与pthread_exit()终止线程](../topics/Linux系统编程/线程创建与终止.md)
- [pthread_join()阻塞等待线程结束并回收资源](../topics/Linux系统编程/线程等待.md)
- [互斥锁pthread_mutex_t的初始化、加锁与解锁](../topics/Linux系统编程/互斥锁.md)
- [条件变量pthread_cond_t的等待wait与通知signal/broadcast](../topics/Linux系统编程/条件变量.md)
- [线程属性设置与分离状态（detachstate）](../topics/Linux系统编程/线程属性.md)

## 第5章 网络编程

- [套接字Socket的概念与地址结构sockaddr_in](../topics/Linux系统编程/Socket概念.md)
- [TCP面向连接的客户端/服务器通信流程（socket、bind、listen、accept、connect）](../topics/Linux系统编程/TCP通信流程.md)
- [UDP无连接的客户端/服务器通信流程（sendto、recvfrom）](../topics/Linux系统编程/UDP通信流程.md)
- [网络字节序与主机字节序及转换函数（htonl、htons、inet_pton等）](../topics/Linux系统编程/字节序转换.md)
- [并发服务器的实现模型（多进程、多线程）](../topics/Linux系统编程/并发服务器.md)

## 第6章 System V IPC进程间通信

- [System V IPC的键值key与ftok()函数](../topics/Linux系统编程/IPC键值.md)
- [消息队列的创建msgget、发送msgsnd、接收msgrcv与控制msgctl](../topics/Linux系统编程/消息队列.md)
- [共享内存的创建shmget、映射shmat、脱离shmdt与控制shmctl](../topics/Linux系统编程/共享内存.md)
- [System V信号量集的创建semget、操作semop与控制semctl（PV操作）](../topics/Linux系统编程/信号量集.md)

## 第7章 Linux设备驱动编程基础

- [字符设备、块设备与网络设备文件的分类与主次设备号](../topics/Linux系统编程/设备文件分类.md)
- [内核模块的编写、insmod加载与rmmod卸载](../topics/Linux系统编程/模块加载卸载.md)
- [file_operations结构体与设备驱动接口注册](../topics/Linux系统编程/file_operations.md)

