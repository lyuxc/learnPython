# coding=utf-8
if __name__ == '__main__':
    # 封装
    class Student():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def study(self):
            print("姓名: %s, 年龄：%d" % (self.name, self.age))

    m1 = Student('Gin', 18)
    m1.study()
    print(m1.name, m1.age)