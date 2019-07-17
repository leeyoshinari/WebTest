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
# 等待元素出现时间，单位秒，直到超时抛出错误
WAIT_TIMEOUT = 10
