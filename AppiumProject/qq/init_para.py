# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = '发朋友圈赚佣金，告别死工资，想做的速度扫码下载，不明白联系我，手把手教'
    qun_name_list = ['百度语音开发者交流⑥',
                     '游戏设计交流群', '性能测试进阶', 'java', 'ATX(AutomatorX) old', '北京化妆师交流群',
                     '珠三角高级化妆师群', '重庆软件测试交流群', '南京软件测试交流群', '长沙软件测试交流群',
                     'selenium交流专用超级', 'PS爱好者学习交流群', 'UI设计交流/招聘/外包/兼职',
                     'java', 'Java技术交流A群'] #群名称
    #qun_name_list = ['输了你赢了全世界又如', '下坝小学', '室内装修设计交流', '湖南化妆师-新年快乐','新娘化妆师交流(一)',
     #                '杭州化妆师交流群', '山西化妆师交流1群']
    index = 1 #调用发送图片的方法
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