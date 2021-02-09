# coding=utf-8
if __name__ == '__main__':
    # 类的继承在python的实现方式

    class Monester:
        def run(self):
            print("正在奔跑。。。。")

    class Boss(Monester):
        def test(self):
            pass

    # 实例化Boss得到一个实例
    b1 = Boss()
    b1.run()
