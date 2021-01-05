# 装饰圈本质是一个方法，它在python经常用力日志处理、性能测试、权限校验等场景

if __name__ == '__main__':
    # 定义装饰器函数
    def checkLogin(func):
        def handle():
            # 检查用户登录状态，假设登录成功
            print('检查用户登录状态，假设登录成功')
            func()
        return handle

    @checkLogin
    def addToCart():
        print('添加到购物车成功')
    addToCart()


    @checkLogin
    def modifyInfo():
        print('用户信息修改成功')
    modifyInfo()

