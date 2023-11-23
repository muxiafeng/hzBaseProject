import pymysql


def linkMysql(excuteSql):
    # 创建连接
    conn = pymysql.connect(host='117.50.187.15',  # 你的数据库地址
                           port=3306,
                           user='root',  # 你的数据库用户名
                           password='mysql123?',  # 你的数据库密码
                           db='testPrepare',  # 你的数据库名称
                           charset='utf8mb4',  # (可选) 数据库字符集,默认是utf8mb4
                           cursorclass=pymysql.cursors.DictCursor)  # 使用字典形式返回查询结果

    try:
        with conn.cursor() as cursor:
            # 执行SQL语句
            sql = excuteSql  # 替换为你的查询语句
            cursor.execute(sql)
            result = cursor.fetchall()  # 获取查询结果
            return result
            # for row in result:  # 遍历查询结果
            #     print(row)  # 打印每一行结果
    finally:
        conn.close()  # 关闭连接


if __name__ == '__main__':
    result = linkMysql('select count(1) from personinfo')
    print(result)
    for row in result:  # 遍历查询结果
        print(row)

    result1 = linkMysql('select * from personinfo limit 0,5')
    print(result1)
    for row1 in result1:  # 遍历查询结果
        print(row1)
