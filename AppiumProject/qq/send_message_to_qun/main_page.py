# -*- coding:utf-8 -*-
# 判断当前是哪个界面，返回主界面
import os
import time

from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qq.send_message_to_qun.init_para import InitParm
from AppiumProject.qq.send_message_to_qun.locators import Locators


class MainPage(object):

    driver = None
    udid = InitParm.device_udid
    back_cmd = 'adb -s %s shell input keyevent 4' % udid
    wake_cmd = 'adb -s %s shell am start com.tencent.mobileqq/.activity.SplashActivity' % udid

    def get_driver(self):
        self.driver = InitDriver.get_driver(InitDriver)

    def element(self, locator):
        try:
            self.driver.find_element(locator[0], locator[1])
            return True
        except Exception as e:
            return False

    def back_to_main_page(self):
        print('ooooooooooooooooooooo')
        self.get_driver(MainPage)
        if Locators.NEWS[1] in self.driver.page_source and Locators.CONTACT[1] in self.driver.page_source and Locators.LOOK[1] in self.driver.page_source and Locators.DYNAMIC[1] in self.driver.page_source:
            self.driver.find_element(Locators.NEWS[0], Locators.NEWS[1]).click()
            time.sleep(1.0)
        elif self.element(MainPage, Locators.RIGHT_ID) or Locators.SLIENT[1] in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
        elif Locators.XIANG_CE[1] in self.driver.page_source and Locators.BIAN_JI[1] in self.driver.page_source and Locators.YUAN_TU[1] in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            os.popen(self.back_cmd)
            time.sleep(1.0)
        else:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.back_to_main_page(MainPage)