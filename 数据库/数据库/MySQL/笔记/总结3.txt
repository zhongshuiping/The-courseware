select distinct * from 表名
where ...
group by ...
having ...
order by ...
limit ...

关系的问题
（1）是什么样的对应关系
（2）存储关系的字段，使用什么类型
（3）存入数据时错了怎么办？

查：学生姓名及所在的班级名称
分析：stu,class
stu.class_id=class.id
答：select * from stu inner join class on stu.class_id=class.id


查询学生的姓名、平均分
分析：姓名->stu
	平均分->先sco查分数，再聚合avg
需要从两张表中获取数据，所以需要连接
连接的条件：stu.id=sco.stu_id
实现一：获取所有的原始数据
select name,score from stu inner join sco on stu.id=sco.stu_id
继续分析：对每个学生求平均分
让姓名相同的信息，分成一组
select name,avg(score) from stu inner join sco on stu.id=sco.stu_id
group by name

查询男生的姓名、总分
分析：姓名->stu
	男生->stu
	总分->sum(),分数->sco
连接条件：stu.id=sco.stu_id
实现一：select * from sco inner join stu on stu.id=sco.stu_id
	where gender=1
实现二：分组
	。。。 group by name

查询科目的名称、平均分
sub.title->sub
avg(),score->sco
sub.id=sco.sub_id


查询学生姓名、科目名称、分数
stu
sub
sco

查询省的名称为“山西省”的所有城市
select * from areas where title='山西省'

查询‘广州市’的所有区县
	#select * from areas where title='淄博市'  #370300
	#select * from areas where pid='370300'  #370301
	#select * from areas where pid='370301'

	#areas as shi where shi.title='广州市'
	#areas as qu on qu.pid=shi.id
	#areas as qu1 on qu1.pid=qu.id

	select qu.*,qu1.*
	from areas as shi
	inner join areas as qu on qu.pid=shi.id
	left join areas as qu1 on qu1.pid=qu.id
	where shi.title='淄博市'

子查询
#查询广州市、淄博市的所有区
#select id from areas where title='广州市' or title='淄博市'
select * from areas where pid in(select id from areas where title='广州市' or title='淄博市')


源码安装：python setup.py install
