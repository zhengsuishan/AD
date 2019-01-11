# 保存发送信息列表

import random

news_url_list = ['支付宝转账时，如果出现这个提示就要注意了。详情链接>>>http://www.fjjjwl.cn/2iQRnulq43podl',
                 '大爆炸：上午，崔 永 元举报了 585位明星！附名单...。详情链接>>>http://www.maliang168.cn/6BV7fuypof7d9']

news_text_list = ['支付宝转账时，如果出现这个提示就要注意了',
                  '大爆炸：上午，崔 永 元举报了 585位明星！附名单']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

