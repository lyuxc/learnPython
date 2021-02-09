# coding=utf-8
# python 一个文件就是一个模块
# if __name__ == '__main__':
def test():
    print("module1中的test方法被调用了")

count = 0

def modifyCount():
    global count
    count+=1
    print("count is %d"%count)