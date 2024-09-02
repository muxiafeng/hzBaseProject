import base64
import json
from datetime import datetime

import requests
from faker import Faker
from flask import Flask, jsonify, request, make_response

import getConfig
import util.connectMysql

app = Flask(__name__)
# api = Api(app)

# base = Namespace("base", description='base项目')

error_data = {
    'code': 0,
    'message': 'error'
}


# @base.route('/base')


@app.route('/', methods=['GET'])
def home():
    return 'HOME'


@app.route('/daletou', methods=['GET'])
def daletou():
    # 最近一期大乐透开奖时间和号码
    url = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1"
    response = requests.request("GET", url)
    if response.status_code != 200:
        status = response.status_code
        message = '获取失败'
    # print(response.status_code, response.content)
    content = json.loads(response.content)
    drawnum = content['value']['lastPoolDraw']['lotteryDrawNum']
    lastday = content['value']['lastPoolDraw']['lotteryDrawTime']
    luckynumber = content['value']['lastPoolDraw']['lotteryDrawResult']
    # print('第', drawnum, '期大乐透开奖时间：', lastday)
    # print('开奖号码为：', luckynumber)
    # print(str(luckynumber).replace(' ', ''))
    status = response.status_code
    message = '第' + drawnum + '期大乐透开奖时间：' + lastday + '，开奖号码为：' + luckynumber
    # print(message)
    data = {
        'code': status,
        'message': message
    }
    return jsonify(data)


@app.route('/personinfo', methods=['GET'])
def personinfo():
    fake = Faker()
    person = {
        'name': fake.name(),
        'phone': fake.phone_number(),
        'address': fake.address()
    }
    data = {
        'code': 200,
        'message': person
    }
    return jsonify(data)


@app.route('/newperson', methods=['GET'])
def newperson():
    fake = Faker()
    param1 = request.args.get('name')
    param2 = request.args.get('phone')
    if not param1 or param1.isdigit() or not param1.isalnum() or not param2.isdigit() or not param2:
        return error_data

    person = {
        'name': param1,
        'phone': param2,
        'address': fake.address()
    }
    data = {
        'code': 200,
        'message': person
    }
    # 返回一个包含两个参数的JSON响应
    return jsonify(data)


@app.route('/error', methods=['GET'])
def error():
    response = make_response(jsonify({'error': '未授权访问'}), 401)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/json', methods=['POST'])
def post1():
    json_data = request.get_json()

    # 遍历JSON数据中的键值对，将键值对拼接成字符串
    data_str = ""
    for key, value in json_data.items():
        data_str += key + ":" + str(value) + " "

    data = {
        'code': 200,
        'message': data_str
    }
    return jsonify(data)


# 假设这是我们的用户数据库
users = {
    "user1": "password1",
    "user2": "password2",
}

# 模拟cookie存储
cookies = {}


@app.route('/login', methods=['POST'])
def login(users=None):
    data = request.get_json()  # 获取POST数据
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        # 模拟设置cookie
        mess = username + "loginSuccess"
        # 将数据转换为 bytes 类型
        data_bytes = mess.encode('utf-8')
        # 使用 base64 对数据进行加密
        encoded_data = base64.b64encode(data_bytes)
        cookie = "base64=" + encoded_data.decode('utf-8')
        return jsonify({'code': 200, 'message': "登录成功！"}), 200, {'Set-Cookie': cookie}
    else:
        return jsonify({'code': '401', 'message': 'Invalid username or password'}), 401


@app.route('/authenticate', methods=['GET'])
def authenticate(users=None):
    cookie = request.cookies.get("base64")
    # print(cookie)
    # 将数据转换为 bytes 类型
    encoded_data_bytes = cookie.encode('utf-8')
    # 使用 base64 对数据进行解密
    decoded_data = (base64.b64decode(encoded_data_bytes)).decode('utf-8')
    # print(decoded_data)  # 输出解密后的数据
    if "loginSuccess" in decoded_data and decoded_data.replace("loginSuccess", "") in users:
        return jsonify(
            {'code': 200, 'message': "鉴定" + decoded_data.replace("loginSuccess", "") + "登录成功！"}), 200
    else:
        return jsonify({'status': 'failed', 'message': 'Invalid cookie'}), 401


@app.route('/dailyMeeting', methods=['GET'])
def dailyMeeting():
    # 执行数据库查询
    result = util.connectMysql.connect_mysql('select * from dailyMeeting order by time desc limit 1;')
    # print(result)
    # print('id', result[0][0])
    # print('message', result[0][1])
    # print('time', result[0][2])
    # print('user', result[0][3])
    data = {
        'code': 200,
        'message': result[0]
    }
    return jsonify(data)


@app.route('/dailyEnglishWords', methods=['GET'])
def dailyEnglishWords():
    today = datetime.now().strftime("%Y-%m-%d")

    result = util.connectMysql.connect_mysql(
        f"SELECT word,wordexplain FROM englishword where tag =1 and time='{today}' LIMIT 10;")
    data = {
        'code': 200,
        'message': result
    }
    return jsonify(data)


@app.route('/sendNotification', methods=['POST'])
def sendNotification(users=None):
    data = request.get_json()  # 获取POST数据
    to = data.get('toMan')
    text = data.get('text')

    flag = True
    if 'hongzhi' in to:
        key = getConfig.get_config('ios', 'hongzhi_key')
    elif 'tingting' in to:
        key = getConfig.get_config('ios', 'tingting_key')
    else:
        response = make_response(jsonify({'error': '发送失败'}), 200)
        flag = False

    if flag is not False:
        url = f'https://api2.pushdeer.com/message/push?pushkey={key}&text={text}'

        res = requests.request('GET', url=url)

        print(res.content)
        if res.status_code == 200:
            data = {
                'code': 200,
                'message': 'send success!'
            }
        return jsonify(data)

# api.add_namespace(base, '/base')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
