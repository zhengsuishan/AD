# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = 'http://toutiao.1kbnt.cn/huitoutiao/news-share.html?id=c6bbd32163cb4c979678c110ed8bafdb'
    send_text1 = '支付宝新版本界面曝光：周一见，拉一拉有变化'
    qun_name_list = ['正定网-买卖交易', 'ATX(AutomatorX) old', '北京化妆师交流群', '珠三角高级化妆师群', '重庆软件测试交流群', '南京软件测试交流群',
                     '长沙软件测试交流群'] #群名称
    qun_name_list1 = ['兄弟汇', '路遇行人', 'Microsoft问题交流', '190933303', '微博热门实时推广精选', '输了你赢了全世界又如',
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