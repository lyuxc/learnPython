if __name__ == '__main__':
    def outer():
        count = 0

        def inner():
            nonlocal count
            count+=1
            print("count is %d" % count)
        return inner

    myFunc = outer()
    myFunc()
