from flask import Flask, jsonify, request, make_response
from util import cjson
import requests
import json
from faker import Faker

app = Flask(__name__)

error_data = {
    'code': 0,
    'message': 'error'
}


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
