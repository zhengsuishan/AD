# -*- coding:utf-8 -*-
from appium import webdriver
from AppiumProject.qq.add_fri.init_para import InitPara
from AppiumProject.qq.add_fri.add_friend import AddFriend
import time
import os

if __name__ == '__main__':
    driver = None
    udid = 'd102deb37d13'
    package = 'com.tencent.mobileqq'
    activity = 'com.tencent.mobileqq.activity.SplashActivity'
    start_activity = 'com.tencent.mobileqq/.activity.SplashActivity'

    # 设置输入法
    setting_cmd = 'adb -s %s shell ime set io.appium.android.ime/.UnicodeIME' % udid
    os.popen(setting_cmd)

    InitPara.set_desired_caps(InitPara, udid, package, activity)
    des_cap = InitPara.get_desired_caps(InitPara)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_cap)

    time.sleep(3.0)

    AddFriend.set_driver_udid_appinfo(AddFriend, driver, udid, package, start_activity)
    AddFriend.go_add(AddFriend)
