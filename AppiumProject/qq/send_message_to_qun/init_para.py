# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = 'http://toutiao.1kbnt.cn/huitoutiao/news-share.html?id=1d4f6190ab434e93bb75e7520d253fa7'
    send_text1 = '微信迎来重大更新，针对抖音支付宝和今日头条，微信开始全面反击'
    qun_name_list = ['省钱宝宝优惠群1087', '珠三角高级化妆师群', '正定网-买卖交易', '北京化妆师交流群', '长沙软件测试交流群','南京软件测试交流群', 'Java技术交流A群', '重庆软件测试交流群', '®Team爱音乐♪ ', 'ATX(AutomatorX) old'] #群名称
    #qun_name_list = ['山西化妆师交流1群', '湖南化妆师-新年快乐', '新娘化妆师交流(一)', '杭州化妆师交流群', '输了你赢了全世界又如', '仁和区主任交流中心']
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