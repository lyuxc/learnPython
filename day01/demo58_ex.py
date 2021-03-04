# coding=utf-8
'''
 实现类Monester
  ①在创建Monester类的时候，指定hp(默认值参数默认是1000)
  ②定义一个方法whoAmI,输出'我是monester'

 实现类Boss:
  继承自Monester,构造函数希望有两个，一个hp，一个name
    复写whoAmI，输出“我是Boss”

 分别去实例化Monester、Boss
 分别调用whoAmI方法
'''
if __name__ == '__main__':
    class Monester:
        def __init__(self, hp=1000):
            self.hp = hp

        def whoAmI(self):
            # print("我是Monester", self.hp)
            print("我是Monester 我的hp：%d" % self.hp)


    # 类进行实例化
    m1 = Monester(300)
    m1.whoAmI()


    # 封装一个类
    class Boss(Monester):
        def __init__(self, hp, name):
            self.hp = hp
            self.name = name

        def whoAmI(self):
            print("我是：%s 我的hp：%d" % (self.name, self.hp))


    b1 = Boss(500, 'jack')
    b1.whoAmI()
