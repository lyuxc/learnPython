# coding=utf-8
# 常见数据类型，支持的api

# 数组
myList = [100,200,300,400]
# print(myList[10])
# print(len(myList)) #查询数组长度
myList.append(400) #尾部追加
# print(myList)
myList.insert(2, 60) #指定位置插入数据
# print(myList)
myList.pop() #移除最后一个元素
# print(myList)
myList.pop(1) #移除下标为1的元素
# print(myList)
myList[0] = 150 #修改指定下标的元素
# print(myList)
myList.sort(reverse=True) #sort方法在没有参数时默认升序
# print(myList)

myLists  = [10,20,15,30]
print(myList, type(myLists))

# 元祖的常见api
myTuple = (100,200,300)
print(myTuple,type(myTuple))
myNewTuple=(100,) #元组中只要1条数据的情况
print(myNewTuple,type(myNewTuple))
print(myTuple[1]) #读取元组中的数据
# max min
print(max(myTuple), min(myTuple))
 
# 字典常见API
myDict = {'stuName':'zhangsan','stuScore':80}
# 读取字典中某一个key的值 myDict.got('')
# 修改字典中某一个key对应的value
myDict['stuScore'] = 100
print(myDict)
# 添加一个新的键值对
myDict['stuSex'] = 'male'
print(myDict)
myDict.pop('stuScore')
print(myDict)
print(myDict.keys())
print(myDict.values())
print(myDict.items())