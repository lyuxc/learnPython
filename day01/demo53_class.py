# coding=utf-8
if __name__ == '__main__':
    # 类的封装和调用
    class Monester():
        # 定义构造函数
        def __init__(self, name, speed):
            # 将传来的数据保存在类的实例中
            self.mName = name
            # self.mSpeed = speed

            self.__mSpeed = speed

        # 定义一个自定义方法
        def run(self):
            print(self.mName + "正在以%d的速度跑..." % self.__mSpeed)


    # 调用
    m1 = Monester('jack', 30)
    m1.run()
    print(m1.mName)
