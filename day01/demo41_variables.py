# coding=utf-8


# class a:
#
#     def test(self):
#         print(11)
#
# def test2():
#     print(2)

if __name__ == '__main__':
    # 全局
    count = 10

    def modifyCount():
        global count
        # 局部
        # count = 0
         myCount = 3
        count += 1
        print("in func count is %d" % count)


    print("count is %d" % count)
    modifyCount()
    print("count is %d" % count)
    # print(myCount)

    # c = a()
    # c.test()
    # test2()
