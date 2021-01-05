if __name__ == '__main__':
    def getList():
        # print('getList', u)
        userList = []

        def login(u):
            nonlocal userList
            # userList.append(u)
            userList.insert(0, u)
            return userList
            # print('login', userList)
        return login

    myFunc = getList()
    myFunc('michael')
    myFunc('jhon')
    myFunc('lucy')
    result = myFunc('Gin')
    print(result)

