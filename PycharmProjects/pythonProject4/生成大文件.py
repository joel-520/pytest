import time


def creatfilesize(n):
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_name = "E:\\" + str(local_time) + ".docx"
    bigFile = open(file_name, 'w')
    bigFile.seek(1024 * 1024 *  n)
    bigFile.write('test ，看到我了么？')
    bigFile.write("test，结束了吗？")
    bigFile.close()
    print
    "ALL down !"


if __name__ == '__main__':
    n = int(input("input:"))
    creatfilesize(n)
