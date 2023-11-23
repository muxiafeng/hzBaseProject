import configparser


def configGet(section_name, option_name):
    # 创建ConfigParser对象
    config = configparser.ConfigParser()

    # 读取config.ini文件
    config.read('config.ini')

    # 获取配置信息
    option_value = config.get(section_name, option_name)
    return option_value
    # print(option_value)
