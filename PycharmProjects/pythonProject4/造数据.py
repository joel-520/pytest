#coding:utf_8
import numpy as np
import pandas as pd


def main():
    list1 = [['西瓜', '兰州', 'first', 20], ['香蕉', '西安', 'second', 30], ['苹果', '银川', 'third', 40],
             ['桔子', '四川', 'fourth', 40]]
    output = open('data.xls', 'w', encoding='gbk')
    output.write('fruit\t place\t digital\t number\n')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            output.write(str(list1[i][j]) + ' ')
            output.write('\t')
        output.write('\n')
    output.close()


if __name__ == '__main__':
    main()

   # 采用numpy将数据写入.txt文件，代码如下：
list2 = [[1,2,3],[4,5,6]]
np.savetxt('data.txt',list2,fmt='%.2f')


#采用pandas导入数据
list1 = [[1,2,3],[4,5,6]]
df = pd.DataFrame(list1)
df.to_csv("test.csv",sep=',',header=False,index=False)