# -*- coding: utf-8 -*-
# @Time : 2022/9/6 9:19
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: /run
# @Describe: ...
import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    files_name = "./reports/report_"+str(int(time.time()))
    os.mkdir(files_name)
    time.sleep(3)
    os.system("allure generate ./temps -o "+files_name+". --clean")