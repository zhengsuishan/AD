# -*- coding:utf-8 -*-

from appium import webdriver
from AppiumProject.qq.add_qun.init_para import InitPara
from AppiumProject.qq.add_qun.add_qun import AddQun
import time
import os
import traceback

if __name__ == '__main__':
    driver = None
    udid = 'd102deb37d13'
    package = 'com.tencent.mobileqq'
    activity = 'com.tencent.mobileqq.activity.SplashActivity'

    InitPara.set_desired_caps(InitPara, udid, package, activity)
    desired_caps = InitPara.get_desired_caps(InitPara)

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

    try:
        AddQun.set_driver(AddQun, driver, udid=udid)
        AddQun.launch_app(AddQun)
        AddQun.go_verfication(AddQun)
        AddQun.apply_add_qun(AddQun)
    except Exception as e:
        print(traceback.print_exc())
