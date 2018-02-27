#!/usr/bin/env python
#  -*- coding:UTF-8 -*-
def printme(str):
    "打印传入的字符串到标准显示设备上"
    print str;
    return;
#调用函数
printme("woyaodiaoyong")
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print b

def Changeme( mylist ):
    "修改传入的列表"
    mylist.extend([23,[1,2,3,4]]);
    #print "函数内取值",mylist
    return
#调用Changeme函数
print "实例化extend方法"
mylist = [10,20,30];
Changeme( mylist );
print "函数外取值：",mylist

def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print "print:"
    print arg1
    for var in vartuple:
        print var
    return;
print (19);
print (70,89,90);

#全局变量和局部变量
total = 0;
def sum(arg1,arg2):
    "返回2个参数的和。"
    total = arg1 + arg2;
    print "函数内饰局部变量：",total
    return total;
sum (10,30);
print "函数外事全局变量：" , total
x = 1
y = 2
def b(y):
    return x+y
def a(x):
    return b
print a(10)
print b(20)