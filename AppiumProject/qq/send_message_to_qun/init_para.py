# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = '穷人和富人吵架，句句在理，太精辟啦！。详情链接>>>http://www.smrmy.cn/biAbqijzefdx9'
    send_text1 = '马云：我是杭州师范学院毕业，我从没-有-自-卑-过'
    qun_name_list0 = ['正定网-买卖交易', 'ATX(AutomatorX) old', '北京化妆师交流群', '珠三角高级化妆师群', '重庆软件测试交流群', '南京软件测试交流群',
                     '长沙软件测试交流群'] #群名称
    qun_name_list1 = ['兄弟汇', '路遇行人', 'Microsoft问题交流', '190933303', '微博热门实时推广精选', '输了你赢了全世界又如',
                     '湖南化妆师-新年快乐', '新娘化妆师交流(一)', '杭州化妆师交流群', '山西化妆师交流1群']

    qun_name_list = ['逆流沙作协基地', '最新电影分享', '永州生姜种植交流', '网站艺术', '体彩十一选五', '淘宝天猫内部优惠券群', '贪玩羊页游-武炼巅峰',
                     '企鹅电竞粉丝群', 'GAME UI创意设计部落', '咸阳福特车友群', '建筑工程机械行业交流', 'value     you',
                     '友情会场', '世界杯竞猜', '全■民■领■福■利', '股票交流', '♚荣耀巅峰♚', '武炼巅峰之崛起', '游戏继续中',
                     '电脑知识交流群', '敢丨死丨队', '南京驾驶员交流群', '孟加拉翻译社', '武炼巅峰', '大同古钱币', '雷诺曼 lenormand',
                     'ppt制作学习交流', 'AE交流学习超级群', '武炼～巅峰', '武炼巅峰♂战队群', '最新热门电影电视剧', '梵语梵文藏语藏文翻译',
                     '最新电影分享群①', '有很多笑话', '电影电视剧有的看', '电影电视剧有的看', '武汉装载机司机交流群', '都市之大天师刷钱系统',
                     '王者荣耀游戏群', '电影 聊天  娱乐机器人']

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