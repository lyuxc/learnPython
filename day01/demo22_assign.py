# coding=utf-8
# 赋值运算符
# += -=
num1 = 10
num2 = 20

myList = [10,20]
[num3,num4] = myList
print(num3,num4)

num3+=1
print(num3)

# 不支持：自增、自减
# num4++