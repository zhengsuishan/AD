# -*- coding:utf-8 -*-
# 发送群消息

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import traceback

class SendQun(object):

    driver = None
    launch_time = 15
    wait_time = 5
    udid = 'H8018K9012345678'
    swipe_y1 = 1000
    swipe_y2 = 880
    picture_x = 135 #图片x坐标
    picture_y = 1164 #图片y坐标
    one_x = 115
    two_x = 265
    three_x = 415
    y = 958
    news = '看视频就能赚零花钱，有兴趣的下载了解下'

    #获取driver
    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'W6'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['udid'] = 'H8018K9012345678'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        try:
            WebDriverWait(self.driver, self.launch_time).until(lambda x: x.find_element_by_name('联系人'))
        except Exception as e:
            self.exce_do()

    #发送消息
    def send_news(self):
        try:
            if '群聊' in self.driver.page_source and '设备' in self.driver.page_source:
                pass
            else:
                self.driver.find_element_by_name('联系人').click()
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/text1'))
            text = self.driver.find_element_by_id('com.tencent.mobileqq:id/text1').get_attribute('text')  # 保存群名称
            self.driver.find_element_by_id('com.tencent.mobileqq:id/text1').click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightImage'))

            if '全员禁言中' in self.driver.page_source:
                back_cmd = 'adb -s %s shell input keyevent 4' % self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda driver: driver.find_element_by_name('联系人'))
                self.driver.find_element_by_name('联系人').click()
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/text1'))

                while text in self.driver.page_source:
                    swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 500' % (
                        self.udid, self.swipe_y1, self.swipe_y2)
                    os.popen(swipe_cmd)
                    time.sleep(3.0)
                else:
                    self.send_news()
            elif self.news in self.driver.page_source:
                back_cmd = 'adb -s %s shell input keyevent 4' % self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element_by_name('联系人'))
                self.driver.find_element_by_name('联系人').click()
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/text1'))

                while text in self.driver.page_source:
                    swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 500' % (
                        self.udid, self.swipe_y1, self.swipe_y2)
                    os.popen(swipe_cmd)
                    time.sleep(3.0)
                else:
                    self.send_news()
            else:
                click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.picture_x, self.picture_y)
                os.popen(click_cmd)
                time.sleep(2.0)

                WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element_by_name('相册'))

                click_cmd1 = 'adb -s %s shell input tap %d %d' % (self.udid, self.one_x, self.y)
                os.popen(click_cmd1)
                time.sleep(1.0)
                click_cmd2 = 'adb -s %s shell input tap %d %d' % (self.udid, self.two_x, self.y)
                os.popen(click_cmd2)
                time.sleep(1.0)
                click_cmd3 = 'adb -s %s shell input tap %d %d' % (self.udid, self.three_x, self.y)
                os.popen(click_cmd3)
                WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element_by_name('发送(3)'))
                self.driver.find_element_by_name('发送(3)').click()
                time.sleep(1.0)
                self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(self.news)
                time.sleep(1.0)
                self.driver.find_element_by_name('发送').click()
                time.sleep(1.0)

                back_cmd5 = 'adb -s %s shell input keyevent 4' % self.udid
                os.popen(back_cmd5)
                time.sleep(1.0)
                back_cmd6 = 'adb -s %s shell input keyevent 4' % self.udid
                os.popen(back_cmd6)
                WebDriverWait(self.driver, self.wait_time).until(lambda driver: driver.find_element_by_name('联系人'))
                self.driver.find_element_by_name('联系人').click()
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/text1'))

                while text in self.driver.page_source:
                    swipe_cmd = 'adb -s %s shell input swipe 360 %d 360 %d 500' % (
                        self.udid, self.swipe_y1, self.swipe_y2)
                    os.popen(swipe_cmd)
                    time.sleep(3.0)
                else:
                    self.send_news()
        except Exception as e:
            print(traceback.print_exc())



    #异常处理
    def exce_do(self):
        pass

if __name__ == '__main__':

    obj = SendQun()
    try:
        obj.get_driver()
        obj.send_news()
    except Exception as e:
        obj.exce_do()