# coding=utf-8
if __name__ == '__main__':
    # 和身份相关的运算符
    # in not in is id
    myList = [100, 200, 300, 400, 500]

    # print(100 in myList)
    # print(100 not in myList)

    num1 = 10
    num2 = 10
    num3 = num2
    print(id(num1), id(num2), id(num3))
    print(num1 is num2)  # true
    print(num3 is num2)  # true

    myTuple1 = (1, 2, 3)
    myTuple2 = (1, 2, 3)
    myTuple3 = myTuple2
    print(id(myTuple1), id(myTuple2), id(myTuple3))
    print(myTuple1 is myTuple2)  # false
    print(myTuple3 is myTuple2)
