# coding=utf-8
if __name__ == '__main__':
    # 关键字参数
    def myFunc(arg1, arg2):
        print("a1: ", arg1)
        print("a2: ", arg2)
    # myFunc(10, 20)
    # 关键字参数，在方法的调用过程中，是可以通过keyValue指定关键字参数，调整穿参顺序
    # myFunc(arg2=30, arg1=50)
    myFunc(16, arg2=22)
    # myFunc(99, arg2=88)