
'''
正则表达式
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''
import re
re.match(pattern, string, flags=0)

import re
data='python'
parrtern='..'#匹配规则，这里匹配两个字符
res=re.match(parrtern,data)
print(res.group())#输出：py
'''测试二'''
names='运智在学习python','运气','换人'
pattern='运.'#匹配规则：会匹配运开头的
for item in names:
    chen=re.match(pattern,item)
    if chen:
        print(chen.group())#输出运智，运气
