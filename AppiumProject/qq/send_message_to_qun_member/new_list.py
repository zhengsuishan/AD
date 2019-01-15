# 保存发送信息列表

import random

news_url_list = ['【会赚钱的头条】只要填写我的邀请码81201961，你立赚1元现金，我立赚2元现金，↓↓快来点击下载帮我助力吧↓↓http://a2.app.qq.com/o/simple.jsp?pkgname=com.cashtoutiao&ckey=CK1371494628908',
                 '早晨洗头发和晚上洗头发，哪个危害更大？多长时间洗一次最健康？。详情链接>>>http://www.taoyuan1688y.cn/MVnMZzq434uxu',
                 '他首次剖白和周星驰的真实关系，揭露17年从没合-作-的-原-因-】https://mini.eastday.com/mobile/190115071300170.html?ca=809169121&f1=xq1']

news_text_list = ['看新闻视频赚钱，1元即可提现，娱乐赚钱两不误。',
                  '早晨洗头发和晚上洗头发，哪个危害更大？多长时间洗一次最健康',
                  '他首次剖白和周星驰的真实关系，揭露17年从没合-作-的-原-因']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

