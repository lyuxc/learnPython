# coding=utf-8
if __name__ == '__main__':
    # python闭包
    def sum(a):
        print('a', a)
        def add(b):
            print('b', b)
            return a+b
        return add

    funcAdd = sum(10)
    rs = funcAdd(5)
    print('rs', rs) 

    # 局部：不会被污染，但不可重用
    # 全局：可被重用，但被污染
    # 重用变量，又保护变量