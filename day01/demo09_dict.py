# coding=utf-8
# 字典

myDict = {"name":"zhangsan","age":20}

print(myDict, type(myDict))
print(myDict['age'])
# print(myDict['ages'])
print(myDict.get('age'))
# print(myDict.get('ages'))

myDict.get('age') = 22
print(myDict)