# -* - coding: UTF-8 -* -

import logging

logger = logging.getLogger()

handler = logging.FileHandler("d:\\log.txt")
logger.addHandler(handler)

# Formatter的文档说明。这里有三项：时间，信息级别，日志信息
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

# 设置日志输出的级别，  写入日志时，小于指定级别的信息将被忽略。
# 因此为了输出想要的日志级别一定, 要设置好此参数。这里我设为NOTSET（值为0），也就是想输出所有信息
logger.setLevel(logging.NOTSET)

# 日志信息有好几个级别。 debug, info, warning, error, critical
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")