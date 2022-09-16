In [17]: path='C:\\Users\\ASUS\\Desktop\\MLCode\\people.xlsx'

In [18]: people=pd.read_excel(path,sheet_name='Sheet1')

In [19]: people
Out[19]:
   id name  age
0   1    张   19
1   2   李四   20
2   3   王五   21

In [20]: people.sort_values(by='age',ascending=False,inplace=True)
#inplace表示就地，直接修改people，若为FALSE则会返回一个对象，对people本身不会修改
In [21]: print(people)
   id name  age
2   3   王五   21
1   2   李四   20
0   1    张   19
