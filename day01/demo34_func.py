# coding=utf-8
if __name__ == '__main__':
    # 传参
    # def testFunc(arg1):
    #     arg1 -= 1
    #     return arg1
    #
    # count = 11
    # newCount = testFunc(count)
    # print(count, newCount)

    # myFunc有一个参数，类型是字典，包含一个键值对 'myCount': 10

    def myFunc(arg1):
        arg1['myCount'] -= 1

    myDict = {'myCount': 10}
    myFunc(myDict)
    print(myDict)

    # 值传递：修改参数，原始数据不受影响 number/string/tuple
    # 引用传递：修改参数，原始数据也会变化 list/set/dict

