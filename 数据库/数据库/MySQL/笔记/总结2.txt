数据库、表、字段、行

问：查询姓黄或洪的男生
分析：数据从哪来，哪个表stu
条件：姓黄或洪name or
	and
	男生gender
答：select * from stu where gender=1 and (name like '黄%' or name like '洪%')

distinct
条件：where 字段 运算符 常量
分组聚合：group by ... having ...


关系的存储方案
1：1-》存储在任何一个表中
1：n-》存储在n的表中，新增一个字段
m：n-》新建表

成绩表：id,成绩，学生，科目
关系，第三范式，外键

问题：两个表之间有关系吗？分析的依据是当前系统的业务，够用就行
	怎么存储这个关系？参照“关系的存储方案”
	关系字段的类型是什么？根据第三范式，引用主键，所以主键的类型，就是这个字段的类型
	关系字段的数据有效性怎么保证？外键

create table sco(
id int not null auto_increment primary key,
stu_id int,
sub_id int,
score int(3),
foreign key(stu_id) references stu(id),
foreign key(sub_id) references sub(id)
);

insert into sco values(0,1,1,100);

