# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = '东方头条【【热】在大型晚会上，你以为歌手耳朵里带的是“耳机”吗？看完-涨-知-识-了-】https://mini.eastday.com/mobile/190103192455115.html?ca=809169121&f1=xq2'
    send_text1 = '在大型晚会上，你以为歌手耳朵里带的是“耳机”吗？看完-涨-知-识-了'
    qun_name_list = ['正定网-买卖交易', 'ATX(AutomatorX) old', '北京化妆师交流群', '珠三角高级化妆师群', '重庆软件测试交流群', '南京软件测试交流群',
                     '长沙软件测试交流群'] #群名称
    qun_name_list1 = ['兄弟汇', '没有一辈子游戏', '路遇行人', 'Microsoft问题交流', '190933303', '微博热门实时推广精选', '输了你赢了全世界又如',
                     '湖南化妆师-新年快乐', '新娘化妆师交流(一)', '杭州化妆师交流群', '山西化妆师交流1群']
    index = 0 #调用发送图片的方法
    text = 1 #代表发送文本消息

    desired_caps = {'platformName': 'Android',
                    'platformVersion': '6.0.1',
                    'deviceName': 'xiaomi',
                    'udid': device_udid,
                    'appPackage': 'com.tencent.mobileqq',
                    'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': True
                    }