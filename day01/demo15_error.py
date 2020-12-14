# coding=utf-8

# NameError: 调用不存在的变量
# print(myName) 

# SyntaxError: 语法错误
# print()) 

# IndexError: 下标有问题
myList = [1,2,3,4,5]
# print(myList[20]) 

# KeyError: key值有问题
myDict = {"stuName":"lucy","age":20}
# print(myDict['stuSex']) 

# ValueError
# int(myDict.get('stuName'))

# AttributeError: 属性错误 调用了不存在的属性
age = 10
# age.append(20)

# IndentationError: 缩进错误
