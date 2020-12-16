# coding=utf-8
if __name__ == '__main__':
    import random  # 随机模块

    # randomnum = random.choice(range(0, 100)) # num得到随机数

    num = random.randint(0, 100)  # num得到随机数
    # print("随机数", num)
    iNum = 0

    while True:
        iNum = int(input("请输入一个数字："))
        if iNum > num:
            print("太大了")
        elif iNum < num:
            print("太小了")
        else:
            print("猜对了!!!!!!")
            break

# number = []  # 创建一个列表
# for i in range(0, 100):  # 循环随机数100位
#     num = random.randint(0, 100)  # num得到随机数
#     number.append(num)  # append是添加 随机数添加到number列表
# print(number)
