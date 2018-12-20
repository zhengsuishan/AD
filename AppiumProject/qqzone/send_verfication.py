# -*- coding:utf-8 -*-
from AppiumProject.qqzone.init_para import InitPara
from selenium.webdriver.support.wait import WebDriverWait
from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qqzone.locators import Locators
import random
import time
import os
import traceback

class SendVerfication(object):

    udid = None

    launch_time = 15
    wait_time = 5
    driver = None

    send_times = None
    user_swipe_times = 0

    def set_udid_driver(self, udid, driver):
        self.udid = udid
        self.driver = driver

    #获取文案
    def get_text(self):
        text1 = ''
        text2 = ''
        text3 = ''
        text_list = [text1, text2, text3]
        size = len(text_list)
        index = random.randint(-1, size - 1)
        return text_list[index]

    def read_count(self):
        file_name = 'send_count'
        file = open(file_name).readlines()
        return int(file[0])

    def write_count(self, param):
        file_name = 'send_count'
        file = open(file_name, 'w+')
        file.write(str(param))
        file.close()

    def launch_app(self):
        try:
            WebDriverWait(self.driver, self.launch_time).until(
                lambda driver: driver.find_element(Locators.MAIN_PAGE_VIDEO[0], Locators.MAIN_PAGE_VIDEO[1]))
            self.driver.find_element(Locators.MAIN_PAGE_VIDEO[0], Locators.MAIN_PAGE_VIDEO[1]).click()
        except Exception as e:
            print(traceback.print_exc())

    def add_fri(self):
        swipe_cmd_user = 'adb -s %s shell input swipe %d %d %d %d %d' % (self.udid, 360, 640, 360, 640 - 145, 300)
        swipe_cmd_video = 'adb -s %s shell input swipe %d %d %d %d %d' % (self.udid, 360, 640, 360, 640 - 600, 300)
        back_cmd = 'adb -s %s shell input keyevent 4' % self.udid
        try:
            if Locators.SAY[1] in self.driver.page_source:
                pass
            else:
                # 读取发送次数
                self.send_times = self.read_count(SendVerfication)

                # 判断是否是广告
                try:
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda driver: driver.find_element(Locators.USER_COMMENT[0], Locators.USER_COMMENT[1]))
                except Exception as e:
                    # 滑动屏幕
                    os.popen(swipe_cmd_video)
                    self.user_swipe_times = 0
                    time.sleep(1.5)
                    self.add_fri(SendVerfication)

                # 获取评论数
                pl_num = self.driver.find_element(Locators.USER_COMMENT[0], Locators.USER_COMMENT[1]).get_attribute(
                    'text')
                pl_num = int(pl_num)

                # 判断评论数是否大于100
                if pl_num >= 100:
                    self.driver.find_element(Locators.USER_COMMENT[0], Locators.USER_COMMENT[1]).click()
                else:
                    os.popen(swipe_cmd_video)
                    time.sleep(1.5)
                    self.add_fri(SendVerfication)

            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.USER_ID[0], Locators.USER_ID[1]))
            self.driver.find_element(Locators.USER_ID[0], Locators.USER_ID[1]).click()  # 点击用户头像

            if Locators.ADD_TEXT[1] in self.driver.page_source:
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.ADD_TEXT[0], Locators.ADD_TEXT[1]))
                self.driver.find_element(Locators.ADD_TEXT[0], Locators.ADD_TEXT[1]).click()  # 点击加为好友
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.VERFICATION[0], Locators.VERFICATION[1]))
                self.driver.find_element(Locators.VERFICATION[0], Locators.VERFICATION[1]).send_keys(
                    self.get_text(SendVerfication))  # 输入内容

                time.sleep(0.5)

                self.driver.find_element(Locators.SUBMIT[0], Locators.SUBMIT[1]).click()
                self.send_times += 1
                self.write_count(SendVerfication, self.send_times)
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.ADD_TEXT[0], Locators.ADD_TEXT[1]))
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(Locators.USER_ID[0], Locators.USER_ID[1]))

                # 滑动屏幕
                os.popen(swipe_cmd_user)
                time.sleep(1.5)
                self.user_swipe_times += 1

                # 判断一个视频的评论数-5 >=划动次数
                if pl_num - 5 >= self.user_swipe_times:
                    os.popen(back_cmd)
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda driver: driver.find_element(Locators.USER_ID[0], Locators.USER_ID[1]))
                    self.add_fri(SendVerfication)
                else:
                    self.add_fri(SendVerfication)
            else:
                os.popen(back_cmd)
                time.sleep(1.5)
                self.add_fri(SendVerfication)

        except Exception as e:
            print(traceback.print_exc())

if __name__ == '__main__':
    pass