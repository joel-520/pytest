import requests
import time
from lxml import etree
import pandas as pd
import csv

base_url = 'https://www.qcc.com/web/search?key='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
data = pd.read_csv('D:\data.csv',header=None)
data.columns=['id','url']
a = []
f = open('企查查.csv','w',newline='')
writer  = csv.writer(f)

title = ['统一社会信用代码','企业名称','法定代表人','登记状态','成立日期','注册资本','实缴资本','核准日期','组织机构代码','工商注册号','纳税人识别号','企业类型','营业期限','纳税人资质','所属行业','所属地区','登记机关','人员规模','参保人数','曾用名','英文名','进出口企业代码','注册地址','经营范围']
def getCompanyData(url,num):
    try:
        response = requests.get(url, headers=headers)
        response.encoding="utf-8"
        # print(response.text)
        html = etree.HTML(response.text)
        try:
            shehui_xinyong=html.xpath('//*[@id="cominfo"]/div[2]/table/tr[1]/td[2]/text()')[0]
        except:
            shehui_xinyong = None

        try:
            gongsi_name = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[1]/td[4]/text()')[0]
        except:
            gongsi_name = None

        try:
            fadingdaibiaoren = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[2]/td[2]/div/span[2]/span/a/text()')[0]
        except:
            fadingdaibiaoren = None

        try:
            dengjizhuangtai = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[2]/td[4]/text()')[0]
        except:
            dengjizhuangtai = None

        try:
            zhuceziben =  html.xpath('//*[@id="cominfo"]/div[2]/table/tr[3]/td[2]/text()')[0]
        except:
            zhuceziben = None

        try:
            shijiaoziben = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[3]/td[4]/text()')[0]
        except:
            shijiaoziben = None

        try:
            jigoudaima = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[4]/td[2]/text()')[0]
        except:
            jigoudaima = None

        try:
            gszucehao = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[4]/td[4]/text()')[0]
        except:
            gszucehao = None

        try:
            qiyeleix = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[5]/td[2]/text()')[0]
        except:
            qiyeleix = None

        try:
            yingyeqixian = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[5]/td[4]/text()')[0]
        except:
            yingyeqixian = None

        try:
            suoshuhangye = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[6]/td[2]/text()')[0]
        except:
            suoshuhangye = None

        try:
            suoshudiqu = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[6]/td[4]/text()')[0]
        except:
            suoshudiqu = None

        try:
            renyuanguimo = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[7]/td[2]/text()')[0]
        except:
            renyuanguimo = None

        try:
            canbaorenshu = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[7]/td[4]/span/text()')[0]
        except:
            canbaorenshu = None

        try:
            yingwenming = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[8]/td[2]/text()')[0]
        except:
            yingwenming = None

        try:
            zucedizhi = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[9]/td[2]/a[1]/text()')[0]
        except:
            zucedizhi = None

        try:
            jingyingfanwei = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[10]/td[2]/text()')[0]
        except:
            jingyingfanwei = None

        try:
            chengliriqi = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[2]/td[6]/text()')[0]
        except:
            chengliriqi = None

        try:
            hezhunriqi = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[3]/td[6]/text()')[0]
        except:
            hezhunriqi = None

        try:
            nashuiren = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[4]/td[6]/text()')[0]
        except:
            nashuiren = None

        try:
            nashuirenzizi = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[5]/td[6]/text()')[0]
        except:
            nashuirenzizi = None

        try:
            dengjijiguan = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[6]/td[6]/text()')[0]
        except:
            dengjijiguan = None

        try:
            cengyongm = html.xpath('//*[@id="cominfo"]/div[2]/table/tr[7]/td[6]/div/text()')[0]
        except:
            cengyongm = None

        try:
            jingchukou =  html.xpath('//*[@id="cominfo"]/div[2]/table/tr[8]/td[4]/text()')[0]
        except:
            jingchukou = None

        writer.writerow([shehui_xinyong,gongsi_name,fadingdaibiaoren,dengjizhuangtai,chengliriqi,zhuceziben,shijiaoziben,
                 hezhunriqi,jigoudaima,gszucehao,nashuiren,qiyeleix,
                 yingyeqixian,nashuirenzizi,suoshuhangye,suoshudiqu,dengjijiguan,
                 renyuanguimo,canbaorenshu,cengyongm,yingwenming,jingchukou,
                  zucedizhi,jingyingfanwei])
        print('第{}条------->>>'.format(num), gongsi_name)
        num += 1

        time.sleep(30)
    except:
        time.sleep(10)
        print('错误')
        pass
# a.append(title)
for j,i in enumerate(data.url):
    getCompanyData(i,j+1)
f.close()

print('successlly')
