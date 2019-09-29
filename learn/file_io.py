#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
#raw_input 函数
str = raw_input("plz input:")
print "your inputing is ",str

#input函数  // input函数和raw_input函数类似，但是它可以接受一个Python表达式作为输入，并将运算结果返回
str = input("请输入：")
print "你输入的内容是：",str
"""
#open函数
test_name = r"E:\pycharm\learn\for range.py"
test_fo = open(test_name,"a+")
test_file = test_fo.read()
print(test_file)
test_fo.close()
test_fo = open(test_name,"a+")
test_fo.write("\nThis is write test for practicing\n")
test_fo.close()
test_fo = open(test_name,"a+")
test_file = test_fo.read()
print(test_file)
test_fo.close()