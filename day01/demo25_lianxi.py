if __name__ == '__main__':
    nowYear = int(input('输入年份:'))
    print(nowYear, type(nowYear))

    condition1 = nowYear % 4 == 0 and nowYear % 100 != 0
    condition2 = nowYear % 400 == 0

    result = condition1 or condition2
    print(result)
