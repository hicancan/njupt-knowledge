---
title: 《Web技术（双语）》Part 7 数据库访问（课件）
kind: 课件
course: Web技术（双语）
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/PPT_hjy%E5%BD%95%E9%9F%B3%E7%89%88/part7-database-voice.pptx
---

# 《Web技术（双语）》Part 7 数据库访问（课件）

原件的每一页，下面附识别出的文字。

### Part 7

![第 1 页](Web技术双语Part-7-数据库访问课件.assets/第1页.webp)

原文：

Part 7

Database Access Through the Web

PEARSON Addison Wesley

Programming the world wide web

### • 13.1 Relational databases

![第 2 页](Web技术双语Part-7-数据库访问课件.assets/第2页.webp)

原文：

• 13.1 Relational databases
• 13.2 Structured Query Language(SQL)
• 13.3 Architectures for database access
• 13.4 The MySQL database
• 13.5 Database access with PHP and MySQL Programming the world wide web

Contents

13-2

### 13.1 Relational Databases

![第 3 页](Web技术双语Part-7-数据库访问课件.assets/第3页.webp)

原文：

13.1 Relational Databases

• A database stores data in a way allowing

<sup>➢</sup>Efficient changes (additions, modifications and deletions),

<sup>➢</sup>Efficient searching.

Programming the world wide web

13-3

### 14.1 Relational Databases

![第 4 页](Web技术双语Part-7-数据库访问课件.assets/第4页.webp)

原文：

14.1 Relational Databases

• The relational model is currently the most popular model.

<sup>➢</sup>Data is stored in many tables.

<sup>➢</sup>Table columns are named.

<sup>➢</sup>Each row of a table contains a value for each column, though some values may be missing.

<sup>➢</sup>Rows are referred to as entities.

<sup>➢</sup>The primary key is one or more columns in a table whose values uniquely identify each row.

Programming the world wide web

13-4

### 13.1 Logical Data Model for Corvettes DB

![第 5 页](Web技术双语Part-7-数据库访问课件.assets/第5页.webp)

原文：

13.1 Logical Data Model for Corvettes DB

Corvettes

States

Corvettes\_Equipment

Equipment

Programming the world wide web

13-5

### Corvettes

![第 6 页](Web技术双语Part-7-数据库访问课件.assets/第6页.webp)

原文：

Corvettes

Programming the world wide web

13-6

### 13.1 Relational Databases

![第 7 页](Web技术双语Part-7-数据库访问课件.assets/第7页.webp)

原文：

13.1 Relational Databases

• Example, Corvettes table

<sup>➢</sup>Primary key is an index number.

<sup>➢</sup>Each row represents a different vehicle.

<sup>➢</sup>Columns are important characteristics of the vehicles.

<sup>➢</sup>Figure 13.3

Programming the world wide web

13-7

### 13.1 Relational Databases

![第 8 页](Web技术双语Part-7-数据库访问课件.assets/第8页.webp)

原文：

13.1 Relational Databases

• Each state can be associated with several cars.

<sup>➢</sup>Each state could have important data, besides the name.

<sup>➢</sup>A separate States table is created with a primary key.

<sup>➢</sup>Each entity in the Corvettes table refers to the States .

<sup>➢</sup>That way, changes in information about a state would not have to be repeated on each line of the Corvettes table.

Programming the world wide web

13-8

### 13.1 Relational Databases

![第 9 页](Web技术双语Part-7-数据库访问课件.assets/第9页.webp)

原文：

13.1 Relational Databases

• Each type of equipment could appear in many cars, and each car could have many types of equipment.

<sup>➢</sup>A table Equipment describing equipment is set up.

<sup>➢</sup>A table Corvettes\_Equipment giving the Corvettes and Equpment relation is set up.

<sup>✓</sup>This is specified by pairs of ids: Corvette-id and Equipment-id.

Programming the world wide web

### 13.2 Structured Query Language

![第 10 页](Web技术双语Part-7-数据库访问课件.assets/第10页.webp)

原文：

13.2 Structured Query Language

• SQL is a standardized language for manipulating and querying relational databases.

• Although relational databases support SQL, there may be some minor or significant differences in the implementations for different DBMS such as Oracle, SQL Server, Sybase, DB2.

• SQL is non-procedure language.

Programming the world wide web

13-10

### 13.2 Structured Query Language

![第 11 页](Web技术双语Part-7-数据库访问课件.assets/第11页.webp)

原文：

13.2 Structured Query Language

• SQL reserved words are not case sensitive

<sup>➢</sup>However, some systems may treat names such as column names as case sensitive.

• Single quotes ‘ are used for literal strings.

Programming the world wide web

13-11

### 13.2 The CREATE TABLE Command

![第 12 页](Web技术双语Part-7-数据库访问课件.assets/第12页.webp)

原文：

13.2 The CREATE TABLE Command

Create a table with specified columns, each column having a specified type of data and satisfying certain constraints.

• Syntax

CREATE TABLE table\_name(

column\_name\_1 data\_type constraints,

column\_name\_n data\_type constraints);

• Common types: integer, real, double, char(length)

Programming the world wide web

13-12

### 13.2 Create Table Constraints

![第 13 页](Web技术双语Part-7-数据库访问课件.assets/第13页.webp)

原文：

13.2 Create Table Constraints

• The constraint not null causes an error to be raised if a row is inserted in which the corresponding column does not have a value.

The primary key constraint causes an error to be raised if a row is inserted in which the corresponding column has a value that equals the value in another row.

<sup>➢</sup>This can be applied to a group of several columns if the primary key is multi-column.

• The foreign key constraints use for the referring to the column in another table.

Programming the world wide web

13-13

### 13.2 The CREATE TABLE Example

![第 14 页](Web技术双语Part-7-数据库访问课件.assets/第14页.webp)

原文：

13.2 The CREATE TABLE Example

• create database hjydb;

• use hjydb;

Programming the world wide web

13-14

### 13.2 The CREATE TABLE Example

![第 15 页](Web技术双语Part-7-数据库访问课件.assets/第15页.webp)

原文：

13.2 The CREATE TABLE Example

Programming the world wide web

13-15

### 13.2.2 The INSERT Command

![第 16 页](Web技术双语Part-7-数据库访问课件.assets/第16页.webp)

原文：

13.2.2 The INSERT Command

• Inserts a new row into a table

• Syntax

INSERT INTO table\_name

(column\_name\_1, ..., column\_name\_n)

VALUES (value\_1, ..., value\_n);

<sup>➢</sup>The values provided will be placed into corresponding columns.

<sup>➢</sup>Columns not named will receive no value.

<sup>✓</sup>This will cause an error if the column was created with a not null constraint

Programming the world wide web

13-16

### 13.2 The INSERT Command Example

![第 17 页](Web技术双语Part-7-数据库访问课件.assets/第17页.webp)

原文：

13.2 The INSERT Command Example

• insert into states(state\_id, state) values(1,’Florida’);

• insert into v values(1,'couple',32.3,1976,1);

Programming the world wide web

13-17

### 13.2 The SELECT Command

![第 18 页](Web技术双语Part-7-数据库访问课件.assets/第18页.webp)

原文：

13.2 The SELECT Command

• Used to query databases

• The command returns a result, a virtual table.

• SELECT column-names FROM table-names [WHEREcondition];

<sup>➢</sup>The resultant table has columns as named.

<sup>➢</sup>Rows are derived from the table named.

<sup>➢</sup>The WHERE clause is optional.

<sup>➢</sup>The WHERE clause specifies constraints on the rows being selected.

<sup>➢</sup>If \* is used for the column names, all columns are selected.

Programming the world wide web

13-18

### 13.2 The SELECT Command Example

![第 19 页](Web技术双语Part-7-数据库访问课件.assets/第19页.webp)

原文：

13.2 The SELECT Command Example

• select v\_id, body\_style from v;

• select body\_style, miles from v where v\_id=1;

Programming the world wide web

13-19

### 13.2 Joins

![第 20 页](Web技术双语Part-7-数据库访问课件.assets/第20页.webp)

原文：

13.2 Joins

• Task: list corvettes that have CD players

• This involves three tables: Corvettes, Equipment, Corvettes\_Equipment

A virtual table is constructed with combinations of rows from the two tables Corvettes and Equipment: a join of the three tables

• The WHERE clause specifies which rows of the join are to be retained in the result

Programming the world wide web

13-20

### 13.2 A Query Using a Join

![第 21 页](Web技术双语Part-7-数据库访问课件.assets/第21页.webp)

原文：

13.2 A Query Using a Join

Programming the world wide web

13-21

### 13.2 The UPDATE Command

![第 22 页](Web技术双语Part-7-数据库访问课件.assets/第22页.webp)

原文：

13.2 The UPDATE Command

• Changes values in an existing row or some rows

• The WHERE clause identifies the rows to be updated.

Programming the world wide web

13-22

### 13.2 The UPDATE Command

![第 23 页](Web技术双语Part-7-数据库访问课件.assets/第23页.webp)

原文：

13.2 The UPDATE Command

• update states set state=‘New York’ where state\_id=1;

Programming the world wide web

13-23

### 13.2 The DELETE Command

![第 24 页](Web技术双语Part-7-数据库访问课件.assets/第24页.webp)

原文：

13.2 The DELETE Command

• Removes one or more rows

• Syntax

DELETE FROM table\_name

WHERE column\_name = value;

• The WHERE clause determines which rows are deleted

Programming the world wide web

13-24

### 13.2 The DELETE Command

![第 25 页](Web技术双语Part-7-数据库访问课件.assets/第25页.webp)

原文：

13.2 The DELETE Command

• Delete from states where state\_id=1;

Programming the world wide web

13-25

### 13.2 The DROP Command

![第 26 页](Web技术双语Part-7-数据库访问课件.assets/第26页.webp)

原文：

13.2 The DROP Command

• Remove a table or database from the system

<sup>➢</sup>A database system usually has several databases within it, and collections of tables in each database.

• Syntax

DROP (TABLE|DATABASE)[IF EXISTS] name;

<sup>➢</sup>The IF EXISTS clause may be included to prevent an error indication if the table or database doesn’t exist.

Programming the world wide web

13-26

### 13.3 Client/Server Database Architecture

![第 27 页](Web技术双语Part-7-数据库访问课件.assets/第27页.webp)

原文：

13.3 Client/Server Database Architecture

• Two-tier architecture

<sup>➢</sup>Client connects to the database to get information.

<sup>➢</sup>Client performs computations and user interactions.

• Problems with two-tier

<sup>➢</sup>Servers getting smaller so client software getting more complex

<sup>➢</sup>Keeping clients up to date becomes difficult.

Programming the world wide web

13-27

### 13.3 Client/Server Database Architecture

![第 28 页](Web技术双语Part-7-数据库访问课件.assets/第28页.webp)

原文：

13.3 Client/Server Database Architecture

• Three-tier architecture

<sup>➢</sup>Web server with applications sits between a browser and the database system.

<sup>➢</sup>The web server accesses the database, carries out computations and deals with user interactions.

Programming the world wide web

13-28

### 13.3 Microsoft Access Architectrue

![第 29 页](Web技术双语Part-7-数据库访问课件.assets/第29页.webp)

原文：

13.3 Microsoft Access Architectrue

• Open Database Connectivity (ODBC)

• An application programming interface (API) provides services to interact with a database

• One service is to submit SQL to the database system and to return results

• An ODBC driver manager, on the client, chooses the proper interface for a particular database

Programming the world wide web

13-29

### 13.3 Database Access Architecture

![第 30 页](Web技术双语Part-7-数据库访问课件.assets/第30页.webp)

原文：

13.3 Database Access Architecture

Programming the world wide web

13-30

### 13.3 PHP and Database Access

![第 31 页](Web技术双语Part-7-数据库访问课件.assets/第31页.webp)

原文：

13.3 PHP and Database Access

• There are modules available in PHP to access numerous different database systems

Programming the world wide web

13-31

### 13.4 The MySQL Database System

![第 32 页](Web技术双语Part-7-数据库访问课件.assets/第32页.webp)

原文：

13.4 The MySQL Database System

The first step to use MySQL is logging into the MySQL system, which is done with the following command. mysql [-h host] [-u username] [database\_name] [-p]

• The second step is to create a new database. create database cars;

• The third step is to specify which database to be used. use cars;

Programming the world wide web

13-32

### 13.4 The MySQL Database System

![第 33 页](Web技术双语Part-7-数据库访问课件.assets/第33页.webp)

原文：

13.4 The MySQL Database System

• Show how many databases are there on the system

• Syntax:

show databases;

• Show how many table there are in a specific database

• Syntax:

show tables;

• Show the schema of table

• Syntax

desc v;

Programming the world wide web

13-33

### 13.5 Database access with PHP and MySQL

![第 34 页](Web技术双语Part-7-数据库访问课件.assets/第34页.webp)

原文：

13.5 Database access with PHP and MySQL

• PHP access to Mysql is achieved with two documents.

<sup>➢</sup>One is to collect user request (.html).

<sup>➢</sup>The other is used to process the request and return the HTML document (.php).

Programming the world wide web

13-34

### 13.5.2 Connecting to MySQL

![第 35 页](Web技术双语Part-7-数据库访问课件.assets/第35页.webp)

原文：

13.5.2 Connecting to MySQL

• The mysqli\_connect() function connects a script to a MySQL server and selects a database

• It accepts four parameters.

<sup>➢</sup>First parameter is MySQL server host

<sup>➢</sup>Second parameter is the MySQL username

<sup>➢</sup>Third parameter is the password, the default is blank

<sup>➢</sup>Fourth parameter is the name of the selected database

• Example: connect.php

Programming the world wide web

13-35

### 13.5.2 Connecting to MySQL

![第 36 页](Web技术双语Part-7-数据库访问课件.assets/第36页.webp)

原文：

13.5.2 Connecting to MySQL

• The mysqli\_close() function accepts the handle of the connection.

• Example: connect.php

Programming the world wide web

13-36

### 13.5.2 Connecting to MySQL

![第 37 页](Web技术双语Part-7-数据库访问课件.assets/第37页.webp)

原文：

13.5.2 Connecting to MySQL

Programming the world wide web

13-37

### 13.5.3 Requesting MySQL Operations

![第 38 页](Web技术双语Part-7-数据库访问课件.assets/第38页.webp)

原文：

13.5.3 Requesting MySQL Operations

• The mysqli\_query function takes two parameters,

<sup>➢</sup>The first is the return value from the mysqli\_connect

<sup>➢</sup>The second is SQL

<sup>➢</sup>Returns a result object

• Example:

\$query=“select \* from v”;

\$result=mysql\_query(\$db,\$query);

Programming the world wide web

13-38

### 13.5.3 Requesting MySQL Operations

![第 39 页](Web技术双语Part-7-数据库访问课件.assets/第39页.webp)

原文：

13.5.3 Requesting MySQL Operations

• Functions that apply to the result object

<sup>➢</sup>mysqli\_num\_rows returns number of rows in the result.

<sup>➢</sup>mysqli\_num\_fields returns the number of fields (columns) in the result.

<sup>➢</sup>mysqli\_fetch\_assoc returns an array with the next row of results. The keys are the column names and the values are the values of those column fields.

Programming the world wide web

13-39

### 13.6.3 Requesting MySQL Operations

![第 40 页](Web技术双语Part-7-数据库访问课件.assets/第40页.webp)

原文：

13.6.3 Requesting MySQL Operations

13-40

### 13.6.3 Requesting MySQL Operations

![第 41 页](Web技术双语Part-7-数据库访问课件.assets/第41页.webp)

原文：

13.6.3 Requesting MySQL Operations

• Example fetch.php

Programming the world wide web

13-41

### 13.6.3 Requesting MySQL Operations

![第 42 页](Web技术双语Part-7-数据库访问课件.assets/第42页.webp)

原文：

13.6.3 Requesting MySQL Operations

• The keys are the column names.

Programming the world wide web

13-42

### 13.6.3 Requesting MySQL Operations

![第 43 页](Web技术双语Part-7-数据库访问课件.assets/第43页.webp)

原文：

13.6.3 Requesting MySQL Operations

• Each array contains each field value indexed by position

Programming the world wide web

13-43

### 13.6 PHP/MySQL Example

![第 44 页](Web技术双语Part-7-数据库访问课件.assets/第44页.webp)

原文：

13.6 PHP/MySQL Example

• The example with carsdata.html and access\_cars.php allows users to submit SQL commands that are executed against the enweb1 database

Programming the world wide web

13-44
