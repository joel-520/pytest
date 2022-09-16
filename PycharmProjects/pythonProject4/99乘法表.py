
#
# for i in range(1,10):
#     # print('i')#多少行
#     for j in range(1,i+1):
#         # print('j')
#         print('%s * %s = %s' %(i,j,i*j),end='')
#         print('\n')



# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

