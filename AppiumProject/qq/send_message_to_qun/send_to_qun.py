# -*- coding:utf-8 -*-

import os
import time
import traceback

from selenium.webdriver.support.wait import WebDriverWait

from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qq.send_message_to_qun.init_para import InitParm
from AppiumProject.qq.send_message_to_qun.locators import Locators
from AppiumProject.qq.send_message_to_qun.main_page import MainPage


class SendToQun(object):

    udid = InitParm.device_udid
    qun_name_list = InitParm.qun_name_list
    swipe_dur = 112
    swipe_x = 360
    swie_y = 1000
    swipe_time = 500
    swipe_cmd = 'adb -s %s shell input swipe %d %d %d %d %d'%(udid, swipe_x, swie_y, swipe_x, swie_y-swipe_dur, swipe_time)

    xiang_ce_x = 153.5
    xiang_ce_y = 1240
    xiangce_click_cmd = 'adb -s %s shell input tap %d %d'%(udid, xiang_ce_x, xiang_ce_y)
    click_x = 115
    click_x_dur = 150
    click_y = 923

    driver = None
    wait_time = 5
    launch_time = 15
    qun_list_index = 0

    back_cmd = 'adb -s %s shell input keyevent 4' % udid

    pic_index = InitParm.index
    send_text = InitParm.send_text
    send_text1 = InitParm.send_text1
    text = InitParm.text

    command1 = 'adb -s %s shell settings get secure default_input_method'%udid
    command3 = 'adb -s %s shell ime set io.appium.android.ime/.UnicodeIME'%udid

    swipe_count = 0 #划动次数超过群列表大小，自动查找下一个群

    def get_driver(self):
        self.driver = InitDriver.get_driver(InitDriver)

        shurufa = os.popen(self.command1)
        if shurufa == 'io.appium.android.ime/.UnicodeIME':
            pass
        else:
            os.popen(self.command3)
            time.sleep(1.0)

    def go_qun_list(self):

        if self.qun_list_index == len(self.qun_name_list) - 1:
            self.driver = None
            exit()
        else:
            pass

        try:
            WebDriverWait(self.driver, self.launch_time).until(lambda driver:driver.find_element(Locators.CONTACT[0], Locators.CONTACT[1]))
            self.driver.find_element(Locators.CONTACT[0], Locators.CONTACT[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.QUN_CHAT[0], Locators.QUN_CHAT[1]))
            self.driver.find_element(Locators.QUN_CHAT[0], Locators.QUN_CHAT[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.QUN_NAME_ID[0], Locators.QUN_NAME_ID[1]))
        except Exception as e:
            print(traceback.print_exc())
            MainPage.back_to_main_page(MainPage)
            self.go_qun_list(SendToQun)
            self.send(SendToQun)

    def send(self):
        try:

            if self.qun_list_index >= len(self.qun_name_list):
                exit()
            else:
                pass

            if self.qun_name_list[self.qun_list_index] in self.driver.page_source:
                self.swipe_count = 0
                try:
                    self.driver.find_element_by_name(self.qun_name_list[self.qun_list_index]).click()
                except Exception as e:
                    if 'An element could not be located on the page using the given search parameters.' in str(e):
                        self.qun_list_index += 1
                        self.go_qun_list(SendToQun)
                        self.send(SendToQun)
                    else:
                        pass

                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.PIC[0], Locators.PIC[1]))
                if Locators.SLIENT[1] in self.driver.page_source:
                    os.popen(self.back_cmd)
                    time.sleep(1.0)
                    self.qun_list_index += 1
                    self.go_qun_list(SendToQun)
                    self.send(SendToQun)
                else:
                    if self.send_text1 in self.driver.page_source:
                        os.popen(self.back_cmd)
                        time.sleep(1.0)
                        self.qun_list_index += 1
                        self.go_qun_list(SendToQun)
                        self.send(SendToQun)
                    else:
                        self.select_pict(SendToQun, self.pic_index, self.text)
                        time.sleep(1.0)
                        os.popen(self.back_cmd)
                        time.sleep(1.0)
                        self.qun_list_index += 1
                        self.go_qun_list(SendToQun)
                        self.send(SendToQun)
            else:
                os.popen(self.swipe_cmd)
                time.sleep(1.0)
                self.swipe_count += 1

                if self.swipe_count >= 5:
                    self.qun_list_index += 1
                else:
                    pass

                self.send(SendToQun)
        except Exception as e:
            print(traceback.print_exc())
            MainPage.back_to_main_page(MainPage)
            self.go_qun_list(SendToQun)
            self.send(SendToQun)

    #设置发送几张图片0-3：0代表不发图片
    def select_pict(self, index, text):
        try:
            if index == 0:
                pass
            elif index == 1:
                os.popen(self.xiangce_click_cmd)
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.XIANG_CE[0], Locators.XIANG_CE[1]))
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.click_x, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)

                try:
                    self.driver.find_element(Locators.SEND_ONE[0], Locators.SEND_ONE[1]).click()
                except Exception as e:
                    time.sleep(1.0)
                    if Locators.SEND_ONE[1] in self.driver.page_source:
                        self.driver.find_element(Locators.SEND_ONE[0], Locators.SEND_ONE[1]).click()
                    else:
                        pic_click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.click_x, self.click_y)
                        os.popen(pic_click_cmd)
                        time.sleep(1.0)
                        self.driver.find_element(Locators.SEND_ONE[0], Locators.SEND_ONE[1]).click()
                time.sleep(0.5)
            elif index == 2:
                os.popen(self.xiangce_click_cmd)
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.XIANG_CE[1]))
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.click_x, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, self.click_x + self.click_x_dur, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)
                self.driver.find_element(Locators.SEND_TWO[0], Locators.SEND_TWO[1]).click()
                time.sleep(0.5)
            elif index == 3:
                os.popen(self.xiangce_click_cmd)
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.XIANG_CE[0], Locators.XIANG_CE[1]))
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, self.click_x, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, self.click_x + self.click_x_dur, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)
                pic_click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, self.click_x + self.click_x_dur + self.click_x_dur, self.click_y)
                os.popen(pic_click_cmd)
                time.sleep(1.0)
                self.driver.find_element(Locators.SEND_THREE[0], Locators.SEND_THREE[1]).click()
                time.sleep(0.5)
            else:
                pass

            if text == 1:

                try:
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda driver: driver.find_element(Locators.SENG_INPUT[0], Locators.SENG_INPUT[1]))
                except Exception as e:
                    # 处理群消息
                    if Locators.QUN_TZ[1] in self.driver.page_source:
                        self.driver.find_element(Locators.QUN_TZ[0], Locators.QUN_TZ[1]).click()
                        time.sleep(1.5)
                    else:
                        self.driver.get_screenshot_as_file('error.png')
                        time.sleep(3.0)

                self.driver.find_element(Locators.SENG_INPUT[0], Locators.SENG_INPUT[1]).send_keys(self.send_text)
                time.sleep(1.0)
                self.driver.find_element(Locators.SEND[0], Locators.SEND[1]).click()
                time.sleep(1.0)
                self.driver.find_element(Locators.SENG_INPUT[0], Locators.SENG_INPUT[1]).send_keys(self.send_text1)
                time.sleep(1.0)
                self.driver.find_element(Locators.SEND[0], Locators.SEND[1]).click()
                time.sleep(1.0)
            else:
                pass
        except Exception as e:
            print(traceback.print_exc())
            MainPage.back_to_main_page(MainPage)
            self.go_qun_list(SendToQun)
            self.send(SendToQun)

if __name__ == '__main__':
    os.popen(SendToQun.swipe_cmd)
