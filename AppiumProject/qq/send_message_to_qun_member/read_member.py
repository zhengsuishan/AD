# 读取每个字母对应的人数

import os
import xml.dom.minidom
import time

json_string = {0:"242", 1:"0", 2:"0", 3:"0", 4:"0", 5:"0", 6:"0", 7:"0", 8:"0", 9:"0", 10:"0",11:"0", 12:"0", 13:"0", 14:"0", 15:"0", 16:"0",17:"0", 18:"0", 19:"0", 20:"0", 21:"0", 22:"0", 23:"0", 24:"0", 25:"0", 26:"0"}

for index in range(0, 27):
    device = 'd102deb37d13'

    desk = os.path.join(os.path.expanduser("~"), 'Desktop')

    x = 694
    y = 289
    dur = 34
    click_cmd = 'adb -s %s shell input tap %d %d' % (device, x, y + dur * index)
    os.popen(click_cmd)
    click_cmd = 'adb -s %s shell input tap %d %d' % (device, x, y + dur * index)
    os.popen(click_cmd)
    time.sleep(1.0)

    #往下花一点
    swipe_cmd = 'adb -s %s shell input swipe 360 600 360 750 500'%device
    os.popen(swipe_cmd)
    time.sleep(2.0)

    cmd_xml = 'adb -s %s shell uiautomator dump' % device
    os.popen(cmd_xml)
    time.sleep(5.0)

    pull_cmd = 'adb -s %s pull /sdcard/window_dump.xml %s' % (device, desk)
    os.popen(pull_cmd)
    time.sleep(1.0)

    file_path = '%s\\window_dump.xml'%desk  # xml文件路径
    DOMTree = xml.dom.minidom.parse(file_path)  # 获取dom对象

    string = DOMTree.toxml()

    char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', '#']

    temp_char = char_list[index] + '('

    if temp_char in string:
        start = string.index(temp_char)

        string_num = string[start:start + 10].split('(')[1].split('人')[0]
        json_string[index] = string_num
    else:
        json_string[index] = '0'

print(json_string)

