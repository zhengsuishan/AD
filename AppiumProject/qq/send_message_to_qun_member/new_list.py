# 保存发送信息列表

import random

news_url_list = ['一个火遍朋友圈的骗局落幕 全国 200 多万人被骗。详情链接>>>http://www.tengxundaxuezd.cn/iQvy2akz34m29',
                 '刚发生！毕福剑在家中自杀身亡！多人参加毕福剑的追悼会....。详情链接>>>http://www.wanjiami.net/3M7Fv225po46dv',
                 '刘强东事件女主蒋娉婷大量高清私密照流出，成熟性感。详情链接>>>http://www.84zhai.cn/IzQ7N3cr4ezyxl',
                 '马云给他儿子写了一封信，感动无数人！。详情链接>>>http://www.btgbanky.cn/rMJZJfo43pqxu',
                 '蒋介石去世时出现的奇异天象，宋美龄都惊呆了！。详情链接>>>http://www.tumitengxun.cn/aqYJFb74opjdk']

news_text_list = ['一个火遍朋友圈的骗局落幕 全国 200 多万人被骗',
                  '刚发生！毕福剑在家中自杀身亡！多人参加毕福剑的追悼会',
                  '刘强东事件女主蒋娉婷大量高清私密照流出，成熟性感',
                  '马云给他儿子写了一封信，感动无数人',
                  '蒋介石去世时出现的奇异天象，宋美龄都惊呆了']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

