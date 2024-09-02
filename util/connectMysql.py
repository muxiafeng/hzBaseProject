import mysql.connector
from mysql.connector import Error

# 配置数据库连接参数
host = '116.63.90.81'  # 数据库地址，对于远程数据库，指定为IP地址
port = 3309
database = 'hongzhi'  # 数据库名
user = 'root'  # 数据库用户名
password = '123456'  # 数据库密码


def connect_mysql(ex_sql):
    # 连接到MySQL数据库
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        # 检查连接是否成功
        if connection.is_connected():
            # 创建一个cursor对象，使用它来执行SQL语句
            cursor = connection.cursor()
            # print("成功连接到MySQL数据库")

            # 执行SELECT语句
            query = ex_sql  # 替换为你的表名和查询条件
            cursor.execute(query)

            # 获取查询结果
            records = cursor.fetchall()
            # print(records[0])
            return records

    except Error as e:
        print("连接或查询失败:", e)
        return None
    finally:
        # 关闭cursor和connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL连接已关闭")


if __name__ == '__main__':
    res = connect_mysql('select * from dailyMeeting limit 1;')
    print(res[0][1])
