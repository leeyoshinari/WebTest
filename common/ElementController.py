#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import time
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import config as cfg
from common.logger import logger


class ElementExistException(Exception):
	pass


class Element(object):
	def __init__(self, driver):
		self.driver = driver
		self.timeout = cfg.WAIT_TIMEOUT
		self.shot_path = cfg.SHOT_PATH

		if not os.path.exists(self.shot_path):
			os.mkdir(self.shot_path)

	def find_ele_by_id(self, ele):
		try:
			WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.ID, ele)))
			return self.driver.find_element_by_id(ele)
		except ElementExistException as err:
			logger.logger.error(traceback.format_exc())
			raise Exception(err)

	def find_ele_by_xpath(self, ele):
		try:
			WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.XPATH, ele)))
			return self.driver.find_element_by_id(ele)
		except ElementExistException as err:
			logger.logger.error(traceback.format_exc())
			raise Exception(err)

	def save_screenshot(self):
		current_time = time.strftime('Y-%m-%d %H_%M_%S', time.localtime(time.time()))
		pic_path = os.path.join(self.shot_path, '{}.png'.format(current_time))
		self.driver.save_screenshot(pic_path)

	def __del__(self):
		pass


class ElementControl(Element):
	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	def element_is_display(self, pattern, ele):
		try:
			if pattern == 'id':
				is_display = self.find_ele_by_id(ele).is_displayed()
			if pattern == 'xpath':
				is_display = self.find_ele_by_xpath(ele).is_displayed()

			if is_display:
				return True
			else:
				return False
		except Exception as err:
			logger.logger.error(err)
			return False

