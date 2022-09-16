import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_current_date():
    '''
    获取当前日期
    :return:
    '''
    timestamps = str(datetime.now().date())
    return timestamps

def get_week_day():
    '''
    获取今天是周几
    :return:
    '''
    week = datetime.today().isoweekday()
    a = {'一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7}
    for i in a:
        if a[i] == week:
            return i

def cal_date(data1,data2):
    '''
    计算日期查
    :param data1: 开始日期
    :param data2: 结束日期
    :return:
    '''
    data1 = time.strptime(data1,"%Y-%m-%d")
    data2 = time.strptime(data2,"%Y-%m-%d")
    data1 = datetime(data1[0],data1[1],data1[2]).date()
    data2 = datetime(data2[0],data2[1],data2[2]).date()
    cal = data2 - data1
    return cal.days

currant_date = get_current_date()
content = f"""提醒划水小助手
【摸鱼办公室】
{currant_date}  周{get_week_day()}
上午好，摸鱼人，工作再累，一定不要忘记摸鱼哦
有事没事起身去茶水间去厕所去廊道走走，
别老在工位上坐着，钱是老板的，但命是自己的
"""

url = 'https://fangjia.bmcx.com/2022__fangjia/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
holiday_list = list(map(lambda td: {td.contents[0].get_text(): f"2022年{td.contents[1].get_text().split('~')[0]}"},
                            soup.table.children))
holiday_list = holiday_list[1:]
for holiday in holiday_list:
    for k, v in holiday.items():
        v = v.replace('年', '-').replace('月', '-').replace('日', '')
        content += f"距离{k}还有{cal_date(currant_date, v)}天 （{v}）\n"

print(content)