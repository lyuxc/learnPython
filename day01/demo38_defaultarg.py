# coding=utf-8
if __name__ == '__main__':
    # 默认值参数:调用方法，如果传参，以实际参数为准，如果没有，以默认值为准
    def myFunc(arg1, arg2=20):
        print(arg1, arg2)

    myFunc(10)  # 10 20
    myFunc(10, 30)  # 10 30

    # SyntaxError: non-default argument follows default argument
    def testFunc(arg1=30, arg2):
        print(arg1, arg2)
    # testFunc(20, 50)