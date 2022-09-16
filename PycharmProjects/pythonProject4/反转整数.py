#!/usr/bin/python
# -*- coding: UTF-8 -*-

class  Solution(object):
    def  reverse(self,x):
        if  -10<x<10:
            return  x
            str_x  =  str(x)
        if  str_x[0]  !="-":
            str_x  =  str_x[::-1]
            x  =  int(str_x)
        else:
            str_x  = str_x[1:][::-1]
            x  =  int(str_x)
            x  = -x
            return  x
        if  -2147483648<x<2147483647:
            return x
        else:
            0


            s  =  Solution()
            reverse_int  = s.reverse(-120)
re=reverse_int
print(re)