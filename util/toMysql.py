import pymysql


def tomysql():
    conn = pymysql.connect(
        host='117.50.187.15',
        port=3306,
        user='root',
        password='mysql123?',
        database='testPrepare',
        charset='utf8'
    )
    print(conn)
    cursor = conn.cursor()
    result = cursor.execute('select count(1) from testPrepare.personinfo limit 10')
    print(result)
    conn.close()


if __name__ == '__main__':
    tomysql()
