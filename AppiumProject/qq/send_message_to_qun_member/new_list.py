# 保存发送信息列表

import random

news_url_list = ['手机赚钱项目交流群，群聊号码：849597564，有兴趣的欢迎加群',
                 '马云的魅力有多大？他为追随马云，放弃590万年薪，拿500块工资  http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=6628ab5d81fc4e3096892beace682c93',
                 '范冰冰又出丑 闻范冰冰与冯小刚露 骨照泄露激情视屏流出。详情链接>>>http://www.htsltzc.cn/ZjqAFrcfezzd9',
                 '陈乔恩冬日街拍，造型成熟差点让-人-认-不-出-】https://mini.eastday.com/mobile/190124005418449.html?ca=809169121&f1=xq1']

news_text_list = ['入群答案：手机赚钱',
                  '马云的魅力有多大？他为追随马云，放弃590万年薪，拿500块工资',
                  '范冰冰又出丑 闻范冰冰与冯小刚露 骨照泄露激情视屏流出',
                  '陈乔恩冬日街拍，造型成熟差点让-人-认-不-出']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

