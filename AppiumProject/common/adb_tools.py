# -*-coding:utf-8 -*-
# 封装adb操作

import os
import xml.dom.minidom
import time

class AdbTools(object):

    get_devices_cmd = 'adb devices'
    device_name = []

    #读取当前连接的设备, len(device_name_list)==2表示没有设备连接
    def get_devices(self):
        device_name_list = os.popen('adb devices').readlines()
        if len(device_name_list) <= 2:
            raise RuntimeWarning('未检测到设备连接')
        elif len(device_name_list) >= 3:
            for index in range(1, len(device_name_list) - 1):
                device_name = device_name_list[index]
                device_name = device_name.split()[0]
                self.device_name.append(device_name)
                return self.device_name
        else:
            raise RuntimeWarning('未知错误')

    #获取界面元素
    def get_all_element(self, udid):
        cmd_xml = 'adb -s %s shell uiautomator dump' % udid
        print(os.popen(cmd_xml))
        time.sleep(5.0)

        desk = os.path.join(os.path.expanduser("~"), 'Desktop')

        pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
        os.popen(pull_cmd)
        time.sleep(1.0)

        file_path = '%s\\window_dump.xml' % desk  # xml文件路径
        DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

        string = DOMTree.toxml()
        return string


if __name__ == '__main__':
    print(AdbTools.get_all_element(AdbTools, '5761c059'))