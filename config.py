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
# 测试用例路径
TESTCASE_PATH = os.path.join(os.path.dirname(__file__), 'testCase', 'UI_test.xlsx')
# 等待元素出现时间，单位秒，直到超时抛出异常
ELEMENT_TIMEOUT = 10
# 场景执行的超时时间，单位秒，达到设置时间，场景未执行完，则抛出异常
SCENE_TIMEOUT = 300
