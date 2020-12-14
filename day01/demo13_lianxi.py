# coding=utf-8

list = []

sc1 = raw_input("第一次输入:")
sc2 = raw_input("第二次输入:")
sc3 = raw_input("第三次输入:")
# list.append(sc1)
# list.append(sc2)
# list.append(sc3)
list = [sc1,sc2,sc3]
 
print(list)
list.pop(2)
print(list)