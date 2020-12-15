# coding=utf-8

# 如何捕获程序中出现的错误，进行错误处理，防止程序crash 退出

# try:
#     print(myName)
# except NameError:
#     print('变量名不存在，不能直接调用')
# finally:
#     print("it is a test")

# 如何捕获多个错误
myList = ["lucy", "john", "Gin"]

# myIndex = input('要读取的下标: ')

try:
    myIndex = input('要读取的姓名的下标: ')
    # 将输入的下标字符串转换为数字类型  
    myNum = int(myIndex)
    print(myList[myNum])
except Exception:
    print('程序错误')
# except (IndexError,ValueError):
#     print('下标错误,格式错误')
# except IndexError:
#     print('下标错误')
# except ValueError:
#     print('输入格式错误')
# except NameError:
#     print('输入错误')
# except SyntaxError:
#     print('语法错误')