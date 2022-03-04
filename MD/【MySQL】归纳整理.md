<!--
 * @Author: Lee
 * @Descripttion: RTMart
 * @Date: 2022-03-04 18:26:58
-->
### 文章目录

- [一 、数据库概述](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#__12)
- - [1.1 基础知识](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#11__13)
    - [1.2 根据系统需求绘制 E-R 图](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#12__ER__73)
    - [案例一：校务管理系统](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#_111)
    - [案例二：销售管理系统](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#_120)
- [二 、创建数据库和表](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#__133)
- - [2.1 创建配置数据库](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#21__134)
    - [2.2 使用合适的数据类型创建表及插入数据](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#22__175)
    - [2.3 修改表结构](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#23__201)
- [三 、SQL 数据操纵语言](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#_SQL__244)
- - [3.1 数据的插入、删除和修改处理](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#31__245)
    - [3.2 查询语句、连接查询](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#32__248)
    - [3.3 嵌套子查询](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#33__254)
    - [3.4 对查询结果进行排序、分组](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#34__259)
    - [3.5 常用函数在查询操作中的应用](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#35__337)
- [四 、视图](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#__439)
- [五、创建索引](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#_444)





* * *


> 【考查目标】
> 
> - **1.掌握绘制E-R 图的方法。**
> - **2.掌握创建配置数据库。**
> - **3.掌握创建表、表间联系等约束条件的方法。**
> - **4.掌握常用的 SQL 数据操纵语言。**


* * *

# 一 、数据库概述

## 1.1 基础知识

**1、数据库（`DataBase/DB`）：数据库按照一定的模型结构（数据模型）来`组织`、`存储`和`管理`数据的仓库。**

**2、数据模型：层次型、网状型、`关系型（二维表）`、语义型、面向对象型**

**3、数据库管理系统（DBMS）：系统软件，所有的应用程序访问数据库必须通过DBMS软件**

**4、常见的数据库管理系统：**

- MySQL：自由软件 – 小型数据库
- SQL Server：商业软件 – 中型数据库
- Oracle：商业软件 – 大型数据库
- DB2\SQLite:嵌入式数据库 – 小型数据库（常用于手机）


**5、关系数据库系统（RDBMS）：**

**（1）数据模型（二维表）**

- 关系：规范化的二维表
- 二维表：
行：元组 – 记录
列：属性 – 字段


（**2）关系代数**

**（3）关系数据库语言SQL**

（**4）特点**

- 数据以表格的形式出现
- 每行为各种记录名称
- 每列为记录名称所对应的数据域
- 许多的行和列组成一张表单
- 若干表单组成database


**（5）术语**

- `数据库`：数据库是一些关联表的集合
- `数据表`：表示数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格
- `列`：一列（数据元素）包含了相同类型的数据，例如邮政编码的数据
- `行`：一行（=元组/记录）是一组相关的数据，例如一条用户订阅的数据
- `冗余`：存储两倍数据，冗余降低了性能，但是提高了数据的安全性
- `主键`：主键是唯一的。一个数据表中只能包含一个主键，可以使用主键来查询数据
- `外键`：外键用于关联两个表
- `复合键`：（组合键）将多个列作为一个索引建，一般用于复合索引
- `索引`：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构，类似于书籍的目录。
- `参照完整性`：参照的完整性要求关系中不允许引用不存在的实体。实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。


**6、MySQL数据库**


> MySQL是一个关系型数据库管理系统，由瑞典MySQL
> AB公司开发，目前属于Oracle公司。MySQL是一种关联数据库管理系统，关丽娜数据库将数据保存在不同表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。


（1）MySQL是开源的，目前隶属于Oracle旗下产品。
（2）MySQL支持大型的数据库。
（3）MySQL使用标准的SQL数据语言形式。
（4）MySQL可以运行于多个系统上，并且支持多种语言。这些编程语言包括C、C++、Python、Java、Perl、PHP、Eiffel、Ruby和Tcl等。
（5）MySQL对PHP有很好的支持，PHP是目前最流行的Web开发语言。
（6）MySQL支持大型数据库，支持5000万条记录的数据仓库，32位系统表文件最大可支持4GB，64位系统支持最大的表文件为8TB。
（7）MySQL是可以定制的，采用了GPL协议（定制需修改源码进行开发）

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

## 1.2 根据系统需求绘制 E-R 图

**1、实体-联系图，用于建立概念模型**

**2、概念模型是指：`把现实世界的对象抽象为某一种不依赖于具体计算机系统的数据结构`。***（这个抽象的数据结构称为概念模型）*

**3、E-R 图与具体的计算机系统及 DBMS 无关**

**4、E-R 概念结构**

- *用 E-R 图对一个单位信息状况进行直观说明，称为一个单位的 E-R 概念结构。*


**5、E-R 概念模式**

- *用 E-R 概念结构对一个单位进行模拟，称为：`E-R 概念模式`。*


**6、E-R 图形**

- *`矩形框表示实体集`。实体就是客观对象。用一个名词表达的事物。*
- *`菱形框表示联系`。实体之间的关系。如：学生与课程之间的关系是：选课。*
◇ 联系是具有属性的
- *`椭圆（或圆形）框表示属性`。*


**7、联系类型：**

- 有三种：`1：1 即 1 对 1`、`1：n 即 1 对多`、`n:m 即多对多`


**8、将 E-R 图转换成关系模式**

*（1）每一个实体，转换成一张二维表。*

- 实体的属性，就是二维表的属性。
- 实体的主键成为二维表的主键。


*（2）每一个联系，转换成一张二维表。*

- 联系的属性就是二维表的属性。
- 更重要的是：联系所涉及到的各个实体的主键，也是该二维表的属性。
- 二维表的主键：
1)若联系类型是 1：1，则任选联系中的一个 1 端所对应的那个实体的主键作为联系这张表的主键。
2)若联系类型是 1：n,则选择联系中的 n 瑞的实体的主键。
3)若联系类型是 n：m,则选择各个实体的主键，构成一个组合。


[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

## 案例一：校务管理系统


> （1）教师管理功能：录入老师的姓名、地址、所教课程；老师缺课记录的名字、时间、原因、课程
> （2）学生管理功能：录入学生的姓名、所选课程、成绩
> （3）主任管理功能：查询系统（教师情况、学生总成绩、学生平均成绩）


![在这里插入图片描述](https://img-blog.csdnimg.cn/8be2a2bf9494459c9096bafb2b09b8f9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16)

* * *

## 案例二：销售管理系统


> 商店实体集：属性有商店编号、商店名、地址等
> 商品实体集：属性有上平好、商品名、规格、单价
> 职工实体集：属性有职工编号、姓名、性别、业绩等
> 商品与商品之间存在销售关系，每个商店可销售多种商品，每种商品也可以放在多个商店进行销售，每个商店销售一种商品，有月销售量；商店与职工之间存在着聘用关系，每个商店有许多职工，每个职工只能在一个商店工作，商店平庸职工有聘期和月薪。


![在这里插入图片描述](https://img-blog.csdnimg.cn/0ee1cbb21be74533912c1923ff634e91.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16)

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

# 二 、创建数据库和表

## 2.1 创建配置数据库

**首先使用命令 `mysql -u用户名 -p密码;` 登陆已经安装的MySQL数据库，使用 `show databases;` 命令查看当前的数据库**


```sql
E:\35192\Desktop>mysql -uroot -p123456
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.17 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| biyesheji          |
| dormitory          |
| ........           |
+--------------------+
25 rows in set (0.02 sec)
1234567891011121314151617181920212223
```

**使用命令 `create database 数据库名；` 创建新的数据库；创建完成后使用 `use 数据库名;` 转到要使用的数据库中：**


```sql
mysql> create database zzb;
Query OK, 1 row affected (0.01 sec)

mysql> use zzb;
Database changed
12345
```

**转数据库的目的：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/bb0b6059c7d84089850cfa23f783c107.png?x_10#pic_center)
**这里的 `jdbc` 为某一个数据库，我们创建的表是存储在其中的，就像文件夹目录一样，创建表之前我们需要选择其存储的位置。**

* * *

## 2.2 使用合适的数据类型创建表及插入数据

***关于数据库类型的博文推荐：*[*mysql数据库数据类型*](https://blog.csdn.net/dayi_123/article/details/83069221?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164618947716780357256187%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&amp;request_id=164618947716780357256187&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-83069221.pc_search_result_cache&amp;utm_term=%E6%95%B0%E6%8D%AE%E5%BA%93%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B&amp;spm=1018.2226.3001.4187)**

**创建数据库表需要：`表名，表字段名、字段数据类型（长度）、限制`。**


```sql
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `name` text CHARACTER ,
  `id` int(11) NULL DEFAULT NULL,
  `sex` text CHARACTER ,
  `age` int(11) NULL DEFAULT NULL,
  `hobby` text CHARACTER 
);
12345678
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8740cd0d1bea48e683636f1d75439a05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

**插入数据使用 `insert into 表名（字段...）；`的语法，注意数据值与数据类型保持一致：**


```sql
INSERT INTO `students` VALUES ('Lucy', 191, '女', 20, '游泳');
INSERT INTO `students` VALUES ('Tom', 194, '男', 22, '打球');
INSERT INTO `students` VALUES ('Tom', 194, '男', 22, '打球');
123
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b2585e1eb24848f2a60324bcce54fac6.png?x_10#pic_center)

* * *

## 2.3 修改表结构

**应用场景：当一张数据库中表已经建立好结构 并且也已经存有数据 不应该删除整张表若需要修改表的部分字段的类型 字段名 或属性 可以采用alter修改**

**1.增加列**


```sql
alter table 表名 add 列名 类型（长度）约束；
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210325193855866.png)

* * *

**2.修改现有列类型、长度和约束**


```sql
alter table 表名 modify 列名 类型（长度） 约束；
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210325193908733.png)
***注意:`modify只能修改属性 不能修改列名`***

* * *

**3.修改现有列名称**


```sql
alter table表名 change 旧列名 新列名 类型（长度）约束；
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210325193908731.png)

* * *

**4.删除现有列**


```sql
alter table 表名 drop 列名；
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210325194130889.png)
**参见：[【MySQL】DDL常见操作](https://blog.csdn.net/qq_45797116/article/details/115824681)**
**参见：[【MySQL】数据库表结构的修改](https://blog.csdn.net/qq_45797116/article/details/115877618)**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

# 三 、SQL 数据操纵语言

## 3.1 数据的插入、删除和修改处理

**参见：[【MySQL】DML常见操作](https://blog.csdn.net/qq_45797116/article/details/115877618)**

* * *

## 3.2 查询语句、连接查询

**参见：[【MySQL】DQL常见操作](https://blog.csdn.net/qq_45797116/article/details/116238132)**
**参见：[【MySQL】MySQL 的连接（Join）以及 MySQL求交集和差集](https://blog.csdn.net/qq_45797116/article/details/115082375)**
**参见：[【MySQL】MySQL 的连接(内、左、右、全)](https://blog.csdn.net/qq_45797116/article/details/115082375)**

* * *

## 3.3 嵌套子查询

**参见：[【MySQL】数据处理（数据的查询之子查询、复查询）](https://blog.csdn.net/qq_45797116/article/details/104033529)**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

## 3.4 对查询结果进行排序、分组

**排序：**


```sql
mysql> select * from student;
+------------------+------+------+
| name             | age  | gpa  |
+------------------+------+------+
| ulysses_thompson |   64 |  1.9 |
| katie_carson     |   25 | 3.65 |
| like_king        |   65 | 0.73 |
| holly_davidson   |   57 | 2.43 |
| fred_miller      |   55 | 3.77 |
+------------------+------+------+
5 rows in set (0.00 sec)

mysql> select * from student order by age;    // 按照年龄默认升序排列查询
+------------------+------+------+
| name             | age  | gpa  |
+------------------+------+------+
| katie_carson     |   25 | 3.65 |
| fred_miller      |   55 | 3.77 |
| holly_davidson   |   57 | 2.43 |
| ulysses_thompson |   64 |  1.9 |
| like_king        |   65 | 0.73 |
+------------------+------+------+
5 rows in set (0.00 sec

mysql> select * from student order by age desc;  // 按照年龄指定降序排列查询
+------------------+------+------+
| name             | age  | gpa  |
+------------------+------+------+
| like_king        |   65 | 0.73 |
| ulysses_thompson |   64 |  1.9 |
| holly_davidson   |   57 | 2.43 |
| fred_miller      |   55 | 3.77 |
| katie_carson     |   25 | 3.65 |
+------------------+------+------+
5 rows in set (0.00 sec)
1234567891011121314151617181920212223242526272829303132333435
```

**分组：**


```sql
mysql> select * from user;
+----+----------+------------+------+---------+
| id | username | birthday   | sex  | address |
+----+----------+------------+------+---------+
|  1 | 宾白     | 1999-07-03 | 男   | 河北省  |
|  2 | 安荷     | 1998-02-07 | 女   | 江苏省  |
|  3 | 白秋     | 2000-03-07 | 女   | 天津市  |
|  4 | 雪莲     | 1998-06-07 | 女   | 湖北省  |
|  5 | 宾实     | 2000-08-07 | 男   | 江苏省  |
|  6 | 斌斌     | 1998-03-07 | 男   | 江苏省  |
+----+----------+------------+------+---------+
6 rows in set (0.00 sec)

mysql> select * from user group by address,sex;
+----+----------+------------+------+---------+
| id | username | birthday   | sex  | address |
+----+----------+------------+------+---------+
|  1 | 宾白     | 1999-07-03 | 男   | 河北省  |
|  2 | 安荷     | 1998-02-07 | 女   | 江苏省  |
|  3 | 白秋     | 2000-03-07 | 女   | 天津市  |
|  4 | 雪莲     | 1998-06-07 | 女   | 湖北省  |
|  5 | 宾实     | 2000-08-07 | 男   | 江苏省  |
+----+----------+------------+------+---------+
5 rows in set (0.00 sec)

mysql> select * from user group by sex;
+----+----------+------------+------+---------+
| id | username | birthday   | sex  | address |
+----+----------+------------+------+---------+
|  1 | 宾白     | 1999-07-03 | 男   | 河北省  |
|  2 | 安荷     | 1998-02-07 | 女   | 江苏省  |
+----+----------+------------+------+---------+
2 rows in set (0.00 sec)
123456789101112131415161718192021222324252627282930313233
```

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

## 3.5 常用函数在查询操作中的应用


```sql
mysql> select avg(age) from student;  // 计算年龄平均值
+----------+
| avg(age) |
+----------+
|  53.2000 |
+----------+
1 row in set (0.00 sec)

mysql> select count(age) from student;  // 计算年龄数量
+------------+
| count(age) |
+------------+
|          5 |
+------------+
1 row in set (0.00 sec)

mysql> select max(age) from student;  // 计算年龄最大值
+----------+
| max(age) |
+----------+
|       65 |
+----------+
1 row in set (0.02 sec)

mysql> select min(age) from student; // 计算年龄最下值
+----------+
| min(age) |
+----------+
|       25 |
+----------+
1 row in set (0.02 sec)

mysql> select sum(age) from student; // 计算年龄总和
+----------+
| sum(age) |
+----------+
|      266 |
+----------+
1 row in set (0.00 sec)

mysql> select greatest(1,2,3,55,4);  // 返回列表中的最大值
+----------------------+
| greatest(1,2,3,55,4) |
+----------------------+
|                   55 |
+----------------------+
1 row in set (0.00 sec)

mysql> select least(1,2,3,55,4);  // 返回列表中的最小值
+-------------------+
| least(1,2,3,55,4) |
+-------------------+
|                 1 |
+-------------------+
1 row in set (0.00 sec)

mysql> select mod(10,3);   // 返回两个参数的模
+-----------+
| mod(10,3) |
+-----------+
|         1 |
+-----------+
1 row in set (0.00 sec)

mysql> select mod(3,10);  // 当x<y的时候直接返回x的值
+-----------+
| mod(3,10) |
+-----------+
|         3 |
+-----------+
1 row in set (0.00 sec)

mysql> select round(4.5);  // 返回离 x 的最近整数
+------------+
| round(4.5) |
+------------+
|          5 |
+------------+
1 row in set (0.00 sec)

mysql> select rand();  // 返回 0-1 的随机数
+--------------------+
| rand()             |
+--------------------+
| 0.1309335437891386 |
+--------------------+
1 row in set (0.00 sec)

mysql> select rand();
+-------------------+
| rand()            |
+-------------------+
| 0.613614663121863 |
+-------------------+
1 row in set (0.00 sec)
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495
```

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

# 四 、视图

**参见：[【MySQL】数据处理（视图）](https://blog.csdn.net/qq_45797116/article/details/103664394)**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)

* * *

# 五、创建索引

**通过索引，查询数据是不用读完整的记录信息，而是值查询索引列。否则，数据库系统将读取每条记录的所有信息进行匹配。**

**可以将索引比作新华字典的音序表，通过简单的音序表查询便可以提高陌生字的快速查询。因此，使用索引查询可以很大程度上提高数据库的查询速度，提高了数据库系统的性能。**

**创建索引是指在某个表的一列或多列上建立一个索引，MySQL提供了三种创建索引的方法：**


```sql
# 直接创建
mysql> create index indexName on tableName(fieldName);

# 创建表的时候创建
mysql> create table test(
            tid int,
            tname varchar(20),
            sex varchar(1),
            index [indexName] (fieldName)
         );

# 修改表结构添加索引
mysql> alter table tableName add unique index indexName (fieldName);
12345678910111213
```

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123221731?spm=1001.2014.3001.5502#0)