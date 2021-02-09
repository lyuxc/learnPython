# coding=utf-8
if __name__ == '__main__':

    class Car():
        def __init__(self, brand):
            self.brand = brand
        def drive(self):
            print("汽车正在行驶..." + self.brand)

    class SUV(Car):
        # pass
        # def __init__(self, brand):
        #     self.brand = brand
        def drive(self):
            print("汽车正在行驶...--------"+self.brand)

    c1 = SUV('volvo')
    c1.drive()

