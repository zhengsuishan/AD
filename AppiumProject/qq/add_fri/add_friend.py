# -*-coding:utf-8-*-
# 能用adb操作尽量用adb操作
import os
import time
import random

class AddFriend(object):

    driver = None
    udid = None
    package = None
    activity = None
    wait_time = 1.5
    net_wait_time = 5.0
    send_times = None
    qun_num = []

    def read_count(self):
        file_name = 'send_count'
        file = open(file_name).readlines()
        return int(file[0])

    def write_count(self, param):
        file_name = 'send_count'
        file = open(file_name, 'w+')
        file.write(str(param))
        file.close()

    # 获取文案
    def get_text(self):
        text1 = '嗨，加个好友呀'
        text2 = '你好呀，交个朋友'
        text3 = '加个好友啦'
        text_list = [text1, text2, text3]
        size = len(text_list)
        index = random.randint(-1, size - 1)
        return text_list[index]

    def get_qun_num(self):
        num_list = ['0', '1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9']

        qun_len = random.randint(6, 11)

        for qun_changdu in range(0, qun_len - 1):
            index = random.randint(-1, len(num_list) - 1)
            self.qun_num.append(num_list[index])

        return ''.join(self.qun_num)

    def set_driver_udid_appinfo(self, driver, udid, package, activity):
        self.driver = driver
        self.udid = udid
        self.package = package
        self.activity = activity

    def adb_cmd(self, cmd, tap_x=100, tap_y=100, text='text'):
        start_cmd = 'adb -s %s shell am start %s' % (self.udid, self.activity)
        back_cmd = 'adb -s % shell input keyevent 4' % self.udid
        tap_cmd = 'adb -s %s shell input tap %d %d' % (self.udid, tap_x, tap_y)
        input_cmd = 'adb -s %s shell input text %s'%(self.udid, text)
        del_cmd = 'adb shell input keyevent 67'
        long_press = 'adb -s %s shell input swipe 360 445 360 445 1000'%self.udid
        if cmd == 'start':
            os.popen(start_cmd)
        elif cmd == 'back':
            os.popen(back_cmd)
        elif cmd == 'tap':
            os.popen(tap_cmd)
        elif cmd == 'text':
            os.popen(input_cmd)
        elif cmd == 'del':
            os.popen(del_cmd)
        elif cmd == 'long_press':
            os.popen(long_press)
        else:
            pass

    def go_add(self):
        # 读取发送次数
        self.send_times = self.read_count(AddFriend)

        if '找人:' in self.driver.page_source or '没有找到相关结果' in self.driver.page_source:
            self.adb_cmd(AddFriend, 'tap', 546, 93)  # 点击清空输入框按钮
            time.sleep(self.wait_time)
        else:
            self.adb_cmd(AddFriend, 'tap', 671, 100)  # 点击右上角+号按钮
            time.sleep(self.wait_time)
            self.adb_cmd(AddFriend, 'tap', 582, 302)  # 点击加好友/群
            time.sleep(self.wait_time)
            self.adb_cmd(AddFriend, 'tap', 360, 314)  # 点击输入框
            time.sleep(self.wait_time)
        self.adb_cmd(AddFriend, cmd='text', text=self.get_qun_num(AddFriend)) #输入号码

        self.qun_num = []

        time.sleep(self.wait_time)

        if '找人:' in self.driver.page_source:
            self.adb_cmd(AddFriend, 'tap', 360, 181)  #点击找人按钮
            time.sleep(self.net_wait_time)

            if '加好友' in self.driver.page_source and '返回' in self.driver.page_source and '更多' in self.driver.page_source:
                self.adb_cmd(AddFriend, 'tap', 360, 1228) #点击加好友按钮
                time.sleep(self.net_wait_time)

                #判断是否拒绝添加
                if '加好友' in self.driver.page_source:
                    self.adb_cmd(AddFriend, 'back')
                    time.sleep(self.wait_time)
                    self.go_add(AddFriend)
                else:
                    if '填写验证信息' in self.driver.page_source:
                        print('111111111111111111111111')

                        self.adb_cmd(AddFriend, 'text', '', '', self.get_text(AddFriend))
                        time.sleep(self.wait_time)
                        self.adb_cmd(AddFriend, 'tap', 652, 99.5)  # 点击发送按钮
                        time.sleep(self.net_wait_time)

                        # 写入文件
                        self.send_times += 1
                        self.write_count(AddFriend, self.send_times)

                        print('3333333333333333333333333')
                        self.adb_cmd(AddFriend, 'back')
                        time.sleep(self.wait_time)
                        self.go_add(AddFriend)
                    elif '输入答案' in self.driver.page_source:
                        self.adb_cmd('back')
                        time.sleep(self.wait_time)
                        self.adb_cmd('back')
                        time.sleep(self.wait_time)
                        self.go_add(AddFriend)
                    else:
                        pass

            elif '发消息' in self.driver.page_source:
                self.adb_cmd(AddFriend, 'back')
            elif '没有找到相关结果' in self.driver.page_source:
                self.go_add(AddFriend)
        else:
            self.adb_cmd(AddFriend, 'tap', 546, 93)  # 点击清空输入框按钮
            time.sleep(self.wait_time)
            self.go_add(AddFriend)

    def exce_to(self):
        pass

if __name__ == '__main__':
    for times in range(0, len(AddFriend.get_text(AddFriend))):
        AddFriend.adb_cmd(AddFriend, 'del')

