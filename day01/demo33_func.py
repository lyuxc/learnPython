# coding=utf-8
if __name__ == '__main__':
    # 定义方法
    # def myFunc():
    #     print("方法被调用了")
    # # 调用方法
    # myFunc()

    # 实现一个方法：得有两个参数，返回参数相加之和
    def add(num1, num2):
        result = num1 + num2
        return result

    count = add(56, 45)
    print("count:", count)
