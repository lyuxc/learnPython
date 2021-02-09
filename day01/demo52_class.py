# coding=utf-8
# 在python中 类的封装和调用的方式
if __name__ == '__main__':

    # 创建一个类
    class Prdouct:
        price = 0
        def check(self):
            print("正在获取商品信息")

    # 实现一个类的对象
    p = Prdouct()
    print(p)
    p.check()