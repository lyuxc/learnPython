 # coding=utf-8
if __name__ == '__main__':
    def factorial(num):
        s = 1

        # for方法
        # num +=1
        # for tmp in range(1,num):
        #     s *= tmp
        # return s

        # while
        fact = 1
        while True:
            if s < num:
                s += 1
                fact *= s
            else:
                return fact
                break

    inputNum = int(input("输入阶乘数："))
    rs = factorial(inputNum)
    print('阶乘结果：', rs)
    
