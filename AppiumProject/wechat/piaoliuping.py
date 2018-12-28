from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

class PiaoLiuPing(object):

    driver = None
    send_message = '东方头条【【热】痛心！北交大实验室爆炸起火，3名-学-生-遇-难-】https://mini.eastday.com/mobile/181226172641446.html?ca=809682829&f1=xq1'
    #send_message = '打开支付宝首页搜索“499754”，即可领红包，每天都可以领取哦，支付宝福利，快去试试吧；没有支付宝赶紧下载https://m.alipay.com/DPlKoAc，注册即可领取现金红包。'
    #send_message = '好有缘分呀，加个好友吧，哈哈'
    #send_message = 'https://m.042h4.cn/forms/FrmRegister?recomPerson=1671b80f20d&device=phone，复制到浏览器，下载安装就送10元红包，提现秒到账，不要白不要。'
    times = 20
    index = 0
    pick_times = 20
    pick_index = 0
    xiaomi_udid = 'd102deb37d13'
    #xiaomi_udid = '0123456789ABCDEF'

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.1.0'
        desired_caps['deviceName'] = 'd102deb37d13'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['udid'] = self.xiaomi_udid
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['noReset'] = 'true'
        try:
            command3 = 'adb -s %s shell ime set io.appium.android.ime/.UnicodeIME' % self.xiaomi_udid
            os.popen(command3)
            time.sleep(1.0)
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_name('发现'))
        except Exception as e:
            self.exception()

    def goto_plp(self):
        try:
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('发现'))
            self.driver.find_element_by_name('发现').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('漂流瓶'))
            self.driver.find_element_by_name('漂流瓶').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('扔一个'))
        except Exception as e:
            self.exception()

    def reng(self):
       try:
           if self.index == 20:
               self.pick()
           else:
               self.driver.find_element_by_name('扔一个').click()
               WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.tencent.mm:id/a60'))
               self.driver.find_element_by_id('com.tencent.mm:id/a60').click()
               WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('扔出去'))
               self.driver.find_element_by_id('com.tencent.mm:id/a5v').send_keys(self.send_message)
               time.sleep(1)
               self.driver.find_element_by_name('扔出去').click()

               self.index = self.index + 1

               WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_name('扔一个'))
               self.reng()

       except Exception as e:
           self.exception()

    def pick(self):
        if self.pick_index == 20:
            self.driver = None
        else:
            self.driver.find_element_by_name('捡一个').click()
            time.sleep(10.0)
            if '打开瓶子' in self.driver.page_source:
                WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_name('打开瓶子'))
                self.driver.find_element_by_id('com.tencent.mm:id/a5p').click()
                WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('回应'))
                self.driver.find_element_by_name('回应').click()
                WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.tencent.mm:id/aie'))
                self.driver.find_element_by_id('com.tencent.mm:id/aie').send_keys(self.send_message)
                time.sleep(1.0)
                self.driver.find_element_by_name('发送').click()
                time.sleep(1.0)
                self.pick_index = self.pick_index +1
                cmd = 'adb -s %s shell input keyevent 4'%self.xiaomi_udid
                os.popen(cmd)
                time.sleep(1.0)
                self.goto_plp()
                self.pick()
            else:
                if '捡一个' in self.driver.page_source:
                    self.pick()
                else:
                    pass

    def exception(self):
        if '通讯录' in self.driver.page_source:
            self.goto_plp()
            self.reng()
        elif '附近的人' in self.driver.page_source and '漂流瓶' in self.driver.page_source:
            self.driver.find_element_by_name('漂流瓶').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('扔一个'))
            self.reng()
        elif '扔一个' in self.driver.page_source and '捡一个' in self.driver.page_source:
            self.reng()
        elif '按住说话' in self.driver.page_source:
            cmd = 'adb -s %s shell input keyevent 4'%self.xiaomi_udid
            os.popen(cmd)
            WebDriverWait(self.driver, 3).until(lambda x:x.find_element_by_name('附近的人'))
            self.driver.find_element_by_name('漂流瓶').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('扔一个'))
            self.reng()
        elif '扔出去' in self.driver.page_source:
            cmd = 'adb -s %s shell input keyevent 4'%self.xiaomi_udid
            os.popen(cmd)
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('附近的人'))
            self.driver.find_element_by_name('漂流瓶').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_name('扔一个'))
            self.reng()
        elif '今天的瓶子已经用完啦。' in self.driver.page_source:
            self.driver.find_element_by_name('确定').click()
            time.sleep(1.0)
            self.pick()
        elif '扔回海里' in self.driver.page_source:
            self.driver.find_element_by_name('回应').click()
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.tencent.mm:id/ac7'))
            self.driver.find_element_by_id('com.tencent.mm:id/ac7').send_keys(self.send_message)
            time.sleep(1.0)
            self.driver.find_element_by_name('发送').click()
            time.sleep(1.0)
            self.pick_index = self.pick_index + 1
            cmd = 'adb -s %s shell input keyevent 4'%self.xiaomi_udid
            os.popen(cmd)
            time.sleep(1.0)
            self.goto_plp()
            self.pick()
        elif '今天捡瓶子的机会已经用完啦。' in self.driver.page_source:
            self.driver = None
        else:
            try:
                cmd = 'adb -s %s shell am force-stop com.tencent.mm'%self.xiaomi_udid
                os.popen(cmd)
                time.sleep(1)
                start_cmd = 'adb -s %s shell am start com.tencent.mm/.ui.LauncherUI'%self.xiaomi_udid
                os.popen(start_cmd)
                WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_name('发现'))
                self.goto_plp()
                self.reng()
            except Exception as e:
                self.exception()

if __name__ == '__main__':
    plp = PiaoLiuPing()
    plp.get_driver()
    plp.goto_plp()
    plp.reng()