# -*-codingLutf-8-*-
# 自动化加群

from selenium.webdriver.support.wait import WebDriverWait
from AppiumProject.qq.add_qun.locators import Locators
import random
import time
import traceback

class AddQun(object):

    driver = None
    launch_time = 15
    wait_time = 5
    qun_num = []

    def get_qun_num(self):
        num_list = ['0', '1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9']

        qun_len = random.randint(6, 8)

        for qun_changdu in range(0, qun_len - 1):
            index = random.randint(-1, len(num_list) - 1)
            self.qun_num.append(num_list[index])

        return ''.join(self.qun_num)

    def set_driver(self, driver, text):
        self.driver = driver

    def go_verfication(self):

        if Locators.NOT_QUN[1] in self.driver.page_source:
            self.driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]).click() #清空输入框
            time.sleep(1.0)
        else:
            WebDriverWait(self.driver, self.launch_time).until(
                lambda driver: driver.find_element_by_accessibility_id(Locators.ADD_RIGHT[1]))  # 等待首页右上角+号按钮出现
            self.driver.find_element_by_accessibility_id(Locators.ADD_RIGHT[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.ADD_FRI_QUN[0], Locators.ADD_FRI_QUN[1]))  # 等待加好友/群按钮出现
            self.driver.find_element(Locators.ADD_FRI_QUN[0], Locators.ADD_FRI_QUN[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.FIND_QUN[0], Locators.FIND_QUN[1]))  # 等待找群按钮出现
            self.driver.find_element(Locators.FIND_QUN[0], Locators.FIND_QUN[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.QQ_PHONE_PUBLIC[0], Locators.QQ_PHONE_PUBLIC[1]))  # 等待输入框出现
        self.driver.find_element(Locators.QQ_PHONE_PUBLIC[0], Locators.QQ_PHONE_PUBLIC[1]).send_keys(self.get_qun_num(AddQun))
        time.sleep(1.0)
        self.driver.find_element(Locators.FIND_QUN_NUM[0], Locators.FIND_QUN_NUM[1]).click()

        #判断是否查到结果, 没查到继续查，查到了下一步
        try:
            WebDriverWait(self.driver, 1.5).until(lambda driver:driver.find_element(Locators.NOT_QUN[0], Locators.NOT_QUN[1]))
            self.go_verfication(AddQun)
        except Exception as e:
            print(traceback.print_exc())


if __name__ == '__main__':
    print(AddQun.get_qun_num(AddQun))