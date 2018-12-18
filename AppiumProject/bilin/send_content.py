from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import traceback

class BiLin(object):
    driver = None
    launch_time = 15
    wait_time = 3
    net_wait_time = 5
    message_content = '支付宝年终大回馈，超大红包免费领，你还不知道吗？，打开支付宝首页搜索“499754”，即可领红包，每天都可以领取哦20181202'
    #message_content = 'https://m.042h4.cn/forms/FrmRegister?recomPerson=1671b80f20d&device=phone，复制到浏览器，下载安装就送10元红包，提现秒到账，不要白不要。'
    #message_content = '提现秒到账，有兴趣的可以下载了解下；投资几百块，开启躺赚人生'
    #message_content = '看视频就能赚零花钱，有兴趣的下载了解下'
    udid = 'H8018K9012345678'
    send_num = None
    swipe_y1 = 1000
    swipe_y2 = 599
    force_stop_count = 10
    main_swipe_count = 0

    def send_pic(self):
        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.bilin.huijiao.activity:id/a1f'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a1f').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.bilin.huijiao.activity:id/a4p'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a4p').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.bilin.huijiao.activity:id/yk'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/yk').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.bilin.huijiao.activity:id/a17'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a17').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('选择'))
            self.driver.find_element_by_name('选择').click()
            time.sleep(1.0)
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/a4p'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a4p').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/yk'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/yk').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/a18'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a18').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('选择'))
            self.driver.find_element_by_name('选择').click()
            time.sleep(1.0)
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/a4p'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a4p').click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/yk'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/yk').click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/a19'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a19').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('选择'))
            self.driver.find_element_by_name('选择').click()
            time.sleep(3.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
        except Exception as e:
            ##print(traceback.#print_exc())
            self.exce_do()


    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'W6'
        desired_caps['appPackage'] = 'com.bilin.huijiao.activity'
        desired_caps['appActivity'] = 'com.bilin.huijiao.ui.activity.NewLoadingActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['udid'] = 'H8018K9012345678'
        desired_caps['newCommandTimeout'] = 300
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.send_count(1)  # 获取发送次数

        try:
            time.sleep(self.launch_time)
            click_cmd = 'adb -s %s shell input tap 514 1179' % self.udid
            os.popen(click_cmd)
            time.sleep(1.0)
        except Exception as e:
            ##print(traceback.#print_exc())
            self.exce_do()

    def main_swipe(self):
        for index in range(0, self.main_swipe_count):
            swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 1000' % (
                self.udid, self.swipe_y1, self.swipe_y2)
            os.popen(swipe_cmd)
            time.sleep(1.5)

    def send_count(self, index):
        if index == 1:
            with open('count', 'r') as f:
                text = f.readlines()[0].split(':')
                self.send_num = int(text[1])
        else:
            with open('count', 'w+') as f:
                f.write('send_count:%d' % self.send_num)

    def go_send(self):
        try:
            if '动态' in self.driver.page_source:
                click_cmd = 'adb -s %s shell input tap 514 1179' % self.udid
                os.popen(click_cmd)
                time.sleep(1.0)
            elif '指纹' in self.driver.page_source and '手机大师' in self.driver.page_source:
                self.exce_do()
            else:
                pass

            WebDriverWait(self.driver, self.net_wait_time).until(
                lambda x: x.find_element_by_id('com.bilin.huijiao.activity:id/a1n'))
            self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a1n').click()

            try:
                WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('打招呼'))
            except Exception as e:
                if '该用户由于不文明行为已被禁用' in self.driver.page_source:
                    back_cmd0 = 'adb -s %s shell input keyevent 4' % self.udid
                    os.popen(back_cmd0)
                    time.sleep(1.0)
                    swipe_cmd0 = 'adb -s %s shell input swipe 360 %d 360 %d 1000' % (
                        self.udid, self.swipe_y1, self.swipe_y2)
                    os.popen(swipe_cmd0)
                    time.sleep(3.0)
                    self.go_send()

            self.driver.find_element_by_name('打招呼').click()
            WebDriverWait(self.driver, self.net_wait_time).until(lambda x:x.find_element_by_name('输入想说的内容'))

            time.sleep(3.0)

            if self.message_content in self.driver.page_source:
                self.send_count(2)
                time.sleep(1.0)

                self.driver.find_element_by_id('com.bilin.huijiao.activity:id/b4').click()
                time.sleep(1.0)
                self.driver.find_element_by_id('com.bilin.huijiao.activity:id/b5').click()
                time.sleep(1.0)

                if '动态' in self.driver.page_source:
                    pass
                else:
                    self.exce_do()

                swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 1000' % (
                    self.udid, self.swipe_y1, self.swipe_y2)
                os.popen(swipe_cmd)
                time.sleep(3.0)
                self.go_send()
            else:
                #self.send_pic()
                try:
                    self.driver.find_element_by_name('输入想说的内容').send_keys(self.message_content)
                except Exception as e:
                    pass

                time.sleep(1.0)
                self.driver.find_element_by_id('com.bilin.huijiao.activity:id/a1f').click()
                time.sleep(3.0)
                self.send_num += 1
                self.send_count(2)
                time.sleep(1.0)

                self.driver.find_element_by_id('com.bilin.huijiao.activity:id/b4').click()
                time.sleep(1.0)
                self.driver.find_element_by_id('com.bilin.huijiao.activity:id/b5').click()
                time.sleep(1.0)

                if '动态' in self.driver.page_source:
                    pass
                else:
                    self.exce_do()

                swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 1000' % (
                    self.udid, self.swipe_y1, self.swipe_y2)
                os.popen(swipe_cmd)
                time.sleep(3.0)
                self.go_send()

        except Exception as e:
            ##print(traceback.#print_exc())
            self.exce_do()

    def exce_do(self):
        if '首页' in self.driver.page_source and '房间' in self.driver.page_source and '动态' in self.driver.page_source and '聊天' in self.driver.page_source:
            #print('1111')
            self.go_send()
        elif '申请通话' in self.driver.page_source and '打招呼' in self.driver.page_source:
            #print('222')
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            self.go_send()
        elif '输入想说的内容' in self.driver.page_source and '图片' not in self.driver.page_source and '拍照' not in self.driver.page_source:
            #print('3333')
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.go_send()
        elif self.message_content in self.driver.page_source:
            #print('4444')
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.go_send()
        elif '该用户由于不文明行为已被禁用' in self.driver.page_source:
            #print('5555')
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 1000' % (
                self.udid, self.swipe_y1, self.swipe_y2)
            os.popen(swipe_cmd)
            time.sleep(3.0)
            self.go_send()
        elif '图片' in self.driver.page_source and '拍照' in self.driver.page_source:
            #print('6666')
            back_cmd62 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd62)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.go_send()
        elif '所有文件夹' in self.driver.page_source:
            #print('77777')
            back_cmd62 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd62)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            back_cmd72 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd72)
            time.sleep(1.0)
            self.go_send()
        elif 'QQ_Images' in self.driver.page_source and '所有文件夹' not in self.driver.page_source:
            #print('8888')
            back_cmd62 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd62)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            back_cmd72 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd72)
            time.sleep(1.0)
            self.go_send()
        elif '比邻' in self.driver.page_source and '选择' in self.driver.page_source:
            #print('99999')
            back_cmd62 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd62)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            back_cmd72 = 'adb -s %s shell input keyevent 4' % self.udid
            os.popen(back_cmd72)
            time.sleep(1.0)
            self.go_send()
        else:
            try:
                #print('00000')

                stop_cmd = 'adb -s %s shell am force-stop com.bilin.huijiao.activity' % self.udid
                os.popen(stop_cmd)
                time.sleep(3.0)
                back_cmd7 = 'adb -s %s shell input keyevent 3' % self.udid
                os.popen(back_cmd7)
                time.sleep(1.0)
                back_cmd72 = 'adb -s %s shell input keyevent 3' % self.udid
                os.popen(back_cmd72)
                time.sleep(1.0)

                self.driver.find_element_by_name('比邻').click()
                time.sleep(self.launch_time)

                self.exce_do()

            except Exception as e:
                self.exce_do()

if __name__ == '__main__':
    new_obj = BiLin()
    try:
        new_obj.get_driver()
        new_obj.main_swipe()
        new_obj.go_send()
    except Exception as e:
        new_obj.exce_do()
