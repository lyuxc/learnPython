# coding=utf-8
myList = ['john','lucy','michale']
try:
    print(myList[3])
except IndexError:
    print('索引不存在')

str = "helloword"
num = 100
try:
    print(str+num)
except TypeError:
    print('不允许将整数和字符串进行拼接')