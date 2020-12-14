# coding=utf-8

cityList = ['gz', 'sz', 'dg']
print(cityList[2])
 
uname = raw_input("请输入用户名:")

upass = raw_input("请输入密码:")

myInfo = {"username": uname, "password": upass}

print(myInfo)

print(myInfo.get('username'))
print(myInfo.get('password'))