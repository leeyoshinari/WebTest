#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
# 日志级别
LOG_LEVEL = 'INFO'
# 日志路径
LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs')
# 页面截图保存路径
SHOT_PATH = os.path.join(os.path.dirname(__file__), 'result')
# 测试结果保存路径
RESULT_PATH = os.path.join(os.path.dirname(__file__), 'result')
# 测试用例路径
TESTCASE_PATH = os.path.join(os.path.dirname(__file__), 'testCase', 'UI_test.xlsx')
# 等待元素出现时间，单位秒，直到超时抛出异常
ELEMENT_TIMEOUT = 5

# 定时任务设置，0为只执行一次，1为每隔INTERVAL(单位s)执行一次，2为每天TIMER_SET执行一次
QUERY_TYPE = 0
INTERVAL = 120
TIMER_SET = '23:59:00'
# 服务重启后是否执行。如果服务重新启动，则立即执行，仅QUERY_TYPE为1或2时有效，如果QUERY_TYPE为1，INTERVAL将重新计算
# 仅支持Linux系统，需远程连接Linux
IS_START = False
LINUX_IP = '127.0.0.1'
LINUX_UAERNAME = 'root'
LINUX_PASSWORD = '123456'
SERVER_PORT = 8888

# 运行过程中的截图保存方式
# 0为保存到本地，1为保存到fastDFS，建议保存至fastDFS，这样其他人可以直接在测试报告中点击链接查看
SAVE_SHOT = 0
# fastDFS的client.conf文件路径
CLIENT_PATH = os.path.join(os.path.dirname(__file__), 'client.conf')
# fastDFS http访问地址
FDFS_URL = 'http://127.0.0.1:88/'
# fastDFS tracker地址见配置文件 client.conf
# tracker_server=127.0.0.1:22122

# 测试完成后是否自动发送邮件
# success为只有全部成功了才发送邮件，failure为只要有失败就发送邮件，both为一直发邮件，neither为都不发邮件
IS_EMAIL = 'both'
# 邮箱配置，qq邮箱为smtp.qq.com
# 所用的发件邮箱必须开启SMTP服务
SMTP_SERVER = 'smtp.sina.com'
# 发件人
SENDER_NAME = '张三'
SENDER_EMAIL = 'zhangsan@qq.com'
# 邮箱登陆密码，经过base64编码
PASSWORD = 'UjBWYVJFZE9RbFpIV1QwOVBUMDlQUT09'
# 收件人，对应 baidu_all.txt 文件，该文件为邮件组名。
RECEIVER_NAME = 'baidu_all'
# RECEIVER_EMAIL = 'baidu_all.txt'    多个收件人用英文逗号分隔


# 每行表格背景颜色
BG_COLOR = ['FFFFFF', 'E8E8E8']
# 表格模板
HEADER = 'UI自动化测试报告'
HTML = '<html><meta http-equiv="Content-Type";content="text/html";charset="utf-8"><body>{}</body></html>'
TITLE = '<h2 align="center">{}</h2>'
TEST_TIME = '<p align="right">测试时间：{}</p>'
H3 = '<h3>{}</h3>'
SPAN = '<span style="font-size:14px; font-weight:normal">&nbsp;&nbsp;&nbsp;&nbsp;所有用例测试结果见邮件附件</span>'
OVERVIEW1 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;场景总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用例总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;步骤总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行总耗时：<font color="blue">{:.2f}</font> s</p>'
OVERVIEW2 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;用例执行成功数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用例执行失败数：<font color="red">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;成功率：<font color="red">{:.2f}%</font></p>'
TABLE = '<table width="100%" border="1" cellspacing="0" cellpadding="6" align="center">{}</table>'
TABLE_HEAD = '<tr bgcolor="#99CCFF" align="center"><th width="7%">场景ID</th><th width="7%">用例ID</th><th width="20%">用例名称</th><th width="20%">步骤名称</th><th width="7%">测试结果</th><th width="9%">运行截图</th><th width="30%">失败原因/校验结果</th></tr>'
TR = '<tr bgcolor="#{}">{}</tr>'
TD = '<td>{}</td>'
TD_FAIL = '<td><font color="red">Failure</font></td>'
TD_SUCCESS = '<td><font color="blue">Success</font></td>'
LAST = '<p style="color:blue">此邮件自动发出，如有疑问，请直接回复。</p>'
SHOT_IMAGE = '<a href="{}" target="_blank">查看图片</a>'
