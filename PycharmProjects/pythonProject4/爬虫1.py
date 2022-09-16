#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import os


def dowmloadPic(html, keyword, i):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

    abc = i * 60
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(abc) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        dir = r'D:\image\i' + keyword + '_' + str(abc) + '.jpg'
        if not os.path.exists('D:\image'):
            os.makedirs('D:\image')

        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        abc += 1


if __name__ == '__main__':
    # word = input("Input key word: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    name = input('输入下载图片的名字')
    num = 0
    x = int(input('您要爬取几张呢?,n*60'))

    for i in range(0,int(x)):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word==' + name + '+&pn=' + str(i * 30)
        result = requests.get(url, headers=headers)
        dowmloadPic(result.content.decode(), name, i)
    print("下载完成")



