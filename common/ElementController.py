#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import config as cfg


class ElementExistException(Exception):
	pass


class Element(object):
	def __init__(self, driver):
		self.driver = driver
		self.time_out = cfg.ELEMENT_TIMEOUT
		self.save_to = cfg.SAVE_SHOT
		self.shot_path = cfg.SHOT_PATH
		self.shot_img = ''

		if not os.path.exists(self.shot_path):
			os.mkdir(self.shot_path)

	def get_title(self):
		return self.driver.title

	def open_web(self, url):
		self.driver.get(url)
		self.save_screenshot()

	def open_new_web(self, url):
		js = 'window.open("{}");'.format(url)
		self.execute_js(js)
		self.save_screenshot()

	def find_ele_by_id(self, ele, timeout=None):
		"""
			通过id定位元素
		"""
		if not timeout:
			timeout = self.time_out
		try:
			WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, ele)))
			return self.driver.find_element_by_id(ele)
		except Exception as err:
			raise Exception('selenium.common.exceptions.TimeoutException')

	def find_ele_by_xpath(self, ele, timeout=None):
		"""
			通过xpath定位元素
		"""
		if not timeout:
			timeout = self.time_out
		try:
			WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, ele)))
			return self.driver.find_element_by_xpath(ele)
		except Exception as err:
			raise Exception('selenium.common.exceptions.TimeoutException')

	def find_eles_by_xpath(self, ele, timeout=None):
		"""
			通过xpath定位多个元素
		"""
		if not timeout:
			timeout = self.time_out
		try:
			WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, ele)))
			return self.driver.find_elements_by_xpath(ele)
		except Exception as err:
			raise Exception('selenium.common.exceptions.TimeoutException')

	def save_screenshot(self):
		"""
			保存浏览器截图
		"""
		current_time = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
		pic_path = os.path.join(self.shot_path, '{}.png'.format(current_time))
		self.shot_img = pic_path
		self.driver.save_screenshot(pic_path)

	def execute_js(self, js_command):
		"""
			执行js命令
		"""
		return self.driver.execute_script(js_command)

	def actionahains(self):
		"""
			实例化鼠标对象
		"""
		return ActionChains(self.driver)

	def __del__(self):
		pass


class ElementController(Element):
	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	def click(self, ele, pattern='xpath'):
		try:
			if pattern == 'id':
				self.find_ele_by_id(ele).click()
			if pattern == 'xpath':
				self.find_ele_by_xpath(ele).click()

			self.save_screenshot()
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def double_click(self, ele, pattern='xpath'):
		try:
			if pattern == 'id':
				self.actionahains().double_click(self.find_ele_by_id(ele)).perform()
			if pattern == 'xpath':
				self.actionahains().double_click(self.find_ele_by_xpath(ele)).perform()

			self.save_screenshot()
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def input(self, ele, text, pattern='xpath'):
		try:
			if pattern == 'id':
				self.find_ele_by_id(ele).send_keys(text)
			if pattern == 'xpath':
				self.find_ele_by_xpath(ele).send_keys(text)

			self.save_screenshot()
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def clear(self, ele, pattern='xpath'):
		try:
			if pattern == 'id':
				self.find_ele_by_id(ele).clear()
			if pattern == 'xpath':
				self.find_ele_by_xpath(ele).clear()

			self.save_screenshot()
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def element_is_display(self, ele, pattern='xpath'):
		"""
			元素是否显示
		"""
		try:
			if pattern == 'id':
				is_display = self.find_ele_by_id(ele).is_displayed()
			if pattern == 'xpath':
				is_display = self.find_ele_by_xpath(ele).is_displayed()

			self.save_screenshot()
			if is_display:
				return True
			else:
				return False
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def element_is_enabled(self, ele, pattern='xpath'):
		"""
			元素是否使能
		"""
		try:
			if pattern == 'id':
				is_enabled = self.find_ele_by_id(ele).is_enabled()
			if pattern == 'xpath':
				is_enabled = self.find_ele_by_xpath(ele).is_enabled()

			self.save_screenshot()
			if is_enabled:
				return True
			else:
				return False
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def element_is_selected(self, ele, pattern='xpath'):
		"""
			元素是否选中
		"""
		try:
			if pattern == 'id':
				is_selected = self.find_ele_by_id(ele).is_selected()
			if pattern == 'xpath':
				is_selected = self.find_ele_by_xpath(ele).is_selected()

			self.save_screenshot()
			if is_selected:
				return True
			else:
				return False
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def elements_of_num(self, ele, pattern='xpath'):
		"""
			获取元素的数量
		"""
		try:
			if pattern == 'xpath':
				elements = self.find_eles_by_xpath(ele)

			self.save_screenshot()
			return len(elements)
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def element_of_attribute(self, ele, attribute, pattern='xpath'):
		"""
			获取元素属性值
		"""
		try:
			if pattern == 'xpath':
				value = self.find_ele_by_xpath(ele).get_attribute(attribute)
			if pattern == 'id':
				value = self.find_ele_by_id(ele).get_attribute(attribute)

			self.save_screenshot()
			return value
		except Exception as err:
			self.save_screenshot()
			raise Exception(err)

	def execute_script(self, js_command):
		"""
			执行js命令
		"""
		try:
			res = self.execute_js(js_command)
			self.save_screenshot()
			return res
		except Exception as err:
			raise Exception(err)

	def get_cookie(self):
		pass
