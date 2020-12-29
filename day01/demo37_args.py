# coding=utf-8
if __name__ == '__main__':
    # 可变长参数

    def test(*myArgs):
        print(myArgs)

    # test()
    # test(1)
    # test(1, 2)
    # test(1, 2, 3)

    def myFunc(arg1, *myArgs):
        print(arg1, myArgs)

    # myFunc()
    # myFunc(1)  # 1 ()
    # myFunc(1, 2, 3, 4, 5)  # 1 (2, 3, 4, 5)

    def testFunc(**myArgs):
        print(myArgs,type(myArgs))
    testFunc(a=1, b=2, c=3)
