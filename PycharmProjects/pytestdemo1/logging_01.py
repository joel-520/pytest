# -*- coding: utf-8 -*-
# @Time : 2022/7/9 16:21
# @Author : joel
# @Email : 770546904@qq.com
# @File : logging_01.py



import logging



"""

#开始使用log功能
logging.debug(‘这是DEBUG等级的信息’)
logging.info(‘这是INFO等级的信息’)
logging.warning(‘这是WARNING等级的信息’)
logging.error(‘这是ERROR等级的信息’)
logging.caitical(‘这是CRITICAL等级的信息’)


创建日志收集器对象logging.getLogger
logger = logging.getLogger(‘123’) #创建logger对象
logger.setLevel(‘DEBUG’) #指定logger对象手机的loggin信息等级

loggin中默认的日志收集器为root，收集等级为Warning

1、输出到控制台

import logging

# 1：创建一个日志收集器
logger = logging.getLogger(‘123’)  # 创建logger对象
logger.setLevel(‘DEBUG’)  # 指定logger对象手机的loggin信息等级

# 2：创建一个输出渠道，输出到控制台
sh = logging.StreamHandler()
sh.setLevel(‘DEBUG’)  # 设定输出到控制台的log信息等级

# 3：将收集渠道添加到收集器中
logger.addHandler(sh)

"""
# 1：创建一个日志收集器
logger = logging.getLogger('')  # 创建logger对象
logger.setLevel('logging.INFO')  # 指定logger对象手机的loggin信息等级

# 2：创建一个handler，用来写入日志文件
file_handler = logging.FileHandler('./ log.txt', mode ='a')  # 指定打开文件的方式
file_handler.setLevel(logging.DEBUG)  # 设定写入到文件的log信息等级

# 3：创建一个handler用来输出到屏幕
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)