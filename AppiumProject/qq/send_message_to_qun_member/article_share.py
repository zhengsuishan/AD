import os
import time
import random
from datetime import datetime
import xml.dom.minidom

class AS(object):

    udid = 'd102deb37d13'

    agent_cmd = 'adb -s %s shell am start com.wanchen.zldl/.LoadingActivity'%udid
    wechat_cmd = 'adb -s %s shell am start com.tencent.mm/.ui.LauncherUI'%udid

    fir_x = 380
    fir_y = 300
    sec_x = 380
    sec_y = 744
    third_x = 380
    third_y = 956

    agent_x = 500
    agent_y = 873

    agent_x_1 = 360
    agent_x_2 = 777

    back_x = 40
    back_y = 98

    times = 10
    send_times = 0

    def change_agent(self):
        os.popen(self.agent_cmd)
        time.sleep(7)

        click_cmd = 'adb -s %s shell input tap %d %d'%(self.udid, self.agent_x ,self.agent_y )
        os.popen(click_cmd)
        time.sleep(1.0)
        click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.agent_x_1, self.agent_x_2)
        os.popen(click_cmd)
        time.sleep(15.0)

    def read_news(self):
        wait_time = random.randint(3, 5)

        os.popen(self.wechat_cmd)
        time.sleep(wait_time)

        wait_time = random.randint(5, 10)
        time.sleep(wait_time)

        # 点击第一个新闻
        click_fir = 'adb -s %s shell input tap %d %d' % (self.udid, self.fir_x, self.fir_y)
        os.popen(click_fir)
        print('第一条新闻点击时间：%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        wait_time = random.randint(10, 20)
        time.sleep(wait_time)

        back_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.back_x, self.back_y)
        os.popen(back_cmd)
        wait_time = random.randint(3, 5)
        time.sleep(wait_time)

        # 点击第二个新闻
        click_fir = 'adb -s %s shell input tap %d %d' % (self.udid, self.sec_x, self.sec_y)
        os.popen(click_fir)
        print('第二条新闻点击时间：%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        wait_time = random.randint(10, 20)
        time.sleep(wait_time)

        back_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.back_x, self.back_y)
        os.popen(back_cmd)
        wait_time = random.randint(3, 5)
        time.sleep(wait_time)

        # 点击第三个新闻
        click_fir = 'adb -s %s shell input tap %d %d' % (self.udid, self.third_x, self.third_y)
        os.popen(click_fir)
        print('第三条新闻点击时间：%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        wait_time = random.randint(10, 20)
        time.sleep(wait_time)

        back_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.back_x, self.back_y)
        os.popen(back_cmd)
        wait_time = random.randint(3, 5)
        time.sleep(wait_time)

    def read_swipe(self):
        pass

    def get_dump(self):
        cmd_xml = 'adb -s %s shell uiautomator dump' % self.udid
        os.popen(cmd_xml)
        time.sleep(5.0)

        desk = os.path.join(os.path.expanduser("~"), 'Desktop')

        pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (self.udid, desk)
        os.popen(pull_cmd)
        time.sleep(1.0)

        file_path = '%s\\window_dump.xml' % desk  # xml文件路径
        DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

        string = DOMTree.toxml()
        print(string)

if __name__ == '__main__':

    num = random.randint(1, AS.times)
    next_wait_time = random.randint(60, 600)

    while True:
        print(num, AS.send_times, next_wait_time)
        if AS.send_times >= num:
            time.sleep(next_wait_time)
            AS().change_agent()
            time.sleep(1.0)
            AS().read_news()
            AS.send_times += 1

            num = random.randint(1, AS.times)
            next_wait_time = random.randint(60, 600)

            AS.send_times = 0

        else:
            AS().change_agent()
            time.sleep(1.0)
            AS().read_news()
            AS.send_times += 1
