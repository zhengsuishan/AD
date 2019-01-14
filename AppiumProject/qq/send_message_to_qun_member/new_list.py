# 保存发送信息列表

import random

news_url_list = ['【会赚钱的头条】只要填写我的邀请码81201961，你立赚1元现金，我立赚2元现金，↓↓快来点击下载帮我助力吧↓↓http://a2.app.qq.com/o/simple.jsp?pkgname=com.cashtoutiao&ckey=CK1371494628908',
                 '人为什么离婚，这是我见过最理性的回答。详情链接>>>http://www.oulemyall.cn/2Iveiyycpefhnb',
                 '老同学是什么?看完我真的哭了！送给我最珍惜的老同学们~。详情链接>>>http://www.weixinfangsheng.cn/6RnaMz243g2n9',
                 '东方头条【【热文】2019爱自己，做自己，靠-自-己-】https://mini.eastday.com/mobile/190114000853918.html?ca=809169121&f1=xq1',
                 '东方头条【【热】不懂英语怎么办？4个华为手机自带语言翻译功能，让英语-畅-通-无-阻-】https://mini.eastday.com/mobile/190113204953244.html?ca=809169121&f1=xq1']

news_text_list = ['看新闻视频赚钱，1元即可提现，娱乐赚钱两不误。',
                  '人为什么离婚，这是我见过最理性的回答',
                  '老同学是什么?看完我真的哭了！送给我最珍惜的老同学们',
                  '2019爱自己，做自己，靠-自-己',
                  '不懂英语怎么办？4个华为手机自带语言翻译功能，让英语-畅-通-无-阻']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

