# 保存发送信息列表

import random

news_url_list = ['手机赚钱项目交流群，群聊号码：849597564，有兴趣的欢迎加群']

news_text_list = ['入群答案：手机赚钱']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

