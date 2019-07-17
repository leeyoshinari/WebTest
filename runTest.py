#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

from selenium import webdriver

driver = webdriver.Chrome()

driver.find_element_by_xpath().is_displayed()