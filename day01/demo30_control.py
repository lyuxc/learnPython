# coding=utf-8

myList = [10, 11, 12, 13, 14]

# for tmp in myList:
#     if tmp % 2 == 0:
#         # 直接进入到下次循环
#         continue
#     print(tmp)

# 变量大于12 结束循环
for tmp in myList:
    if tmp > 12:
        break
    print(tmp)

