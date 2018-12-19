# -*- coding:utf-8 -*-

class InitPara(object):

    desired_caps = None

    def set_desired_caps(self, udid, package, activity):
        self.desired_caps = {'platformName': 'Android',
                             'platformVersion': '8.1.0',
                             'deviceName': 'vivo',
                             'udid': udid,
                             'appPackage': package,
                             'appActivity': activity,
                             'unicodeKeyboard': True,
                             'resetKeyboard': True,
                             'noReset': True
                             }

    def get_desired_caps(self):
        return self.desired_caps