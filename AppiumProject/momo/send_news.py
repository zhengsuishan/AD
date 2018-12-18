from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import traceback

class MoMo(object):

    driver = None
    launch_time = 15
    wait_time = 3
    net_wait_time = 5
    message_content = '支付宝发红包啦，赶紧领取，打开支付宝首页搜索“499754”，即可领红包，每天都可以领取哦；没有支付宝赶紧下载https://m.alipay.com/DPlKoAc，注册即可领取现金红包。1110'
    #message_content = 'https://m.042h4.cn/forms/FrmRegister?recomPerson=1671b80f20d&device=phone，复制到浏览器，下载安装就送10元红包，提现秒到账，不要白不要。'
    udid = 'H8018K9012345678'
    swipe_y1 = 500
    swipe_y2_first = 320
    swipe_y2 = 320
    send_num = None
    force_stop_count = 20

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'W6'
        desired_caps['appPackage'] = 'com.immomo.momo'
        desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['udid'] = 'H8018K9012345678'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.send_count(1) #获取发送次数

        try:
            WebDriverWait(self.driver, self.launch_time).until(lambda x:x.find_element_by_name('附近的人'))
            self.driver.find_element_by_name('附近的人').click()
            WebDriverWait(self.driver, self.net_wait_time).until(lambda x:x.find_element_by_id('com.immomo.momo:id/userlist_item_iv_face'))
        except Exception as e:
            self.exce_do()

    def send(self):
        try:
            if '聊天室' in self.driver.page_source and '全部' in self.driver.page_source:
                location = self.swipe_y2_first
            else:
                location = self.swipe_y2
            swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 200' % (
                self.udid, self.swipe_y1, location)
            os.popen(swipe_cmd)
            time.sleep(3)

            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.immomo.momo:id/userlist_item_iv_face'))

            while '聊天室' in self.driver.page_source:
                if '聊天室' in self.driver.page_source and '全部' in self.driver.page_source:
                    location = self.swipe_y2_first
                else:
                    location = self.swipe_y2
                swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 200' % (
                    self.udid, self.swipe_y1, location)
                os.popen(swipe_cmd)
                time.sleep(0.5)
            else:
                pass

            self.driver.find_element_by_id('com.immomo.momo:id/userlist_item_iv_face').click()
            time.sleep(3.0)

            if '对话' in self.driver.page_source and '关注' in self.driver.page_source:
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('对话'))
                self.driver.find_element_by_name('对话').click()
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('请输入消息...'))

                temp_bool = True
                try:
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda x: x.find_element_by_id('com.immomo.momo:id/iv_message_status'))
                except Exception as e:
                    temp_bool = False

                if temp_bool:
                    self.send_count(2)
                    back_cmd1 = 'adb -s %s shell input keyevent 4' % self.udid
                    os.popen(back_cmd1)
                    time.sleep(1)
                    back_cmd2 = 'adb -s %s shell input keyevent 4' % self.udid
                    os.popen(back_cmd2)
                    WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))

                    self.send()

                else:
                    self.driver.find_element_by_name('请输入消息...').send_keys(self.message_content)
                    time.sleep(0.5)
                    self.driver.find_element_by_name('发送').click()
                    time.sleep(2)

                    if '当日打招呼人数已达上限.' in self.driver.page_source:
                        self.driver = None
                    else:
                        pass

                    self.send_num += 1
                    #print(self.send_num)
                    self.send_count(2)
                    #print(self.send_num)
                    back_cmd1 = 'adb -s %s shell input keyevent 4' % self.udid
                    os.popen(back_cmd1)
                    time.sleep(1)
                    back_cmd2 = 'adb -s %s shell input keyevent 4' % self.udid
                    os.popen(back_cmd2)
                    WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))

                    while '聊天室' in self.driver.page_source:
                        if '聊天室' in self.driver.page_source and '全部' in self.driver.page_source:
                            location = self.swipe_y2_first
                        else:
                            location = self.swipe_y2
                        swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 200' % (
                            self.udid, self.swipe_y1, location)
                        os.popen(swipe_cmd)
                        time.sleep(0.5)
                    else:
                        pass


                    self.send()
            else:
                back_cmd3 = 'adb -s %s shell input keyevent 4' % self.udid
                os.popen(back_cmd3)
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))

                while '聊天室' in self.driver.page_source:
                    if '聊天室' in self.driver.page_source and '全部' in self.driver.page_source:
                        location = self.swipe_y2_first
                    else:
                        location = self.swipe_y2
                    swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 200' % (
                        self.udid, self.swipe_y1, location)
                    os.popen(swipe_cmd)
                    time.sleep(1.0)
                else:
                    pass


                self.send()

        except Exception as e:
            #print(e)
            self.exce_do()

    def send_count(self, index):
        if index == 1:
            with open('count', 'r') as f:
                text = f.readlines()[0].split(':')
                self.send_num = int(text[1])
        else:
            with open('count', 'w+') as f:
                f.write('send_count:%d' % self.send_num)

    def exce_do(self):
        if '附近动态' in self.driver.page_source and '附近的人' in self.driver.page_source and '附近直播' in self.driver.page_source:
            self.send()
        elif '对话' in self.driver.page_source and '关注' in self.driver.page_source:
            back_cmd4 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd4)
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))
            self.send()
        elif '点点' in self.driver.page_source:
            back_cmd5 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd5)
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))
            self.send()
        elif '请输入消息...' in self.driver.page_source:
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(0.5)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(0.5)
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('附近的人'))
            self.send()
        elif '存储空间不足' in self.driver.page_source:
            self.driver.find_element_by_name('取消').click()
            time.sleep(1.0)
            self.exce_do()
        elif '提示' in self.driver.page_source and '取消' in self.driver.page_source and '确认' in self.driver.page_source:
            self.driver.find_element_by_name('取消').click()
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.exce_do()
        elif '同城' in self.driver.page_source and 'KTV' in self.driver.page_source:
            back_cmd8 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd8)
            time.sleep(1.0)
            self.exce_do()
        else:
            if self.force_stop_count >= 0:
                start_cmd1 = 'adb -s %s shell am start com.immomo.momo/.android.activity.WelcomeActivity' % self.udid
                os.popen(start_cmd1)
                time.sleep(3.0)
                self.exce_do()
                self.force_stop_count -= 1
            else:
                try:
                    stop_cmd = 'adb -s %s shell am force-stop com.immomo.momo' % self.udid
                    os.popen(stop_cmd)
                    time.sleep(3.0)
                    start_cmd = 'adb -s %s shell am start com.immomo.momo/.android.activity.WelcomeActivity' % self.udid
                    os.popen(start_cmd)
                    time.sleep(self.launch_time)
                    WebDriverWait(self.driver, self.launch_time).until(lambda x: x.find_element_by_name('附近的人'))
                    self.driver.find_element_by_name('附近的人').click()
                    WebDriverWait(self.driver, self.net_wait_time).until(
                        lambda x: x.find_element_by_id('com.immomo.momo:id/userlist_item_iv_face'))
                    self.send()
                except Exception as e:
                    self.exce_do()



if __name__ == '__main__':
    girl_friend = MoMo()
    try:
        girl_friend.get_driver()
        girl_friend.send()
    except Exception as e:
        girl_friend.exce_do()