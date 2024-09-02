import mysql.connector
from mysql.connector import Error
from mysql.connector.constants import ClientFlag

# MySQL数据库连接配置
db_config = {
    'user': 'root',
    'password': '123456',
    'port': 3309,
    'host': '116.63.90.81',
    'database': 'hongzhi',
    'client_flags': [ClientFlag.LOCAL_FILES],
    'auth_plugin': 'mysql_native_password'
}


# 连接MySQL数据库
def connect():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            # print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f'Error: {e}')
        return None


# 读取最新数据
def read_latest_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dailyMeeting ORDER BY id DESC LIMIT 1;")
        result = cursor.fetchone()
        if result:
            print(f'Latest data: {result}')
            return result
    except Error as e:
        # print(f'Error: {e}')
        return None


# 主函数
def main():
    connection = connect()
    if connection:
        try:
            # 这里可以添加其他操作，如监视文件变化的代码

            # 读取最新数据
            read_latest_data(connection)
        finally:
            connection.close()
            print('Connection closed.')


if __name__ == "__main__":
    main()
