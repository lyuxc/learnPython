# coding=utf-8
myScore = '90'
# 将字符串转为数字：
# 将数字转字符串 str()
newScore = int(myScore)
print(newScore, type(newScore))
# list tuple
nameList = ['zhangsan', 'jhon', 'michale']
myTuple = tuple(nameList) #将数组转换为元祖
print(myTuple, type(myTuple))
myList = list(myTuple) #将元祖转换为数组
print(myList, type(myList))

# list = [1,2,3]
myTuple2 = list((100,200,300))
print(myTuple2, type(myTuple2))

# 隐式类型转换
age = 10
isStudent = True
print(age+isStudent)

