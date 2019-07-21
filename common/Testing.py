#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import re
import time
import traceback
from selenium import webdriver
from common.ExcelController import ExcelController
from common.ElementController import ElementController
from common.HtmlController import HtmlController
from common.EmailController import sendMsg
from common.logger import logger
import config as cfg


class Testing(object):
	def __init__(self):
		self.driver = None
		self.open_browser()

		self.is_email = cfg.IS_EMAIL

		self.excel = ExcelController()
		self.ele = ElementController(self.driver)
		self.html = HtmlController()

		self.global_variable = self.excel.global_variables
		self.local_variable = {}

	def open_browser(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		logger.logger.info('打开浏览器')

	def get_value(self, value):
		"""
			处理参数，value可以是变量名，也可以是值
			优先从局部变量里查找，然后查找全局变量，如果都不是，则说明输入的是值，需要匹配出值
		"""
		if self.local_variable.get(value):
			return self.local_variable[value]
		elif self.global_variable.get(value):
			return self.global_variable[value]
		else:
			return self.compile(value)

	@staticmethod
	def compile(data):
		pattern = '<(.*?)>'
		try:
			res = re.findall(pattern, data)
			return res[0]
		except Exception as err:
			logger.logger.error(traceback.format_exc())
			raise Exception(err)

	@staticmethod
	def verified(truth, expected, method):
		if method == 'equal':
			return str(truth) == str(expected)
		elif method == 'not equal':
			return str(truth) != str(expected)
		elif method == 'contain':
			return str(expected) in str(truth)
		elif method == 'contain reverse':
			return str(truth) in str(expected)

	def test(self):
		try:
			for scene in self.excel.testscene:  # 遍历所有场景
				logger.logger.info('开始执行场景{}，该场景需要执行用例{}'.format(scene['id'], scene['testcase']))
				if scene['is_run'] == 0:    # 场景是否执行
					logger.logger.info('场景{}不执行，已跳过'.format(scene['id']))
					continue

				self.html.scene_num = 1
				scene2case = scene['testcase'].split(',')
				for case in scene2case:    # 场景执行所需要的用例id
					self.html.case_num = 1
					steps = self.excel.testcase[int(case)-1]   # 执行用例需要的所有操作步骤
					logger.logger.info('开始执行用例{}，该用例共有{}个步骤'.format(case, len(steps)))
					for step in steps:  # 遍历操作步骤
						try:
							result = 'Success'
							reason = ''
							time.sleep(int(step['timeout']))
							logger.logger.info('开始执行“{}”'.format(step['step_name']))
							if step['method'] == 'click':
								self.ele.click(step['location'], step['location_way'])
							elif step['method'] == 'open url':
								self.ele.open_web(self.get_value(step['input']))
							elif step['method'] == 'double click':
								self.ele.double_click(step['location'], step['location_way'])
							elif step['method'] == 'input':
								self.ele.input(step['location'], self.get_value(step['input']), step['location_way'])
							elif step['method'] == 'window title':
								if step['result']:
									self.local_variable.update({step['result']: self.ele.get_title()})
							elif step['method'] == 'get attribute':
								if step['result']:
									self.local_variable.update({step['result']: self.ele.element_of_attribute(step['location'], step['attribute'], step['location_way'])})
							elif step['method'] == 'get element num':
								if step['result']:
									self.local_variable.update({step['result']: self.ele.elements_of_num(step['location'], step['location_way'])})
							elif step['method'] == 'execute java script':
								js = step['javascript']
								if step['input']:
									js = js.format(self.get_value(step['input']))
								if step['result']:
									self.local_variable.update({step['result']: self.ele.execute_script(js)})
									reason = 'JS脚本运行结果：{}'.format(self.local_variable[step['result']])
								else:
									self.ele.execute_script(js)
							elif step['method'] == 'verify':
								reason = '真实值：{}，期望值：{}，验证方式：{}'.format(self.get_value(step['truth']), self.get_value(step['expected']), step['verify'])
								if self.verified(self.get_value(step['truth']), self.get_value(step['expected']), step['verify']):
									result = 'Success'
								else:
									result = 'Fail'
									logger.logger.error('“{}”执行失败，{}'.format(step['step_name'], reason))
							elif step['method'] == 'open new window':
								self.ele.open_new_web(self.get_value(step['input']))
							elif step['method'] == 'clear':
								self.ele.clear(step['location'], step['location_way'])

							self.html.all_step = {
								'sceneId': scene['id'],
								'caseId': case,
								'caseName': step['name'],
								'stepName': step['step_name'],
								'shotImg': self.ele.shot_img,
								'result': result,
								'reason': reason
							}

						except Exception as err:
							self.html.all_step = {
								'sceneId': scene['id'],
								'caseId': case,
								'caseName': step['name'],
								'stepName': step['step_name'],
								'shotImg': self.ele.shot_img,
								'result': 'Fail',
								'reason': err
							}
							self.html.case_fail = 1
							logger.logger.error('“{}”执行失败，失败原因：{}'.format(step['step_name'], err))
							logger.logger.error(traceback.format_exc())
							break

			logger.logger.info('所有场景执行完毕！')
			fail_html, html_name = self.html.writeHtml()

			if self.is_email:
				mail_group = '{}.txt'.format(cfg.RECEIVER_NAME)
				with open(mail_group, 'r') as f:
					receiver = f.readline().strip()
				msg = {
					'subject': html_name,
					'smtp_server': cfg.SMTP_SERVER,
					'sender_name': cfg.SENDER_NAME,
					'sender_email': cfg.SENDER_EMAIL,
					'password': cfg.PASSWORD,
					'receiver_name': cfg.RECEIVER_NAME,
					'receiver_email': receiver,
					'fail_test': fail_html,
					'all_test': os.path.join(cfg.RESULT_PATH, html_name + '.html')
				}
				sendMsg(msg)

		except Exception as err:
			logger.logger.error(traceback.format_exc())

	def __del__(self):
		del self.excel
		del self.ele
		del self.html
		self.driver.quit()
		logger.logger.info('关闭浏览器')
