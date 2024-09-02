import configparser


def get_config(part, key):
    # 创建一个ConfigParser对象
    config = configparser.ConfigParser()

    # 读取INI文件
    config.read('config/config.ini')

    # 获取默认部分的一个值
    server_alive_interval = config.get(part, key)
    print(server_alive_interval)
    return server_alive_interval


if __name__ == '__main__':
    get_config('ios', 'hongzhi_key')
