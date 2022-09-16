fields = ['a', 'b']
sql = "insert into test2 ({fields}) values ({mark})".format(
    fields='`' + '`,`'.join(fields) + '`',
    mark=','.join(['%s'] * len(fields))
)
temp_list = [[6, 7], [72, 8], [37, 87]]
temp_list = [(1, 2), (2, 3), (3, 4)]
conn = connect()
with conn.cursor() as cur:
    cur.executemany(sql, temp_list)
    conn.commit()
cur.close()
conn.close()




import pymysql
import random
import time
from datetime import datetime

fstatus_list = ['0', '1']
content_list = ['数据异常', '对账成功',
                '对账失败：ACS-109050P资产对账时出错！：DB2 SQL Error: SQLCODE=-204, SQLSTATE=42704, SQLERRMC=uatacs.T_DI_CF_CUSFUND, DRIVER=3.58.82',
                '对账失败：AMS-109051P资产对账时出错！：DB2 SQL Error: SQLCODE=-204, SQLSTATE=42704, SQLERRMC=uatacs.T_DI_CF_CUSFUND, DRIVER=3.58.82',
                '对账失败：ACS-204050P资产对账时出错！：DB2 SQL Error: SQLCODE=-204, SQLSTATE=42704, SQLERRMC=uatacs.T_DI_CF_CUSFUND, DRIVER=3.58.82']
type_dict = {'YHCK': '银行存款对账', 'YQDZ_BZJ': '银期对账_保证金', 'YQDZ_BFJ': '银期对账_备付金', 'CCDZ': '持仓对账'}

fid_start = 16122016170315051473
fproduct_id_list = ['01','02','03','04','05','06','07','08']

class Sqldriver(object):
    # 初始化属性
    def __init__(self):
        self.host = 'hostIP'
        self.port = 3306
        self.user = 'root'
        self.password = 'root'
        self.database = 'bi_acs'

    # 连接数据库
    def Connect(self):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8'
        )

    # 插入数据
    def insert(self, fid, fdate, fproduct_id, fcost_time, fstatus, flog_content, fbus_type, fbus_name, fpmoney, fomoney):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql = "insert into t_dc_result(fid,fdate,fproduct_id,fcost_time,fstatus,flog_content,fbus_type,fbus_name,fpmoney,fomoney)" \
                  " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # 执行sql语句
            cursor.execute(sql, (
            fid, fdate, fproduct_id, fcost_time, fstatus, flog_content, fbus_type, fbus_name, fpmoney, fomoney))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()

    # 生成随机日期
    def mkdate(self):
        a1 = (2016, 1, 1, 0, 0, 0, 0, 0, 0)
        a2 = (2019, 12, 31, 23, 59, 59, 0, 0, 0)

        start = time.mktime(a1)
        end = time.mktime(a2)

        for i in range(10):
            t = random.randint(start, end)
            date_touple = time.localtime(t)
            date = time.strftime("%Y-%m-%d", date_touple)
            print(type(date))
            return date

    # 数据生成并调用数据插入方法
    def data_make(self):
        fid = fid_start
        fdate = self.mkdate()
        fproduct_id = random.choice(fproduct_id_list)
        fcost_time = str(round(random.uniform(1, 100), 2))
        fstatus = random.choice(fstatus_list)
        flog_content = random.choice(content_list)
        fbus_type = random.choice(list(type_dict.keys()))
        fbus_name = str(type_dict[fbus_type])
        fpmoney = str(random.randint(10000, 99999999))
        fomoney = str(random.randint(10000, 99999999))

        self.insert(fid, fdate, fproduct_id, fcost_time, fstatus, flog_content, fbus_type, fbus_name, fpmoney, fomoney)
        fid = fid + 1


if __name__ == '__main__':
    db = Sqldriver()
    # for循环

    for record in range(1,10001):
        db.data_make()
        fid_start +=1
