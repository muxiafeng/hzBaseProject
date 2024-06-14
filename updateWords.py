from datetime import datetime

from util.connectMysql import connect_mysql

today = datetime.now().strftime("%Y-%m-%d")

last_data_sql = "SELECT count(1) from englishword where tag!=1;"
last_data_count = connect_mysql(last_data_sql)
print(last_data_count[0][0])

if int(last_data_count[0][0]) < 10:
    connect_mysql("update englishword SET time ='',tag ='',q1 ='';")

# 10条数据
words_sql_10 = "SELECT word FROM englishword where tag !=1  ORDER BY rand() LIMIT 10;"
words_10 = connect_mysql(words_sql_10)
for word in words_10:
    print(word[0])
    connect_mysql(f"UPDATE englishword SET time = '{today}',tag = 1 WHERE word ='{word[0]}';commit;")

# res = connect_mysql(f"SELECT word,wordexplain FROM englishword where tag =1 and time='{today}' LIMIT 10;")
# print(res)
