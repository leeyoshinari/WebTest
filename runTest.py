#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.get('https://www.cnblogs.com/feng0815/p/8334144.html')
c = driver.get_cookies()
print(c)
driver.close()