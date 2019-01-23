# 保存发送信息列表

import random

news_url_list = ['手机赚钱项目交流群，群聊号码：849597564，有兴趣的欢迎加群',
                 '马云离开阿里后转行了？新店已经正式开业，看到名字大家笑了！http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=e963dd35d7e44164b4f65ce7ca6856f0',
                 '“九大门派”围攻阿里、腾讯 谁能笑傲支付江湖？http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=61100f371c2044e2a4a34014d50d2903',
                 '实拍农村壕热闹婚礼全程，许多习俗没见过，真稀奇,http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=fb5b7249095644b6b3e69807f669fdd7',
                 '赵本山徒弟程野被“全网通缉”，电影被下架，连师傅都没法救他！。详情链接>>>http://www.mapcaijit.cn/Rb6rUbvnpe46dv',
                 '王思聪女友真敢穿，透视装出席活动，网友：看着好尴尬。详情链接>>>http://www.lingjingdianshang.cn/YF3uIzrpoqz2u']

news_text_list = ['入群答案：手机赚钱',
                  '马云离开阿里后转行了？新店已经正式开业，看到名字大家笑了',
                  '“九大门派”围攻阿里、腾讯 谁能笑傲支付江湖',
                  '实拍农村壕热闹婚礼全程，许多习俗没见过，真稀奇',
                  '赵本山徒弟程野被“全网通缉”，电影被下架，连师傅都没法救他',
                  '王思聪女友真敢穿，透视装出席活动，网友：看着好尴尬']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

