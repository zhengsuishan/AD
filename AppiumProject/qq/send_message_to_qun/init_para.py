# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = 'http://toutiao.1kbnt.cn/huitoutiao/news-share.html?id=6708fa0371fa454f86e21b7049a8a25d'
    send_text1 = '2019跑男名单曝光，快来看看有没有你喜欢的明星'
    qun_name_list = ['省钱宝宝优惠群1087', '珠三角高级化妆师群', '正定网-买卖交易', '北京化妆师交流群', '长沙软件测试交流群',
                     '南京软件测试交流群', 'Java技术交流A群', '重庆软件测试交流群', '®Team爱音乐♪ ', 'ATX(AutomatorX) old'] #群名称
    #qun_name_list = ['输了你赢了全世界又如', '下坝小学', '室内装修设计交流', '湖南化妆师-新年快乐','新娘化妆师交流(一)',
     #                '杭州化妆师交流群', '山西化妆师交流1群']
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