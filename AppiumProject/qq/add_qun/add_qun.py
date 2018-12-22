# -*-codingLutf-8-*-
# 自动化加群

from selenium.webdriver.support.wait import WebDriverWait
from AppiumProject.qq.add_qun.locators import Locators
import random
import time
import traceback
import os

class AddQun(object):

    driver = None
    launch_time = 15
    wait_time = 5
    qun_num = []
    udid = None

    def get_qun_num(self):
        num_list = ['0', '1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9']

        qun_len = random.randint(6, 8)

        for qun_changdu in range(0, qun_len - 1):
            index = random.randint(-1, len(num_list) - 1)
            self.qun_num.append(num_list[index])

        return ''.join(self.qun_num)

    def set_driver(self, driver, udid):
        self.driver = driver
        self.udid = udid

    def launch_app(self):
        try:
            WebDriverWait(self.driver, self.launch_time).until(
                lambda driver: driver.find_element(Locators.ADD_RIGHT[0], Locators.ADD_RIGHT[1]))
        except Exception as e:
            self.exce_do(AddQun)

    def go_verfication(self):
        try:
            back_cmd = 'adb -s %s shell input keyevent 4' % self.udid
            if Locators.NOT_QUN[1] in self.driver.page_source:
                self.driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]).click()  # 清空输入框
                time.sleep(1.0)
            elif Locators.FIND_QUN_NUM[1] in self.driver.page_source:
                self.driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]).click()  # 清空输入框
                time.sleep(1.0)
            elif Locators.QQ_PHONE_PUBLIC[1] in self.driver.page_source:
                pass
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
                    lambda driver: driver.find_element(Locators.QQ_PHONE_PUBLIC[0],
                                                       Locators.QQ_PHONE_PUBLIC[1]))  # 等待输入框出现
            self.driver.find_element(Locators.QQ_PHONE_PUBLIC[0], Locators.QQ_PHONE_PUBLIC[1]).send_keys(
                self.get_qun_num(AddQun))
            self.qun_num = []
            time.sleep(1.0)
            self.driver.find_element(Locators.FIND_QUN_NUM[0], Locators.FIND_QUN_NUM[1]).click()

            # 判断是否查到结果, 没查到继续查，查到了下一步
            try:
                WebDriverWait(self.driver, 3.0).until(
                    lambda driver: driver.find_element(Locators.NOT_QUN[0], Locators.NOT_QUN[1]))
                self.go_verfication(AddQun)
            except Exception as e:
                time.sleep(3.0)
                if Locators.FIND_RES[1] in self.driver.page_source:
                    os.popen(back_cmd)
                    time.sleep(1.5)
                    self.go_verfication(AddQun)
                elif Locators.SEND_MESSAGE[1] in self.driver.page_source:
                    os.popen(back_cmd)
                    time.sleep(1.5)
                    self.go_verfication(AddQun)
                else:
                    self.apply_add_qun(AddQun)
        except Exception as e:
            self.exce_do(AddQun)

    #申请加群
    def apply_add_qun(self):
        try:
            back_cmd = 'adb -s %s shell input keyevent 4' % self.udid

            text = self.driver.find_element(Locators.QUN_PEOPLE_NUM[0], Locators.QUN_PEOPLE_NUM[1]).get_attribute(
                'text')
            text = text.split('人')
            num = int(text[0])
            # 判断群人数是否大于10
            if num >= 10:
                self.driver.find_element(Locators.APPLY_ADD_QUN[0], Locators.APPLY_ADD_QUN[1]).click()  # 点击申请加群
                time.sleep(3.0)

                # 判断点击申请加群后，该群是否允许加入
                if Locators.APPLY_ADD_QUN[1] in self.driver.page_source:
                    os.popen(back_cmd)
                    time.sleep(1.5)
                    self.go_verfication(AddQun)
                else:
                    # 判断是否需要填写问题
                    if Locators.PERSON[1] in self.driver.page_source:
                        self.driver.find_element(Locators.SUBMIT[0], Locators.SUBMIT[1]).click()
                        WebDriverWait(self.driver, self.wait_time).until(
                            lambda driver: driver.find_element(Locators.SEND_SUCCESS[0], Locators.SEND_SUCCESS[1]))
                        os.popen(back_cmd)
                        WebDriverWait(self.driver, self.wait_time).until(
                            lambda driver: driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]))
                        self.go_verfication(AddQun)
                    else:
                        time.sleep(10)
                        print('未知界面')
                        os.popen(back_cmd)
                        time.sleep(1.0)
                        os.popen(back_cmd)
                        time.sleep(1.0)
                        self.go_verfication(AddQun)
            else:
                os.popen(back_cmd)
                time.sleep(1.5)
                self.go_verfication(AddQun)
        except Exception as e:
            self.exce_do(AddQun)

    def element(self, locator):
        try:
            self.driver.find_element(locator[0], locator[1])
            return True
        except Exception as e:
            return False

    #异常处理
    def exce_do(self):
        back_cmd = 'adb -s %s shell input keyevent 4' % self.udid
        if Locators.QQ_PHONE_PUBLIC[1] in self.driver.page_source and Locators.FIND_QUN[1] not in self.driver.page_source:
            self.go_verfication(AddQun)
        elif Locators.FIND_QUN_NUM[1] in self.driver.page_source:
            self.driver.find_element(Locators.FIND_QUN_NUM[0], Locators.FIND_QUN_NUM[1]).click()
            # 判断是否查到结果, 没查到继续查，查到了下一步
            try:
                WebDriverWait(self.driver, 3.0).until(
                    lambda driver: driver.find_element(Locators.NOT_QUN[0], Locators.NOT_QUN[1]))
                self.go_verfication(AddQun)
            except Exception as e:
                time.sleep(3.0)
                if Locators.FIND_RES[1] in self.driver.page_source:
                    os.popen(back_cmd)
                    time.sleep(1.5)
                    self.go_verfication(AddQun)
                else:
                    self.apply_add_qun(AddQun)
        elif Locators.APPLY_ADD_QUN[1] in self.driver.page_source:
            self.apply_add_qun(AddQun)
        elif Locators.PERSON[1] in self.driver.page_source:
            self.driver.find_element(Locators.SUBMIT[0], Locators.SUBMIT[1]).click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.SEND_SUCCESS[0], Locators.SEND_SUCCESS[1]))
            os.popen(back_cmd)
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]))
            self.go_verfication(AddQun)
        elif Locators.SEND_SUCCESS[1] in self.driver.page_source:
            os.popen(back_cmd)
            WebDriverWait(self.driver, self.wait_time).until(
                lambda driver: driver.find_element(Locators.CLEAR[0], Locators.CLEAR[1]))
            self.go_verfication(AddQun)
        elif self.element(AddQun, Locators.RIGHT_ID):
            os.popen(back_cmd)
            time.sleep(1.5)
            self.go_verfication(AddQun)
        else:
            self.driver.get_screenshot_as_file('error.png')
            raise '未知界面'

if __name__ == '__main__':
    print(AddQun.get_qun_num(AddQun))