from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import random
import sys
import traceback

class AddFriend(object):

    driver = None
    xiaomi_udid = 'd102deb37d13'
    #xiaomi_udid = '0123456789ABCDEF'
    launch_time = 15
    wait_time = 3
    net_wait_time = 5
    yanzheng_mess = '嗨!，加个好友吧，哈哈'
    force_stop_count = 5
    lo_x = 74
    lo_y = 207

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.1.0'
        desired_caps['deviceName'] = 'xiaomi'
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
            WebDriverWait(self.driver, self.launch_time).until(lambda x: x.find_element_by_id('com.tencent.mm:id/hu'))
        except Exception as e:
            self.exception()

    def add(self):
        print(sys._getframe().f_code.co_name)
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        phone_num = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.tencent.mm:id/hu'))
            self.driver.find_element_by_id('com.tencent.mm:id/hu').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('添加朋友'))
            self.driver.find_element_by_name('添加朋友').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('微信号/QQ号/手机号'))
            self.driver.find_element_by_name('微信号/QQ号/手机号').click()
            time.sleep(1.5)
            self.driver.find_element_by_id('com.tencent.mm:id/ji').send_keys(phone_num)

            time.sleep(3.0)

            cmd_click = 'adb -s %s shell input tap %d %d'%(self.xiaomi_udid, self.lo_x, self.lo_y)
            os.popen(cmd_click)
            time.sleep(3.0)

            if '该用户不存在' in self.driver.page_source:
                back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd8)
                time.sleep(1.0)
                back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd8)
                time.sleep(1.0)
                self.add()
            elif '被搜帐号状态异常，无法显示' in self.driver.page_source:
                back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd8)
                time.sleep(1.0)
                back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd8)
                time.sleep(1.0)
                self.add()
            elif '操作过于频繁，请稍后再试' in self.driver.page_source:
                time.sleep(3600)
                back_cmd9 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd9)
                time.sleep(1.0)
                back_cmd10 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd10)
                time.sleep(1.0)
                self.add()
            elif '发消息' in self.driver.page_source:
                back_cmd13 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd13)
                time.sleep(1)
                back_cmd11 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd11)
                time.sleep(1.0)
                back_cmd12 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd12)
                time.sleep(1.0)
                self.add()


            WebDriverWait(self.driver, self.net_wait_time).until(lambda x:x.find_element_by_name('设置备注和标签'))
            if '发消息' in self.driver.page_source:
                back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd8)
                time.sleep(1.0)
                back_cmd9 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd9)
                time.sleep(1.0)
                back_cmd10 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                os.popen(back_cmd10)
                time.sleep(1.0)
                self.add()
            elif '添加到通讯录' in self.driver.page_source:
                self.driver.find_element_by_name('添加到通讯录').click()
                time.sleep(3.0)

                if '验证申请' in self.driver.page_source:
                    if self.yanzheng_mess in self.driver.page_source:
                        self.driver.find_element_by_name('发送').click()
                        time.sleep(3.0)
                        back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd8)
                        time.sleep(1.0)
                        back_cmd9 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd9)
                        time.sleep(1.0)
                        back_cmd10 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd10)
                        time.sleep(1.0)
                        self.add()
                    else:
                        self.driver.find_element_by_id('com.tencent.mm:id/dny').clear()
                        time.sleep(1.0)
                        self.driver.find_element_by_id('com.tencent.mm:id/dny').send_keys(self.yanzheng_mess)
                        time.sleep(1.0)
                        self.driver.find_element_by_name('发送').click()
                        time.sleep(3.0)
                        back_cmd8 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd8)
                        time.sleep(1.0)
                        back_cmd9 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd9)
                        time.sleep(1.0)
                        back_cmd10 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                        os.popen(back_cmd10)
                        time.sleep(1.0)
                        self.add()
                elif '你已添加了╰ 温柔的悬念，现在可以开始聊天了。' in self.driver.page_source:
                    back_cmd11 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
                    os.popen(back_cmd11)
                    time.sleep(1.0)
                    self.add()

            else:
                pass

        except Exception as e:
            print(traceback.print_exc())
            self.exception()

    def ele_id(self, ele_id):
        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element_by_id(ele_id))
            return True
        except Exception as e:
            return False

    def exception(self):
        print(sys._getframe().f_code.co_name)
        if '通讯录' in self.driver.page_source and '发现' in self.driver.page_source and '我' in self.driver.page_source:
            self.add()
        elif '发起群聊' in self.driver.page_source and '添加朋友' in self.driver.page_source:
            back_cmd1 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd1)
            time.sleep(1.0)
            self.add()
        elif '雷达加朋友' in self.driver.page_source and '面对面建群' in self.driver.page_source and '微信号/QQ号/手机号' not in self.driver.page_source:
            back_cmd2 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd2)
            time.sleep(1.0)
            self.add()
        elif '微信号/QQ号/手机号' in self.driver.page_source:
            back_cmd3 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd3)
            time.sleep(1.0)
            back_cmd4 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd4)
            time.sleep(1.0)
            self.add()
        elif '该用户不存在' in self.driver.page_source or '被搜帐号状态异常，无法显示' in self.driver.page_source:
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.add()
        elif '操作过于频繁，请稍后再试' in self.driver.page_source:
            time.sleep(3600)
            back_cmd12 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd12)
            time.sleep(1.0)
            back_cmd13 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd13)
            time.sleep(1.0)
            self.add()
        elif '添加到通讯录' in self.driver.page_source:
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.add()
        elif '选择一个群' in self.driver.page_source:
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.add()
        elif self.ele_id(ele_id='com.tencent.mm:id/ji'):
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.add()
        elif '验证申请' in self.driver.page_source:
            back_cmd4 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd4)
            time.sleep(1.0)
            back_cmd5 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd5)
            time.sleep(1.0)
            back_cmd6 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd6)
            time.sleep(1.0)
            back_cmd7 = 'adb -s %s shell input keyevent 4' % self.xiaomi_udid
            os.popen(back_cmd7)
            time.sleep(1.0)
            self.add()
        else:
            if self.force_stop_count >= 0:
                start_cmd1 = 'adb -s %s shell am start com.tencent.mm/.ui.LauncherUI' % self.xiaomi_udid
                os.popen(start_cmd1)
                time.sleep(3.0)
                self.exception()
                self.force_stop_count -= 1
            else:
                try:
                    stop_cmd = 'adb -s %s shell am force-stop com.tencent.mm' % self.xiaomi_udid
                    os.popen(stop_cmd)
                    time.sleep(3.0)
                    start_cmd = 'adb -s %s shell am start com.tencent.mm/.ui.LauncherUI' % self.xiaomi_udid
                    os.popen(start_cmd)
                    time.sleep(self.launch_time)
                    WebDriverWait(self.driver, self.launch_time).until(lambda x: x.find_element_by_id('com.tencent.mm:id/hu'))
                    self.add()
                except Exception as e:
                    self.exception()

if __name__ == '__main__':
    add_fri = AddFriend()
    try:
        add_fri.get_driver()
        add_fri.add()
    except Exception as e:
        add_fri.exception()