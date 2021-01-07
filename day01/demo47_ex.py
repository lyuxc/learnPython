if __name__ == '__main__':
    # 定义装饰器函数
    def log(func):
        def myHandle(num1, num2):
            # 检查用户登录状态，假设登录成功
            print('方法被调用了')
            func(num1, num2)
        return myHandle

    @log
    def add(num1, num2):
        result = num1 + num2
        print('求和:%d' % result)
    add(12, 2)
