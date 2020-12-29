# coding=utf-8
if __name__ == '__main__':

    def indexOf(myList, item, start=0):
        for tmp in range(start, len(myList)):
            if item == myList[tmp]:
                return tmp
        # 如果for循环结束，返回-1
        return -1

    myArray = ['a', 'b', 'c', 'd', 'e']
    rs = indexOf(myArray, 'd')
    print('rs', rs)
