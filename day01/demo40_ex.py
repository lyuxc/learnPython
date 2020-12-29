# coding=utf-8
if __name__ == '__main__':
    def maxMin(*args):
        print(args)
        # print(max(args), min(args))
        # python的返回值可以写多个，其实是存在元组中去返回的
        return max(args), min(args)
    res = maxMin(4, 6, 2, 8, 9)
    print(res)

    def myFunc(arg1, arg2, arg3):
        print(arg1, arg2, arg3)
    myFunc(100, 200, 300)
    myFunc(1, arg3=333, arg2=222)
