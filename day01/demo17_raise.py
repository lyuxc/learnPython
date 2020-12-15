# coding=utf-8
# 手动触发错误，并自定义错误信息内容
try:
    print('it is a test')
    raise(NameError("出错了"))
    # raise(NameError,{"code":1})
    # print(myName)
except NameError as msg:
    print(msg)
    print('已经进入错误处理流程')