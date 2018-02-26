
-- 查询
	-- 查询所有字段
	-- select * from 表名;
	select * from students; 

	-- 查询指定字段
	-- select 列1,列2,... from 表名;
	select name,age from students;
	
	-- 使用 as 给字段起别名
	-- select 字段 as 名字.... from 表名;
	select name as "姓名",age as "年龄" from students;

	-- select 表名.字段 .... from 表名;
	select students.name as "姓名",students.age as "年龄" from students;

	
	-- 可以通过 as 给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
	select s.name as "姓名",s.age as "年龄" from students as s;
	
	-- 失败的select students.name, students.age from students as s;
	

	-- 消除重复行(查性别)
	select gender from students;
	-- distinct 字段 
	select distinct gender from students;
	

-- 条件查询
	-- 比较运算符
		-- select .... from 表名 where .....
		-- >
		-- 查询大于18岁的信息
		select * from students where age > 18;

		-- <
		-- 查询小于18岁的信息
		select * from students where age < 18;
		

		-- >=
		-- <=
		-- 查询小于或者等于18岁的信息
		select * from students where age <= 18;
		-- =
		-- 查询年龄为18岁的所有学生的名字
		select * from students where age = 18;


		-- != 或者 <>
		select * from students where age != 18;
		

	-- 逻辑运算符
		-- and
		-- 18和28之间的所以学生信息
		select * from students where age > 18 and age < 28;
		
		-- 失败select * from students where age>18 and <28;


		-- 18岁以上的女性
		select * from students where age > 18 and gender = 2;


		-- or
		-- 18以上或者身高高过180(包含)以上
		select * from students where age > 18 or height >= 180;


		-- not
		-- 不在 18岁以上的女性 这个范围内的信息
		-- select * from students where not age>18 and gender=2;
		select * from students where not (age > 18 and gender = 2);

		-- 年龄不是小于或者等于18 并且是女性
		select * from students where not age <= 18 and gender = 2 ;
		


	-- 模糊查询(where name like 要查询的数据)
		-- like 
		-- % 替换任意个
		-- _ 替换1个
		-- 查询姓名中 以 "小" 开始的名字
		select * from students where name like "小%";
		

		-- 查询姓名中 有 "小" 所有的名字
		select * from students where name like "%小%";

		-- 查询有2个字的名字
		select * from students where name like "__";
		

		-- 查询有3个字的名字
		select * from students where name like "___";
		

		-- 查询至少有2个字的名字
		select * from students where name like "__%";



	-- 范围查询
		-- in (1, 3, 8)表示在一个非连续的范围内
		-- 查询 年龄为18、34的姓名
		select name from students where age = 18 or age = 34;
		select * from students where age in (18,34,25);
		
		-- not in 不非连续的范围之内
		-- 年龄不是 18、34岁之间的信息
		select * from students where age not in (18,34);
		-- select name from students where not age in (18,34);


		-- between ... and ...表示在一个连续的范围内
		-- 查询 年龄在18到34之间的的信息
		select * from students where age between 18 and 34;

		
		-- not between ... and ...表示不在一个连续的范围内
		-- 查询 年龄不在在18到34之间的的信息
		select * from students where age not between 18 and 34;
		-- 失败的select * from students where age not (between 18 and 34);
		

	-- 空判断
		-- 判空is null
		-- 查询身高为空的信息
		select * from students where height is null;
		
		-- 判非空is not null
		select * from students where height is not null;
		-- 失败select * from students where height not is  null;



-- 排序
	-- order by 字段
	-- asc从小到大排列，即升序
	-- desc从大到小排序，即降序

	-- 查询年龄在18到34岁之间的男性，按照年龄从小到大到排序
	select * from students where (age between 18 and 34) and gender = 1 order by age asc;	
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
	select * from students where (age between 18 and 34) and gender = 2 order by height desc;
	

	-- order by 多个字段
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
	 select * from students where (age between 18 and 34) and gender = 2 order by height desc,age asc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序,
	-- 如果年龄也相同那么按照id从大到小排序
	select * from students where (age between 18 and 34) and gender = 2 order by height desc,age asc,id desc;

	
	-- 按照年龄从小到大、身高从高到矮的排序
	select * from students order by age asc,height desc;


-- 聚合函数
	-- 总数
	-- count
	-- 查询男性有多少人，女性有多少人
	select count(*) from students where gender = 1;
	select count(*) from students where gender = 2;

	-- 最大值
	-- max
	-- 查询最大的年龄
	select max(age) from students;

	-- 查询女性的最高 身高
	select max(height) from students where gender = 2;

	-- 最小值
	-- min
	select min(height) from students ;
	
	-- 求和
	-- sum
	-- 计算所有人的年龄总和
	select sum(age) from students ;

	
	-- 平均值
	-- avg
	-- 计算平均年龄
	select avg(age) from students ;


	-- 计算平均年龄 sum(age)/count(*)
	select sum(age)/count(*) from students;


	-- 四舍五入 round(123.23 , 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
	select round(avg(age),2) from students;

	-- 计算男性的平均身高 保留2位小数
	select round(avg(height),2) from students where gender = 1;
	

-- 分组

	-- group by
	-- 按照性别分组,查询所有的性别
	select gender from students group by gender;
	-- select name,gender from students group by gender;错误
	-- select name,gender from students group by gender;
	-- 失败select * from students group by gender;

	-- 计算每种性别中的人数
	select count(*),gender from students group by gender;


	-- 计算男性的人数
	select count(*),gender from students where gender = 1;

	-- group_concat(...)
	-- 查询同种性别中的姓名
 	select group_concat(name),gender from students group by gender;
	
	-- 查询每组性别的平均年龄
	select avg(age),gender from students group by gender;

	-- having
	-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
	-- 注意 having 后面一定是聚合函数
	select gender from students group by gender having avg(age) > 30;
	
	-- 查询每种性别中的人数多于2个的信息
	select gender from students group by gender having count(*) > 2;

	-- with rollup 汇总的作用

-- 分页
	-- limit start, count
	
	-- 限制查询出来的数据个数
	-- 查询前5个数据
	select * from students limit 5;
	
	-- 每页显示2个，第1个页面
	select * from students limit 0,2;

	-- 每页显示2个，第2个页面
	select * from students limit 2,2;

	-- 每页显示2个，第3个页面
	select * from students limit 4,2;

	-- 每页显示2个，第4个页面
	select * from students limit 6,2;
	

	-- 每页显示2个，显示第6页的信息, 按照年龄从小到大排序
	错误1 select * from students limit 10,2 order by age asc;
	
	-- 工作错误的写法
	失败2 select * from students limit 2*(6-1),2;
	
	-- limit 放在最后面
	 


-- 连接查询
	-- inner join ... on
	-- select ... from 表A inner join 表B;
	
	
	-- 查询 有能够对应班级的学生以及班级信息
	

	-- 按照要求显示姓名、班级
	

	-- 给数据表起名字
	

	-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息 students.*，只显示班级名称 classes.name.
	
	
	-- 在以上的查询中，将班级姓名显示在第1列
	

	-- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
	-- select c.xxx s.xxx from students as s inner join clssses as c on .... order by ....;
	
	
	-- 当时同一个班级的时候，按照学生的id进行从小到大排序
	

	-- left join
	-- 查询每位学生对应的班级信息
	

	-- 查询没有对应班级信息的学生
	-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having .....
	
	
	-- 不建议使用 select * from students left join classes on students.cls_id=classes.id having classes.id is null;
	
	-- right join   on
	-- 将数据表名字互换位置，用left join完成


	

-- 子查询
	-- 标量子查询(一行一列)
	-- 查询出高于平均身高的信息(height)
	
	
	-- 行级子查询
	-- 查询最高的男生信息(一行多列)
	

	-- 列级子查询(一列多行)
	-- 查询学生的班级号能够对应的 学生名字
	-- select name from students where cls_id in (select id from classes);
	
	
	









