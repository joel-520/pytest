import pandas as pd
import matplotlib.pyplot as plt

students=pd.read_excel(r'C:\Users\ASUS\Desktop\MLCode\student.xlsx')
students.sort_values(by='Score',inplace=True,ascending=False)
plt.bar(students['Name'],students.Score,color='orange')
plt.title('Student score')#名称是学生分数
plt.xlabel('Name')#横坐标是name
plt.ylabel('score')#纵坐标是score
plt.xticks(students.Name,rotation='90')#学生名旋转90读
plt.tight_layout()
plt.show()

#中文
import pandas as pd
import matplotlib.pyplot as plt

students=pd.read_excel(r'C:\Users\ASUS\Desktop\MLCode\student.xlsx')
students.sort_values(by='Score',inplace=True,ascending=True)
# add chinese character support
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"C:\Windows\Fonts\AdobeSongStd-Light.otf",size=16)
plt.bar(students['Name'],students.Score,color='orange')
plt.title('学生分数：',FontProperties=font)
plt.xlabel('名字',FontProperties=font)
plt.ylabel('分数',FontProperties=font)
plt.xticks(students.Name,rotation='90')
plt.tight_layout()
plt.show()



#叠加柱状图
import pandas as pd
import matplotlib.pyplot as plt

stu=pd.read_excel(r'C:\Users\ASUS\Desktop\MLCode\threemon.xlsx')#读文件
stu['sum']=stu['Begin']+stu['Middle']+stu['Final']#求各时期考试和
stu.sort_values(by='sum',inplace=True)#排序
stu.plot.barh(x='Name',y=['Begin','Middle','Final'],stacked=True)#stack可实现叠加
plt.tight_layout()
plt.show()
