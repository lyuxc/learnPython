# coding=utf-8

# 如何捕获程序中出现的错误，进行错误处理，防止程序crash 退出

try:
    print(myName)
except NameError:
    print('变量名不存在，不能直接调用')