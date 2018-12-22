# -*- coding:utf-8 -*-

from appium import webdriver

from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qq.send_message_to_qun.init_para import InitParm
from AppiumProject.qq.send_message_to_qun.send_to_qun import SendToQun

import os
import time

if __name__ == '__main__':

    driver = None
    desired_caps = InitParm.desired_caps

    temp_bool = True
    while temp_bool:
        # 启动appium
        os.popen('taskkill /f /im cmd.exe')
        time.sleep(1.5)
        os.popen('start appium')
        time.sleep(15.0)
        try:
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            temp_bool = False
        except Exception as e:
            time.sleep(60)

    InitDriver.set_driver(InitDriver, driver)
    SendToQun.get_driver(SendToQun)
    SendToQun.go_qun_list(SendToQun)
    SendToQun.send(SendToQun)