# coding=utf-8
if __name__ == '__main__':
    # 循环控制
    myList = [100, 200, 300, 400, 500]
    for tmp in myList:
        print(tmp)  # tmp是遍历数组时对应的临时变量

    # range函数：range(start,stop[,stop]) 生产一个序列，存储从start开始，到stop结束的数据
    # for tmp in range(5, 10):
    # print(tmp)  # 5 6 7 8 9

    # 遍历数组时，有时需要获取遍历时的下标？
    for tmp in range(0, len(myList)):
        print("下标为:%d 数据是:%d" % (tmp, myList[tmp]))
