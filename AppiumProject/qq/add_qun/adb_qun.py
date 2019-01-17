#adb命令

import os
import time
import xml.dom.minidom
import time
import demjson
import json
import collections

global index
index = -1


def get_qun_num():

    global index
    file = open('qun_num')
    res = file.readlines()
    if index >= len(res):
        file.close()
        file = open('qun_num', 'w+')
        file.truncate()
        file.close()
        exit()
    else:
        index += 1
        print(res[index].strip())
        return res[index].strip()

while True:
    udid = '5761c059'

    #判断页面状态
    # 等待查询结果
    cmd_xml = 'adb -s %s shell uiautomator dump' % udid
    os.popen(cmd_xml)
    time.sleep(5.0)

    desk = os.path.join(os.path.expanduser("~"), 'Desktop')

    pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
    os.popen(pull_cmd)
    time.sleep(1.0)

    file_path = '%s\\window_dump.xml' % desk  # xml文件路径
    DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

    string = DOMTree.toxml()

    if '快捷入口' in string:
        click_1 = 'adb -s %s shell input tap %d %d'%(udid, 73, 60)
        os.popen(click_1)
        time.sleep(1.5)
        click_1 = 'adb -s %s shell input tap %d %d' % (udid, 144, 66)
        os.popen(click_1)
        time.sleep(1.5)
        click_1 = 'adb -s %s shell input tap %d %d' % (udid, 41, 28)
        os.popen(click_1)
        time.sleep(1.5)
        click_1 = 'adb -s %s shell input tap %d %d' % (udid, 540, 66)
        os.popen(click_1)
        time.sleep(1.5)
        # 清空输入框
        clear_cmd = 'adb -s %s shell input tap %d %d' % (udid, 816, 148)
        os.popen(clear_cmd)
        time.sleep(1.5)

        # 获取输入框焦点
        clear_cmd = 'adb -s %s shell input tap %d %d' % (udid, 500, 148)
        os.popen(clear_cmd)
        time.sleep(1.5)

        input = 'adb -s %s shell input text %s' % (udid, get_qun_num())
        os.popen(input)
        time.sleep(1.5)
        click = 'adb -s %s shell input tap %d %d' % (udid, 282, 297)
        os.popen(click)
        time.sleep(3.0)

        # 等待查询结果
        cmd_xml = 'adb -s %s shell uiautomator dump' % udid
        os.popen(cmd_xml)
        time.sleep(5.0)

        desk = os.path.join(os.path.expanduser("~"), 'Desktop')

        pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
        os.popen(pull_cmd)
        time.sleep(1.0)

        file_path = '%s\\window_dump.xml' % desk  # xml文件路径
        DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

        string = DOMTree.toxml()

        if '申请加群' in string:
            click_cmd = 'adb -s %s shell input tap %d %d' % (udid, 567, 1952)
            os.popen(click_cmd)
            time.sleep(3.0)

            cmd_xml = 'adb -s %s shell uiautomator dump' % udid
            os.popen(cmd_xml)
            time.sleep(5.0)

            pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
            os.popen(pull_cmd)
            time.sleep(1.0)

            file_path = '%s\\window_dump.xml' % desk  # xml文件路径
            DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

            string = DOMTree.toxml()

            if '个人介绍' in string:
                click_send = 'adb -s %s shell input tap %d %d' % (udid, 969, 166)
                os.popen(click_send)
                time.sleep(3.0)

                back_cmd = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd)
                time.sleep(1.5)
            else:
                back_cmd1 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd1)
                time.sleep(1.5)
                back_cmd2 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd2)
                time.sleep(1.5)
                back_cmd3 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd3)
                time.sleep(1.5)
        elif '没有找到相关结果' in string:
            pass
        else:
            ack_cmd34 = 'adb -s %s shell input keyevent 4' % udid
            os.popen(ack_cmd34)
            time.sleep(1.5)
    else:
        # 清空输入框
        clear_cmd = 'adb -s %s shell input tap %d %d' % (udid, 816, 148)
        os.popen(clear_cmd)
        time.sleep(1.5)

        # 获取输入框焦点
        clear_cmd = 'adb -s %s shell input tap %d %d' % (udid, 500, 148)
        os.popen(clear_cmd)
        time.sleep(1.5)

        input = 'adb -s %s shell input text %s' % (udid, get_qun_num())
        os.popen(input)
        time.sleep(1.5)
        click = 'adb -s %s shell input tap %d %d' % (udid, 282, 297)
        os.popen(click)
        time.sleep(3.0)

        # 等待查询结果
        cmd_xml = 'adb -s %s shell uiautomator dump' % udid
        os.popen(cmd_xml)
        time.sleep(5.0)

        desk = os.path.join(os.path.expanduser("~"), 'Desktop')

        pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
        os.popen(pull_cmd)
        time.sleep(1.0)

        file_path = '%s\\window_dump.xml' % desk  # xml文件路径
        DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

        string = DOMTree.toxml()

        if '申请加群' in string:
            click_cmd = 'adb -s %s shell input tap %d %d' % (udid, 567, 1952)
            os.popen(click_cmd)
            time.sleep(3.0)

            cmd_xml = 'adb -s %s shell uiautomator dump' % udid
            os.popen(cmd_xml)
            time.sleep(5.0)

            pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (udid, desk)
            os.popen(pull_cmd)
            time.sleep(1.0)

            file_path = '%s\\window_dump.xml' % desk  # xml文件路径
            DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

            string = DOMTree.toxml()

            if '个人介绍' in string:
                click_send = 'adb -s %s shell input tap %d %d' % (udid, 969, 166)
                os.popen(click_send)
                time.sleep(3.0)

                back_cmd = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd)
                time.sleep(1.5)
            else:
                back_cmd1 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd1)
                time.sleep(1.5)
                back_cmd2 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd2)
                time.sleep(1.5)
                back_cmd3 = 'adb -s %s shell input keyevent 4' % udid
                os.popen(back_cmd3)
                time.sleep(1.5)
        elif '没有找到相关结果' in string:
            pass
        else:
            ack_cmd34 = 'adb -s %s shell input keyevent 4' % udid
            os.popen(ack_cmd34)
            time.sleep(1.5)


