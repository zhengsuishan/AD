import os
import time

file_name = 'C:\\Users\\zss\\Desktop\\data.xls' #文件路径
first = True

while True:
    if first:
        py_path = 'E:\\pyproject\\qq\\qun_message.py'
        go_cmd = 'python %s'%py_path
        os.popen(go_cmd)
        first = False
    else:
        time.sleep(180)
        local_time = int(time.time())
        change_time = int(os.stat(file_name).st_mtime)
        print(local_time, change_time)
        if local_time - change_time >= 180:
            py_path = 'E:\\pyproject\\qq\\qun_message.py'
            go_cmd = 'python %s' % py_path
            os.popen(go_cmd)
        else:
            pass

