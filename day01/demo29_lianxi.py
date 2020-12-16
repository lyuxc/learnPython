# coding=utf-8
if __name__ == '__main__':
    count = 0
    for tmp in range(1, 4):
        count += int(input("输入第%d个成绩:" % tmp))
    averageScore = count / 3
    print("averageScore：", averageScore)

    if averageScore >= 90:
        print("A")
    elif averageScore >= 80:
        print("B")
    elif averageScore >= 60:
        print("C")
    else:
        print("D")
