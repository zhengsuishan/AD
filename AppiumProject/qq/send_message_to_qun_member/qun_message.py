import xlrd
import os
import time
import sys
import json
from xlutils.copy import copy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import traceback

class QunMessage(object):

    driver = None
    swipeDur = 87 #滑动间距
    launch_time = 60 #启动时间
    file_name = 'data.xlsx' #文件路径
    qun_name = None #群名称
    qun_num = None #群人数
    line = None #保存当前操作的是第几行
    send_times = None #发送的次数
    click_zimu = None #点击的字母
    temp_swpie_times = None #临时保存滑动次数
    wait_time = 5.0 #超时等待
    qun_list_wait_time = 60.0 #进入群列表等待时间
    qun_list_name_id = 'com.tencent.mobileqq:id/tv_name'
    #message_content = '支付宝发红包啦，赶紧领取，打开支付宝首页搜索“499754”，即可领红包，每天都可以领取哦；没有支付宝赶紧下载https://m.alipay.com/DPlKoAc，注册即可领取现金红包。1014'
    temp_num = 0 #记录启动appium的次数
    data_json = None
    udid = 'd102deb37d13'

    message_content_url = '当心！有人路过你身边，就能刷走-你-的-钱！https://mini.eastday.com/mobile/181217154453129.html?ca=809169121&f1=xq1'
    message_content = '当心！有人路过你身边，就能刷走-你-的-钱！'
    #haha小视频
    #message_content = '哈哈小视频，一款边刷视频边赚钱的软件，和抖音一样好玩，关键是还能赚钱哦。'
    #haha_content = '有兴趣的话，扫码下载注册试试吧。'


    def loop_step(self):
        #print(sys._getframe().f_code.co_name)
        try:
            self.get_nameandnum()
            self.change_to_false()
            self.speak_isexists_and_click_qunname()
            self.click_letter(self.click_zimu)
            self.swipe_qunchengyuan(self.send_times)
            self.click_ok_by_id()
            self.send_new()
        except Exception as e:
            #print('loop_step异常信息: %s'%e)
            #print(traceback.print_exc())
            self.exce_method()

    #获取driver
    def get_driver(self):
        #print(sys._getframe().f_code.co_name)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'W6'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['noReset'] = 'true'
        desired_caps['udid'] = self.udid
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        try:
            WebDriverWait(self.driver, self.launch_time).until(lambda x:x.find_element_by_name('联系人'))
        except Exception as e:
            #print('get_driver异常信息: %s' % e)
            if 'Message' in e:
                pass
            else:
                self.exce_method()

    #发送次数大于群人数，将yes变为false
    def change_to_false(self):
        last_qum = int(self.data_json['26'])
        if self.click_zimu >= 26 and self.send_times >= last_qum:
            workbook = xlrd.open_workbook(self.file_name)
            workbook_new = copy(workbook)
            ws = workbook_new.get_sheet(0)
            ws.write(self.line, 0, 'no')
            ws.write(self.line + 1, 0, 'yes')
            workbook_new.save(self.file_name)
        else:
            pass

    #读取群昵称和群人数
    def get_nameandnum(self):
        work_book = xlrd.open_workbook(self.file_name)
        sheet = work_book.sheet_by_index(0)
        rows = sheet.nrows
        for i in range(0, rows):
            if sheet.cell_value(i, 0) == 'yes':
                self.qun_name = sheet.cell_value(i, 1)
                self.qun_num = int(str(sheet.cell_value(i, 2)).split('.')[0])
                self.send_times = int(str(sheet.cell_value(i, 3)).split('.')[0])
                self.click_zimu = int(str(sheet.cell_value(i, 4)).split('.')[0])
                self.line = i #保存当前操作的行数

                #读取字符串转成json
                self.data_json = json.loads(sheet.cell_value(i, 5))

                if int(self.data_json[str(self.click_zimu)]) == 0 and self.click_zimu != 26:
                    self.click_zimu += 1
                    work_book_new = copy(work_book)
                    work_book_new_sheet = work_book_new.get_sheet(0)
                    work_book_new_sheet.write(i, 4, self.click_zimu)
                    work_book_new.save(self.file_name)
                    self.get_nameandnum()
                elif int(self.data_json[str(self.click_zimu)]) == 0 and self.click_zimu == 26:
                    work_book_new = copy(work_book)
                    work_book_new_sheet = work_book_new.get_sheet(0)
                    work_book_new_sheet.write(i, 0, 'no')
                    work_book_new_sheet.write(i + 1, 0, 'yes')
                    work_book_new.save(self.file_name)
                    self.get_nameandnum()
                else:
                    pass

            else:
                pass
        if self.send_times >= self.qun_num:
            self.change_to_false()
            self.get_nameandnum()
        else:
            pass

    #点击对应的字母, character_index传入0
    def click_letter(self, character_index):
        x = 694
        y = 289
        dur = 34
        click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, x, y + dur*character_index)
        os.popen(click_cmd)
        click_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, x, y + dur*character_index)
        os.popen(click_cmd)
        time.sleep(1.0)

    #判断坦白说是否存在
    def speak_isexists_and_click_qunname(self):
        #print(sys._getframe().f_code.co_name)
        try:
            self.driver.find_element_by_name('联系人').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('群聊'))
            self.driver.find_element_by_name('群聊').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_id('com.tencent.mobileqq:id/text1'))

            # 点击群聊文案
            self.driver.find_element_by_name('群聊').click()
            time.sleep(1.0)

            #判断群名称是否是str类型
            if type(self.qun_name) is not str:
                self.qun_name = str(self.qun_name)
            else:
                pass

            '''
                        if self.qun_name not in self.driver.page_source:
                cmd_swipe = 'adb -s %s shell input swipe 360 800 360 700 500'%self.udid
                os.popen(cmd_swipe)
                time.sleep(1.0)
            else:
                pass
            '''

            # 判断群昵称是否存在页面，不存在滑动屏幕
            while self.qun_name not in self.driver.page_source:
                cmd_swipe = 'adb -s %s shell input swipe 360 800 360 350 500'%self.udid
                os.popen(cmd_swipe)
                time.sleep(2.0)
            else:
                self.driver.find_element_by_name(self.qun_name).click()

            # 进入群成员列表页面
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightImage'))
            self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightImage').click()
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('群聊成员'))
            self.driver.find_element_by_name('群聊成员').click()
            WebDriverWait(self.driver, self.qun_list_wait_time).until(lambda x: x.find_element_by_name('搜索'))
        except Exception as e:
            #print('speak_isexists_and_click_qunname异常信息: %s' % e)
            #print(traceback.print_exc())
            self.exce_method()

    #判断成员列表页面点击成员是否有效
    def click_ok_by_id(self):
        #print(sys._getframe().f_code.co_name)
        try:
            self.driver.find_element_by_id(self.qun_list_name_id).click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.tencent.mobileqq:id/info'))

            if '发消息' in self.driver.page_source:
                pass
            elif '编辑资料' in self.driver.page_source:
                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                time.sleep(1.0)
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('群聊成员'))
                self.driver.swipe(360, 602, 360, 602 - self.swipeDur, 300)
                time.sleep(0.3)
                self.click_ok_by_id()
        except Exception as e:
            #print('click_ok_by_id异常信息: %s' % e)
            self.exce_method()

    #发送消息
    def send_new(self):
        #print(sys._getframe().f_code.co_name)
        try:
            self.driver.find_element_by_name('发消息').click()
            WebDriverWait(self.driver, self.wait_time).until(
                lambda x: x.find_element_by_id('com.tencent.mobileqq:id/input'))

            # 判断是否发送过消息
            if self.message_content in self.driver.page_source:
                self.send_times += 1
                self.write_to_file() #写入文件
                self.change_to_false()
                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('联系人'))
            else:
                self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(self.message_content_url)
                time.sleep(0.5)
                self.driver.find_element_by_name('发送').click()
                time.sleep(0.5)
                self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(self.message_content)
                time.sleep(0.5)
                self.driver.find_element_by_name('发送').click()
                time.sleep(0.5)
                #self.send_picture()      #调用发图片方法
                self.send_times += 1
                self.write_to_file()  # 写入文件
                self.change_to_false()  # 发送次数大于群人数，修改文件
                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('联系人'))

            self.loop_step()
        except Exception as e:
            #print('click_ok_by_id异常信息：%s'%e)
            self.exce_method()

    #发送次数写入文件
    def write_to_file(self):
        workbook = xlrd.open_workbook(self.file_name)
        workbook_new = copy(workbook)
        ws = workbook_new.get_sheet(0)

        if self.send_times >= int(self.data_json[str(self.click_zimu)]):
            self.click_zimu += 1
            ws.write(self.line, 3, 0)
            ws.write(self.line, 4, self.click_zimu)
            workbook_new.save(self.file_name)
        else:
            ws.write(self.line, 3, self.send_times)
            workbook_new.save(self.file_name)

        self.change_to_false()

    #群成员界面
    def swipe_qunchengyuan(self, times):
        #print(sys._getframe().f_code.co_name)
        self.click_letter(self.click_zimu)
        if times >= 1:
            try:
                self.get_nameandnum()
                self.click_letter(self.click_zimu)
                time.sleep(1.0)

                first = int(self.send_times / 9)
                second = int(self.send_times % 9)

                for i in range(0, first):
                    self.driver.swipe(360, 1180, 360, 1180 - self.swipeDur * 9, 1000)
                    time.sleep(0.3)

                for j in range(0, second):
                    self.driver.swipe(360, 602, 360, 602 - self.swipeDur, 300)
                    time.sleep(0.3)
            except Exception as e:
                #print('swipe_qunchengyuan异常信息：%s' %e)
                self.exce_method()
        else:
            pass

    #异常处理方法
    def exce_method(self):
        #print(sys._getframe().f_code.co_name)
        if '消息' in self.driver.page_source and '看点' in self.driver.page_source and '动态' in self.driver.page_source:
            self.loop_step()
        elif '我的群名片' in self.driver.page_source:
            self.driver.find_element_by_name('群聊成员').click()
            WebDriverWait(self.driver, self.qun_list_wait_time).until(lambda x:x.find_element_by_name('搜索'))
            self.swipe_qunchengyuan(self.send_times)
            self.click_ok_by_id()
            self.send_new()
            self.loop_step()
        elif '群聊成员' in self.driver.page_source and '默认排序' in self.driver.page_source:
            self.swipe_qunchengyuan(self.send_times)
            self.click_ok_by_id()
            self.send_new()
            self.loop_step()
        elif '发消息' in self.driver.page_source:
            self.send_new()
            self.loop_step()
        elif self.is_exists_element_by_id('com.tencent.mobileqq:id/input') and '屏蔽此人' in self.driver.page_source and '加为好友' in self.driver.page_source and '原图' not in self.driver.page_source:
            # 判断是否发送过消息
            if self.message_content in self.driver.page_source:
                self.send_times += 1
                self.write_to_file()  # 写入文件
                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('联系人'))
            else:
                self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(self.message_content)
                time.sleep(0.5)
                self.driver.find_element_by_name('发送').click()
                time.sleep(1.5)
                self.send_times += 1
                self.write_to_file()  # 写入文件
                self.change_to_false()  # 发送次数大于群人数，修改文件
                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('联系人'))

            self.loop_step()
        elif '原图' in self.driver.page_source and '相册' in self.driver.page_source and '编辑' in self.driver.page_source:
            back_cmd1 = 'adb -s %s shell input keyevent 4'%self.udid
            os.popen(back_cmd1)
            time.sleep(1.0)
            back_cmd2 = 'adb -s %s shell input keyevent 4'%self.udid
            os.popen(back_cmd2)
            WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element_by_name('联系人'))
            self.loop_step()

        elif self.is_exists_element_by_id('com.tencent.mobileqq:id/input'):
            back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
            os.popen(back_cmd)
            time.sleep(1.0)
            self.loop_step()
        else:
            try:
                stop_cmd = 'adb -s %s shell am force-stop com.tencent.mobileqq'%self.udid
                os.popen(stop_cmd)
                time.sleep(3.0)
                start_cmd = 'adb -s %s shell am start com.tencent.mobileqq/.activity.SplashActivity'%self.udid
                os.popen(start_cmd)
                WebDriverWait(self.driver, self.launch_time).until(lambda x:x.find_element_by_name('联系人'))
                self.loop_step()
            except Exception as e:
                #print('exce_method异常信息：%s'%e)
                self.exce_method()
    #根据控件id判断是否存在某元素
    def is_exists_element_by_id(self, ele_id):
        try:
            self.driver.find_element_by_id(ele_id)
            return True
        except Exception as e:
            return False

    #初始化driver失败，多次重试
    def repet_get_driver(self):
        if self.temp_num >= 4:
           pass
        else:
            self.temp_num += 1
            try:
                qm.get_driver()
            except Exception as e:
                #kill_adb_cmd = 'taskkill /f /im adb.exe'
                #os.popen(kill_adb_cmd)
                #time.sleep(0.5)
                #start_cmd = 'adb devices'
                #os.popen(start_cmd)
                #time.sleep(1.0)
                self.repet_get_driver()

    #发送图片
    def send_picture(self):
        #判断发送的消息类型
        if '支付宝' in self.message_content:
            pass
        elif '视频' in self.message_content:
            try:
                x = 135
                y = 1164
                cmd1 = 'adb -s %s shell input tap %d %d'%(self.udid, x, y)
                os.popen(cmd1)
                time.sleep(1.0)

                if '相册' in self.driver.page_source:
                    pass
                else:
                    time.sleep(1.0)
                    if '相册' in self.driver.page_source:
                        pass
                    else:
                        x = 135
                        y = 1164
                        cmd1 = 'adb -s %s shell input tap %d %d' % (self.udid, x, y)
                        os.popen(cmd1)
                        time.sleep(1.0)

                #发送第一张图片
                x1 = 75
                y1 = 958
                cmd_pic1 = 'adb -s %s shell input tap %d %d' % (self.udid, x1, y1)
                os.popen(cmd_pic1)
                time.sleep(1.0)
                if '发送(1)' in self.driver.page_source:
                    pass
                else:
                    time.sleep(1.0)
                    if '发送(1)' in self.driver.page_source:
                        pass
                    else:
                        cmd_pic1 = 'adb -s %s shell input tap %d %d' % (self.udid, x1, y1)
                        os.popen(cmd_pic1)
                        time.sleep(1.0)

                # 发送第二张图片
                x2 = 225
                y2 = 958
                cmd_pic2 = 'adb -s %s shell input tap %d %d' % (self.udid, x2, y2)
                os.popen(cmd_pic2)
                time.sleep(1.0)
                if '发送(2)' in self.driver.page_source:
                    pass
                else:
                    time.sleep(1.0)
                    if '发送(2)' in self.driver.page_source:
                        pass
                    else:
                        cmd_pic2 = 'adb -s %s shell input tap %d %d' % (self.udid, x2, y2)
                        os.popen(cmd_pic2)
                        time.sleep(1.0)

                #发送第三张图片
                x3 = 375
                y3 = 958
                cmd_pic3 = 'adb -s %s shell input tap %d %d' % (self.udid, x3, y3)
                os.popen(cmd_pic3)
                time.sleep(1.0)
                if '发送(3)' in self.driver.page_source:
                    pass
                else:
                    time.sleep(1.0)
                    if '发送(3)' in self.driver.page_source:
                        pass
                    else:
                        cmd_pic3 = 'adb -s %s shell input tap %d %d' % (self.udid, x3, y3)
                        os.popen(cmd_pic3)
                        time.sleep(1.0)

                self.driver.find_element_by_name('发送(3)').click()
                time.sleep(0.5)

                self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(self.haha_content)
                time.sleep(0.5)
                self.driver.find_element_by_name('发送').click()
                time.sleep(1.0)

                back_cmd = 'adb -s %s shell input keyevent 4'%self.udid
                os.popen(back_cmd)
                time.sleep(0.5)

            except Exception as e:
                self.exce_method()
        else:
            pass

    #优先在线排序
    def send_by_sort_online(self):
        self.driver.find_element_by_accessibility_id('切换排序方式').click()
        WebDriverWait(self.driver, self.wait_time).until(lambda x:x.find_element_by_name('优先在线成员'))
        self.driver.find_element_by_name('优先在线成员').click()
        pass


if __name__ == '__main__':

    qm = QunMessage()

    os.popen('adb -s %s shell settings put system screen_brightness_mode 0'%qm.udid)
    time.sleep(1.0)
    os.popen('adb -s %s shell settings put system screen_brightness 1'%qm.udid)
    time.sleep(1.0)
    #qm.repet_get_driver()
    try:
        qm.get_driver()
        qm.loop_step()
    except Exception as e:
        qm.exce_method()