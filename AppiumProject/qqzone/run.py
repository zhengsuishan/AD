# -*- coding:utf-8 -*-

from appium import webdriver
from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qqzone.init_para import InitPara
from AppiumProject.qqzone.send_verfication import SendVerfication
import os

if __name__ == '__main__':

    driver = None
    udid = 'd102deb37d13'
    package = 'com.qzone'
    activity = 'com.tencent.sc.activity.SplashActivity'

    # 设置输入法
    setting_cmd = 'adb -s %s shell ime set io.appium.android.ime/.UnicodeIME'%udid
    os.popen(setting_cmd)

    InitPara.set_desired_caps(InitPara, udid, package, activity)
    desired_caps = InitPara.get_desired_caps(InitPara)

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    SendVerfication.set_udid_driver(SendVerfication, udid, driver)
    SendVerfication.launch_app(SendVerfication)
    SendVerfication.add_fri(SendVerfication)