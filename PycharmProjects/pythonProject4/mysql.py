import MySQLdb

#打开数据库连接
db = MySQLdb.connect(host="127.0.0.1",user="",passwd="",db="",port="",charset="utf8")

#获取操作游标
cu = db.cursor()

#构造SQL语句-查询
sqlstr = """
select * from 表名；
"""
#构造SQL语句-更新
sqlstr = """
update biao set 'lie' = 'jintian' where name = '44'
"""
#构造SQL语句-插入
sqlstr = """
insert into biao values （1,3）
"""
#构造SQL语句-删除
sqlstr = """
delete biao where id>2;
"""
#构造SQL语句-分组
sqlstr = """
select sum(price)from goods group by goods_type;
"""
#构造SQL语句-子查询
sqlstr = """
use 数据库
select * from table1 where id = (select id from table2 where name = 'ke' )
select * from table1 where id in (select id from table2 where id > 2 )
"""

#构造SQL语句-多表联查    mysql workbench      左表-join-右表
sqlstr = """
use 数据库

create table testtable(id int primary key, name varchar(50) not null);

左连接-以左表为基准，左表中数据全出现，右表出现可以匹配的,没有出现的用null代替；
select * from a left join b on a.name = b.name

右连接-以右表为基准，右表中数据全出现，左表出现可以匹配的,没有出现的用null代替；
select * from a right join b on a.name = b.name

内连接-两张表的交集，共有部分出现；
select * from a inner join b on a.name = b.name

全连接-两张表的交叉相连；
select * from a full join b on a.name = b.name

select * from table1 where id in (select id from table2 where id > 2 )
"""

#执行SQL访问
cu.execute("select version();")

#将更新提交到数据库(增删改需要）
db.commit()

#获取执行结果
data = cu.fetchone()   #获取一条       fetchall 获取所有    fetchmany  获取N条
print("database version is:",data)

#释放资源
cu.close()
db.close()







