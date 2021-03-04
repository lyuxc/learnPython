# coding=utf-8
if __name__ == '__main__':
    # 引入
    import mysql.connector.pooling as pooling

    # 创建连接池
    config = {
        "host": "localhost",
        "user": "root",
        "passwd": "root",
        "database": "xz"
    }

    pool = pooling.MySQLConnectionPool(pool_size=10, **config)

    # 连接
    myConn = pool.get_connection()

    # 创建游标对象
    myCursor = myConn.cursor()

    # 执行sql操作 处理结果
    myCursor.execute("select * from xz_user")
    print(myCursor.fetchall())