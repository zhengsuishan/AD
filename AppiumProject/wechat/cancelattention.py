from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os

class CancelAttention(object):

    driver = None
    launch_time = 15.0
    wait_time = 3.0
    public_num = 141

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.1.0'
        desired_caps['deviceName'] = 'd102deb37d13'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['udid'] = 'd102deb37d13'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        WebDriverWait(self.driver, self.launch_time).until(lambda x:x.find_element_by_name('通讯录'))
        self.driver.find_element_by_name('通讯录').click()
        WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('公众号'))
        self.driver.find_element_by_name('公众号').click()
        WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.tencent.mm:id/a6c'))

    def cancel_method(self, num):
        for i in range(0, num):
            click_cmd = 'adb -s d102deb37d13 shell input swipe 343 256 343 256 1000'
            os.popen(click_cmd)
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('取消关注'))
            self.driver.find_element_by_name('取消关注').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('不再关注'))
            self.driver.find_element_by_name('不再关注').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_id('com.tencent.mm:id/a6c'))

if __name__ == '__main__':
    calcel = CancelAttention()
    try:
        calcel.get_driver()
        calcel.cancel_method(calcel.public_num)
    except Exception as e:
        calcel.driver = None