# -*-coding:utf-8-*-
# 定位器

from selenium.webdriver.common.by import By

class Locators(object):

    MAIN_PAGE_NEWS = (By.NAME, '消息')
    MAIN_PAGE_CONTACTS = (By.NAME, '联系人')
    MAIN_PAGE_LOOK = (By.NAME, '看点')
    MAIN_PAGE_DYNAMIC = (By.NAME, '动态')

    ADD_RIGHT = (By.ID, '快捷入口') #首页右上角+号按钮
    ADD_FRI_QUN = (By.NAME, '加好友/群') #加好友/群按钮

    FIND_QUN = (By.NAME, '找群')
    QQ_PHONE_PUBLIC = (By.NAME, 'QQ号/手机号/群/公众号')
    FIND_QUN_NUM = (By.NAME, '找群:')

    NOT_QUN = (By.NAME, '没有找到相关结果')
    SEARCH_ID = (By.ID, 'com.tencent.mobileqq:id/et_search_keyword') #搜索框id
    CLEAR = (By.ID, 'com.tencent.mobileqq:id/ib_clear_text') #清空输入框按钮