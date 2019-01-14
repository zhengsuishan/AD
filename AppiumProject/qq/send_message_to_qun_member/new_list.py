# 保存发送信息列表

import random

news_url_list = ['【会赚钱的头条】只要填写我的邀请码81201961，你立赚1元现金，我立赚2元现金，↓↓快来点击下载帮我助力吧↓↓http://a2.app.qq.com/o/simple.jsp?pkgname=com.cashtoutiao&ckey=CK1371494628908',
                 '东方头条【【热】识破微信诈骗五大伎俩，别-入-坑-】https://mini.eastday.com/mobile/190113082723493.html?ca=809169121&f1=xq1',
                 '两个人在一起是不是真合适，就看做2件事是否很融洽。详情链接>>>http://www.xunqdq.cn/iABvUfwpy43xk',
                 '离婚考卷红了！分数太高的夫妻不准离婚！你能做对几道？。详情链接>>>http://www.weixinhehua.cn/rayiAzzd4yzjxb']

news_text_list = ['看新闻视频赚钱，1元即可提现，娱乐赚钱两不误。',
                  '识破微信诈骗五大伎俩，别-入-坑',
                  '两个人在一起是不是真合适，就看做2件事是否很融洽',
                  '离婚考卷红了！分数太高的夫妻不准离婚！你能做对几道']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

