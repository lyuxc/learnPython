if __name__ == '__main__':
    def add(num1, num2):
        result = num1 + num2
        return result

    print(add(3, 6))

    addFunc = lambda num1, num2: num1 + num2
    print(addFunc(3, 5))

    test = lambda:print('it is a test')
    test()
