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
    device_udid = 'd102deb37d13'

    #判断屏幕是否亮屏
    is_light_cmd = 'adb shell "dumpsys window policy|grep mScreenOnFully"'
    res = os.popen(is_light_cmd).readlines()[0].split(' ')[4].split('=')[1]
    if res == 'true':
        pass
    else:
        wake_cmd = 'adb -s %s shell input keyevent 26' % device_udid
        os.popen(wake_cmd)
        time.sleep(2.0)
        swipe_cmd = 'adb -s %s shell input swipe 360 800 360 100 100' % device_udid
        os.popen(swipe_cmd)
        time.sleep(1.0)

    light_cmd = 'adb -s %s shell settings put system screen_brightness 1'%device_udid
    os.popen(light_cmd)
    time.sleep(1.0)

    auto_cmd = 'adb -s %s shell settings put system screen_brightness_mode 0'%device_udid
    os.popen(auto_cmd)
    time.sleep(1.0)

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

    time.sleep(1.0)
    auto_cmd = 'adb -s %s shell settings put system screen_brightness_mode 1' % device_udid
    os.popen(auto_cmd)
    time.sleep(1.0)

    close_cmd = 'adb -s %s shell input keyevent 26'%device_udid
    os.popen(close_cmd)
