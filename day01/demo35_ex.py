 # coding=utf-8
if __name__ == '__main__':
    def myFunc(num):
        s = 1

        # for方法
        # num +=1
        # for tmp in range(1,num):
        #     s *= tmp
        # return s

        # while方法
        # fact = 1
        # while True:
        #     if s < num:
        #         s += 1
        #         fact *= s
        #     else:
        #         return fact
        #         break

        # 递归方法
        if num == 1 or num == 0:
            return 1
        else:
            return num*myFunc(num-1)

    inputNum = int(input("输入阶乘数："))
    rs = myFunc(inputNum)
    print('阶乘结果：', rs)
