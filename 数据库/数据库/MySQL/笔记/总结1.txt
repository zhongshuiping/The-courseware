数据库命令：
创建create database 数据库名 charset=utf8;
删除drop database 数据库名;
查看所有数据库：show databases;
使用数据库：use 数据库名;
----------------------------------------
表命令：
create table 表名(列...);
唯一标识的要求：id
	类型：int unsigned
	约束1：not null
	约束2：primary key
	约束3：auto_increment
列的格式：列的名称 类型 约束
create table stu(
    -> id int not null primary key auto_increment,
    -> name varchar(10) not null,
    -> gender bit default 1,
    -> birthday datetime,
    -> isDelete bit default 0,
    -> );
查看表show tables;
查看表结构desc 表名;
修改表：alter table 表名 add|modify|drop 列名 类型 约束;
alter table stu modify column isDelete bit not null default 0;
删除表：drop table 表名;
----------------------------------------
数据命令：
添加数据：insert into 表名(列名) values(值),(值)...;
修改数据：update 表名 set 列1=值1,... where ...;
删除数据：delete from 表名 where ...;
逻辑删除：update ....
备份：mysqldump >
恢复：mysql <
