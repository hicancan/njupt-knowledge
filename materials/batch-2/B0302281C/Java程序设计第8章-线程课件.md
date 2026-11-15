---
title: 《Java程序设计》第8章 线程（课件）
kind: 课件
course: Java软件开发
source: batch-2:JAVA/Java课件（建设中）.zip/8-Java程序设计课件（朱艳梅）.ppt
---

# 《Java程序设计》第8章 线程（课件）

原件的每一页，下面附识别出的文字。

### Java 程序设计Java Programming

![第 1 页](Java程序设计第8章-线程课件.assets/第1页.webp)

原文：

Java 程序设计Java Programming

南京邮电大学Java程序设计课程组心川

教材：《Java程序设计》，北京邮电大学出版社，2016年出版

南京鐵電大學 南京郵電大学 Nanjing University of Posts and Telecommunications

### 第8章 线程

![第 2 页](Java程序设计第8章-线程课件.assets/第2页.webp)

原文：

第8章 线程

➢ 一般来说，一个应用程序只有一条执行路径。对于Java的Application程序，其执行路径从main()方法开始的。

在实际应用中，经常需要一个程序同时执行多个任务，要求一个程序同时有多条执行路径。比如，一个执行复杂计算功能的应用程序，在执行计算的同时还需要监视用户在界面中的操作。由此引出java的多线程问题。

### 8.1 理解线程

![第 3 页](Java程序设计第8章-线程课件.assets/第3页.webp)

原文：

8.1 理解线程

8.1.1 进程的概念

8.1.2 线程的概念

➢ 8.1.3 线程的生命周期

### 8.1.1 进程的概念

![第 4 页](Java程序设计第8章-线程课件.assets/第4页.webp)

原文：

8.1.1 进程的概念

➢程序是一段静态的代码，进程是程序的一次

动态执行过程，它对应从代码加载、执行到

执行完毕的一个完整过程，Windows任务管

理器里的每一条都是一个进程。一个程序运

行后，会在内存里产生一个进程。

### 8.1.2 线程的概念

![第 5 页](Java程序设计第8章-线程课件.assets/第5页.webp)

原文：

8.1.2 线程的概念

➢线程是比进程更小的执行单位

线程是进程的组成部分

➢ 一个进程在执行过程中可以产生多个线程

➢ 每个线程有自身产生存在和消亡的过程

➢线程是系统分配处理器时间资源的基本单元

### 8.1.3 线程的生命周期

![第 6 页](Java程序设计第8章-线程课件.assets/第6页.webp)

原文：

8.1.3 线程的生命周期

➢ 1. 产生（spawn）

➢ 2. 中断（block）

➢ 3. 非中断（unblock）

4. 退出（finish）

### 8.2 线程类设计

![第 7 页](Java程序设计第8章-线程课件.assets/第7页.webp)

原文：

8.2 线程类设计

➢ 8.2.1 线程API类图

➢ 8.2.2 线程类Thread的构造方法

### 8.2.1 线程API类图

![第 8 页](Java程序设计第8章-线程课件.assets/第8页.webp)

原文：

8.2.1 线程API类图

Thread.State

StackTraceElement (from lang)

Thread.UnCaughtExceptionHandler

### 8.2.2 线程类Thread的构造方法

![第 9 页](Java程序设计第8章-线程课件.assets/第9页.webp)

原文：

8.2.2 线程类Thread的构造方法

➢ 1. Thread(String threadName)：

创建一个线程类的对象并为其指定一个字符串名称。

➢ 2. Thread()：

创建一个线程类的对象，其名称由系统自动指定为“Thread-”连接一个数值，例如“Thread-1” “Thread-2”。。 。

➢ 3. Thread(Runnable target)：

### 8.3 线程实现

![第 10 页](Java程序设计第8章-线程课件.assets/第10页.webp)

原文：

8.3 线程实现
▶ 8.3.1 继承实现
▶ 8.3.2 接口实现

### 8.3.1 继承Thread类实现线程

![第 11 页](Java程序设计第8章-线程课件.assets/第11页.webp)

原文：

8.3.1 继承Thread类实现线程

public class ThreadDemo extends Thread{ public void run(){ //线程代码实现 System.out.println("线程执行");

static public void main(String[] args){ ThreadDemo th=new ThreadDemo(); th.start();

### 8.3.2 实现Runnable接口实现线程

![第 12 页](Java程序设计第8章-线程课件.assets/第12页.webp)

原文：

8.3.2 实现Runnable接口实现线程

public class ThreadDemo{ static public void main(String[] args){ Thread th=new Thread(new MyThImpl()); th.start();

class MyThImpl implements Runnable{ public void run(){ //线程代码实现 System.out.println("线程执行");

### 8.4 线程控制

![第 13 页](Java程序设计第8章-线程课件.assets/第13页.webp)

原文：

8.4 线程控制
▶ 8.4.1 监控线程状态
▶ 8.4.2 线程睡眠
▶ 8.4.3 中断线程
▶ 8.4.4 阻塞线程
▶ 8.4.5 线程等待和唤醒
▶ 8.4.6 线程终止

### 8.4.1 监控线程状态

![第 14 页](Java程序设计第8章-线程课件.assets/第14页.webp)

原文：

8.4.1 监控线程状态

NEW：

⚫ 线程对象创建，还没有调用start之前的状态

RUNNABLE：线程执行时候的状态，即run中代码被执行的状态

BLOCKED：⚫ 线程被阻塞等待一个解锁时候的状态。

WAITING：⚫ 另外一个线程在执行，本线程会处于等待状态。

TERMINATED：线程退出run的状态

### 8.4.2 线程睡眠

![第 15 页](Java程序设计第8章-线程课件.assets/第15页.webp)

原文：

8.4.2 线程睡眠

使主线程每休眠100毫秒，然后再输出数字。 public class ThreadTest1 { public static void main(String[] args) throws InterruptedException { for(int i=0;i<20;i++){ System.out.println("main"+i); Thread.sleep(100);

### 8.4.3 中断线程

![第 16 页](Java程序设计第8章-线程课件.assets/第16页.webp)

原文：

8.4.3 中断线程

线程中断调用interrupt()方法，具体原型为：

public void interrupt()：线程中断时中断当前的阻塞与等待状态，并强制线程抛出异常。

➢ 一般在wait()、sleep()、join()等方法导致线程阻塞的时候调用。

### 8.4.4 阻塞线程

![第 17 页](Java程序设计第8章-线程课件.assets/第17页.webp)

原文：

8.4.4 阻塞线程

void join(long millis)：

⚫ 当前线程等待该线程终止的时间最长为millis毫秒。如果在millis时间内，该线程没有执行完，那么当前线程进入就绪状态，重新等待CPU调度。

### 8.4.5 线程等待和唤醒

![第 18 页](Java程序设计第8章-线程课件.assets/第18页.webp)

原文：

8.4.5 线程等待和唤醒

➢ public final void wait(long timeout,int nanos)

void notify()

➢ void notifyAll()

### 8.4.6 线程终止

![第 19 页](Java程序设计第8章-线程课件.assets/第19页.webp)

原文：

8.4.6 线程终止

线程终止是指当前线程放弃调度执行权力，等待下次排队执行。其并不是线程结束，也不是线程等待。

➢ public static void yield()

### 【例8-2】线程控制的综合实例

![第 20 页](Java程序设计第8章-线程课件.assets/第20页.webp)

原文：

【例8-2】线程控制的综合实例

import java.util.Scanner; public class ThreadTest2 { private static int data = -1; private static Thread thread = new Thread(new Runnable() { public void run() { System.out.println("线程已经启动...输入0，则

计数开始！");

for(int i=10;i>0;i--){ while(data != 0){ Thread.yield();

System.out.println(Thread.currentThread().getName()+":"+i); try {Thread.sleep(100); } catch (InterruptedException e) { e.printStackTrace();

### 第 21 页

![第 21 页](Java程序设计第8章-线程课件.assets/第21页.webp)

### 第 22 页

![第 22 页](Java程序设计第8章-线程课件.assets/第22页.webp)

原文：

线程已经启动..输入0，则计数开始 0 Thread-0:10 Thread-0:9 Thread-0:8 Thread-0:7 Thread-0:6 Thread-0:5 Thread-0:4 Thread-0:3 Thread-0:2 Thread-0:1 Press any key to continue.

### 8.5 线程属性

![第 23 页](Java程序设计第8章-线程课件.assets/第23页.webp)

原文：

8.5 线程属性
▶ 8.5.1 优先级属性
▶ 8.5.2 守护线程

### 8.5.1 优先级属性

![第 24 页](Java程序设计第8章-线程课件.assets/第24页.webp)

原文：

8.5.1 优先级属性

优先级高的线程可以获得较多的执行机会，而优先级低的线程则获得较少的执行机会。

Thread类提供了setPriority(int newPriority)和getPriority()方法来设置和返回一个指定线程的优先级

⚫ setPriority方法的参数是一个整数，范围是1-10之间。

➢ 也可以使用Thread类提供的三个静态常量：

MAX\_PRIORITY=10

MIN\_PRIORITY=1

NORM\_PRIORITY=5

### 8.5.2 守护线程

![第 25 页](Java程序设计第8章-线程课件.assets/第25页.webp)

原文：

8.5.2 守护线程

Daemon Thread(守护线程)

守护线程具有最低的优先级，用于为系统中的其它对象和线程提供服务。

### 线程同步

![第 26 页](Java程序设计第8章-线程课件.assets/第26页.webp)

原文：

线程同步

多个线程的调度会导致一些严重的问题，尤其是对用户数据的访问上，会导致数据不一致。可能一个线程刚把a++执行完，另外一个线程就被调度执行，还从a++执行，这样导致a的值产生了两次自加操作，从而影响了第一个线程中对于a的值的预期。要解决这个问题的根本：就是保证某个线程一定要执行完某段代码，其他线程才能被调度执行。这种保护某段代码只能同时被一个线程执行的技术称为线程同步。

### 8.6 线程同步

![第 27 页](Java程序设计第8章-线程课件.assets/第27页.webp)

原文：

8.6 线程同步

➢ 8.6.1 Synchronized同步方法和同步代码块

➢ 8.6.2 同步变量volatile关键字

➢ 8.6.3 线程锁Lock接口及ReentrantLock类

➢ 8.6.4 死锁

➢ 8.6.5 测试锁

➢ 8.6.6 读写锁ReadWriteLock

### 8.6.1 Synchronized同步方法和同步代码块

![第 28 页](Java程序设计第8章-线程课件.assets/第28页.webp)

原文：

8.6.1 Synchronized同步方法和同步代码块

关键字synchronized是Java内部实现的一个简单锁，可以使用synchronized关键字锁定一段代码：

⚫ public static void biz(){

synchronized(Object.class){

//锁定代码段

a++;

b++;

if(a!=b){

System.out.println(a+"!="+b); }}}

### 8.6.2 同步变量volatile关键字

![第 29 页](Java程序设计第8章-线程课件.assets/第29页.webp)

原文：

8.6.2 同步变量volatile关键字

➢ Java中变量前面可以加个修饰语volatile

，关键字volatile引入的主要目的是解决成

员变量的多线程访问同步的问题。

### 8.6.3 线程锁Lock接口及 ReentrantLock类

![第 30 页](Java程序设计第8章-线程课件.assets/第30页.webp)

原文：

8.6.3 线程锁Lock接口及 ReentrantLock类

➢ Lock接口包含的方法有：

void lock()

void lockInterruptibly()线程被Interrupt

//加锁

//加锁直到

Condition newCondition() //返回与所绑定的条件

boolean tryLock()

//测试锁

⚫ boolean tryLock(long time, TimeUnit unit)

void unlock()

//释放锁

### 8.6.4 死锁

![第 31 页](Java程序设计第8章-线程课件.assets/第31页.webp)

原文：

8.6.4 死锁

Java线程死锁是一个经典的多线程问题，因为不同的线程都在等待那些根本不可能被释放的锁，从而导致所有的工作都无法完成。

### 【例8-6】死锁问题说明

![第 32 页](Java程序设计第8章-线程课件.assets/第32页.webp)

原文：

【例8-6】死锁问题说明

public void method2() {

synchronized(lkObj2) {

synchronized(lkObj1) {

m\_b++;

System.out.println("method2:"+m\_b);

### DeadLocker();

![第 33 页](Java程序设计第8章-线程课件.assets/第33页.webp)

原文：

// 两个线程分别调用method1与method2就容易导致死锁。 public class ThreadDeadLockTest{ public static DeadLocker locker=new

DeadLocker();

public static void main(String[] args)throws

Exception{

new ThreadOne().start(); new ThreadTwo().start();

class ThreadOne extends Thread{//负责向 amount添加数据 public void run(){ while(true){ //try{Thread.sleep(10);}catch(Exception e){} ThreadDeadLockTest.locker.method1(); }

class ThreadTwo extends Thread{ public void run(){ while(true){ //try{Thread.sleep(10);}catch(Exception e){} ThreadDeadLockTest.locker.method2(); } }

### 8.6.5 测试锁

![第 34 页](Java程序设计第8章-线程课件.assets/第34页.webp)

原文：

8.6.5 测试锁

➢在Lock接口中提供的方法

⚫ boolean tryLock()

⚫ boolean tryLock(long time, TimeUnit unit)

### 8.6.6 读写锁ReadWriteLock

![第 35 页](Java程序设计第8章-线程课件.assets/第35页.webp)

原文：

8.6.6 读写锁ReadWriteLock

读操作可以多线程并发操作，写操作不能并发操作，读/写不能并发操作。就是写/写是互斥的，读/写是互斥的，但读/读不互斥。

➢ 类ReentrantReadWriteLock的方法：

⚫ ReentrantReadWriteLock.ReadLock readLock()

⚫ ReentrantReadWriteLock.WriteLock writeLock()
