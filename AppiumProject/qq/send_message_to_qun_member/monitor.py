import os
import time

file_name = 'data.xlsx' #文件路径
first = True

udid = 'd102deb37d13'

# 设置输入法
setting_cmd = 'adb -s %s shell ime set io.appium.android.ime/.UnicodeIME' % udid
os.popen(setting_cmd)

while True:
    if first:
        py_path = 'qun_message.py'
        go_cmd = 'python %s'%py_path
        os.popen(go_cmd)
        first = False
    else:
        time.sleep(180)
        local_time = int(time.time())
        change_time = int(os.stat(file_name).st_mtime)
        if local_time - change_time >= 180:
            py_path = 'qun_message.py'
            go_cmd = 'python %s' % py_path
            os.popen(go_cmd)
        else:
            pass

