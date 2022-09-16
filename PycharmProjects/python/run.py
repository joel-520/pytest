import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
    # files_name = "./reports/report_"+str(int(time.time()))
    # os.mkdir(files_name)
    # time.sleep(3)
    # os.system("allure generate ./temps -o "+files_name+"./reports")
