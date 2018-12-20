# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

class Locators(object):

    MAIN_PAGE_DYNAMIC = (By.NAME, '动态') #首页动态
    MAIN_PAGE_NEWS = (By.NAME, '消息')  # 首页消息
    MAIN_PAGE_ME = (By.NAME, '我')  # 首页我
    MAIN_PAGE_VIDEO = (By.NAME, '小视频')  # 首页小视频

    SAY = (By.NAME, '说点什么...')

    USER_ID = (By.ID, 'com.qzone:id/avatar') #用户头像id
    USER_COMMENT = (By.ID, 'com.qzone:id/video_comment') #用户评论
    ADD_TEXT = (By.NAME, '加为好友') #加为好友文本
    APPLY = (By.NAME, '申请访问')
    ADD_TEXT_1 = (By.NAME, '加为好友')

    VERFICATION = (By.NAME, '请输入验证信息')
    SUBMIT = (By.NAME, '提交')
    ANSWER = (By.NAME, '回答问题')
    MASTER_ANSWER = (By.NAME, '主人设置了权限，答对问题后可访问')

    QINMI = (By.NAME, '亲密度')