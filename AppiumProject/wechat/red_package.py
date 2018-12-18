from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

class RedPackage(object):

    get_time = None
    bool_new_mess = True
    launch_time = 15.0
    new_mess_id = 'com.tencent.mm:id/lu' #用户判断是否存在新消息
    driver = None

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.1.0'
        desired_caps['deviceName'] = 'xiaomi'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['udid'] = 'd102deb37d13'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        WebDriverWait(self.driver, self.launch_time).until(lambda x: x.find_element_by_name('发现'))

        while True:
            time.sleep()
            try:
                self.get_time = time.strftime('%H:%M', time.localtime())

                #判断是否在主界面
                if '通讯录' in self.driver.page_source and '发现' in self.driver.page_source:
                    pass
                else:
                    raise NameError('界面异常')

                if self.get_time in self.driver.page_source:
                    self.driver.find_element_by_name(self.get_time).click()

                    try:
                        WebDriverWait(self.driver, 3.0).until(lambda x: x.find_element_by_name('领取红包'))  # 等待红包出现
                        self.driver.find_element_by_name('领取红包').click()
                        WebDriverWait(self.driver, 5.0).until(lambda x: x.find_element_by_id('com.tencent.mm:id/clb'))
                        if '手慢了，红包派完了' in self.driver.page_source:
                            cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                            os.popen(cmd)
                            time.sleep(0.5)
                            cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                            os.popen(cmd)
                        else:
                            self.driver.find_element_by_id('com.tencent.mm:id/cnu').click()
                            WebDriverWait(self.driver, 3.0).until(lambda x: x.find_element_by_name('红包详情'))
                            cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                            os.popen(cmd)
                            time.sleep(0.5)
                            cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                            os.popen(cmd)

                    except Exception as e:
                        cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                        os.popen(cmd)

                    WebDriverWait(self.driver, 3.0).until(lambda x: x.find_element_by_name('通讯录'))

                else:
                    pass
            except Exception as e:
                if '界面异常' in str(e):
                    for i in range(0, 2):
                        cmd = 'adb -s d102deb37d13 shell input keyevent 4'
                        os.popen(cmd)
                        time.sleep(0.5)
                    start_cmd = 'adb -s d102deb37d13 shell am start com.tencent.mm/.ui.LauncherUI'
                    os.popen(start_cmd)
                    time.sleep(1.0)

if __name__ == '__main__':
    rp = RedPackage()
    rp.get_driver()