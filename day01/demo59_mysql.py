# coding=utf-8
if __name__ == '__main__':
    # 引入安装的mysql-connector所提供的模块
    import mysql.connector as conn

    # 准备建立连接
    myConnection = conn.connect(host='localhost', user='root', passwd='root', database='xz')

    print('connect', myConnection)

    # 创建一个可以执行sql操作的游标对象
    # myCursor = myConnection.cursor() #元祖
    myCursor = myConnection.cursor(dictionary=True)

    # 执行sql
    # myCursor.execute('select * from xz_user')

    # 获取查询到的数据集合
    # res = myCursor.fetchall()
    # print('res', res)

    # 通过sql语句 修改数据库中的数据
    sql = "insert into xz_user (uname,upwd,email) values ('zhangsan', '123456', 'zhangsan@zs.com')"
    myCursor.execute(sql)

    print("成功修改了%d行 最后的id是%d"%(myCursor.rowcount,myCursor.lastrowid))

    # myConnection.commit()