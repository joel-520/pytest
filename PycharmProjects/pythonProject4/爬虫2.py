import requests
import bs4
import os
import datetime
import time
import json


def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def saveFile(content, path, filename):
    '''
    功能：将文章内容 content 保存到本地文件中
    参数：要保存的内容，路径，文件名
    '''
    # 如果没有该文件夹，则自动生成
    if not os.path.exists(path):
        os.makedirs(path)
        # 保存文件
    with open(path + filename, 'w', encoding='utf-8') as f:
        f.write(content)

def download_jfrb(year, month, day, destdir):
    '''
    功能：网站 某年 某月 某日 的新闻内容，并保存在 指定目录下
    参数：年，月，日，文件保存的根目录
    '''
    url = 'https://www.shobserver.com/staticsg/data/journal/' + year + '-' + month + '-' + day + '/navi.json'
    html = fetchUrl(url)
    jsonObj = json.loads(html)

    for page in jsonObj["pages"]:
        pageName = page["pname"]
        pageNo = page["pnumber"]
        print(pageNo, pageName)
        for article in page["articleList"]:
            title = article["title"]
            subtitle = article["subtitle"]
            pid = article["id"]
            url = "https://www.shobserver.com/staticsg/data/journal/" + year + '-' + month + '-' + day + "/" + str(
                pageNo) + "/article/" + str(pid) + ".json"
            print(pid, title, subtitle)

            html = fetchUrl(url)

            cont = json.loads(html)["article"]["content"]
            bsobj = bs4.BeautifulSoup(cont, 'html.parser')
            content = title + subtitle + bsobj.text
            print(content)

            path = destdir + '/' + year + month + day + '/' + str(pageNo) + " " + pageName + "/"
            fileName = year + month + day + '-' + pageNo + '-' + str(pid) + "-" + title + '.txt'
            saveFile(content, path, fileName)

if __name__ == '__main__':
                '''
主函数：程序入口
                '''
    # 爬取指定日期的新闻
newsDate = input('请输入要爬取的日期（格式如 20210416 ）:')
year = newsDate[0:4]
month = newsDate[4:6]
day = newsDate[6:8]
download_jfrb(year, month, day, 'Data')
print("爬取完成：" + year + month + day)