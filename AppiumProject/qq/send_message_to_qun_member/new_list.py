# 保存发送信息列表

import random

news_url_list = ['【会赚钱的头条】只要填写我的邀请码81201961，你立赚1元现金，我立赚2元现金，↓↓快来点击下载帮我助力吧↓↓http://a2.app.qq.com/o/simple.jsp?pkgname=com.cashtoutiao&ckey=CK1371494628908']

news_text_list = ['看新闻视频赚钱，1元即可提现，娱乐赚钱两不误。']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

