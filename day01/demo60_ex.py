# coding=utf-8
# 练习: demo60_lianxi.py
# ①连接数据库xz
# ②获取xz_index_product表的数据，将每一行的title整理在一个数组中
if __name__ == '__main__':
    import mysql.connector as conn

    myConnection = conn.connect(host="localhost", user='root', passwd='root', database='xz')

    print('connect', myConnection)

    myCursor = myConnection.cursor()

    # sql = "select * from xz_index_product"
    sql = "select title from xz_index_product"
    myCursor.execute(sql)

    res = myCursor.fetchall()

    print('res', type(res), res)

    myList = []

    for tmp in res:
        myList.append(tmp[0])
        # print(tmp['title'])

    print('myList', myList)