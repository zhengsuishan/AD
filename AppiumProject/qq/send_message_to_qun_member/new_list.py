# 保存发送信息列表

import random

news_url_list = ['手机赚钱项目交流群，群聊号码：849597564，有兴趣的欢迎加群',
                 '世界最后一个纯女性部落，没有一个男人，繁衍方式令人大跌眼镜。详情链接>>>http://www.wenjiubangy.cn/i2EjUzf1z3zjxb',
                 '王思聪下跪照曝出，夜店里当众下跪 细说王思聪的失败与成功之处。详情链接>>>http://www.tengxunyoung.cn/miiAjena4efk20',
                 '各国第一美女出炉，最后一个让世界都惊呆了！。详情链接>>>http://www.heheguaji.cn/YrMN7vtp3462k',
                 '世界首批体细胞克隆疾病模型猴在-中-国-诞-生-】https://mini.eastday.com/mobile/190124021916853.html?ca=809169121&f1=xq2',
                 '同样的姿势，热巴赵丽颖软萌，鞠婧祎像在生气，唯独关晓-彤-太-做-作-】https://mini.eastday.com/mobile/190122101843544.html?ca=809169121&f1=xq2',
                 '遍地钻石的冥王星，为何没人去开采？除了技术问题还有什么？http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=e14fa6caa2104631ba867714463cd485',
                 '吴京带小板凳坐火车过道：只要能回家，坐哪都行！12306回应  http://toutiao.rervyh.cn/huitoutiao/news-share.html?id=ca6c4d7de06f42c89a3d48a85a4f3ae7']

news_text_list = ['入群答案：手机赚钱',
                  '世界最后一个纯女性部落，没有一个男人，繁衍方式令人大跌眼镜',
                  '王思聪下跪照曝出，夜店里当众下跪 细说王思聪的失败与成功之处',
                  '各国第一美女出炉，最后一个让世界都惊呆了！',
                  '世界首批体细胞克隆疾病模型猴在-中-国-诞-生',
                  '同样的姿势，热巴赵丽颖软萌，鞠婧祎像在生气，唯独关晓-彤-太-做-作',
                  '遍地钻石的冥王星，为何没人去开采？除了技术问题还有什么',
                  '吴京带小板凳坐火车过道：只要能回家，坐哪都行！12306回应']

def get_news():
    size = len(news_url_list)
    random_num = random.randint(0, size)
    return news_url_list[random_num - 1], news_text_list[random_num - 1]

