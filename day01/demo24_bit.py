# coding=utf-8
if __name__ == '__main__':
    a = int('00111100', 2)
    b = int('00001101', 2)
    print(a, b)
    print("按位与", a & b)
    print("按位或", a | b)
    print("异或", a ^ b)
    print("按位取反", ~b)
