# coding=utf-8
if __name__ == '__main__':
    # time
    # random
    # math
    num = 10.3
    print(num)

    # 向下取整
    import math
    print(math.floor(num))
    print(math.ceil(num))

    # 和文件、文件夹相关的处理和os相关的处理
    # os:operating system
    import os
    print(os.environ) #查看环境变量
    print(os.getlogin()) # 得到当前的登录用户
    # 获取当前目录的绝对路径
    print(os.path.abspath('.'))
    # 操作文件
    print(os.path.exists("./demo63.py"))