# -*- coding:utf-8 -*-

from appium import webdriver
from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qqzone.init_para import InitPara
from AppiumProject.qqzone.send_verfication import SendVerfication

if __name__ == '__main__':
    driver = None
    udid = 'd102deb37d13'
    package = 'com.qzone'
    activity = 'com.tencent.sc.activity.SplashActivity'

    SendVerfication.set_udid(SendVerfication, udid)

    InitPara.set_desired_caps(InitPara, udid, package, activity)
    desired_caps = InitPara.get_desired_caps(InitPara)

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    InitDriver.set_driver(InitDriver, driver)

    SendVerfication.launch_app(SendVerfication)
    SendVerfication.add_fri(SendVerfication)