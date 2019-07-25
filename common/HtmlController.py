#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import time
import config as cfg
from common.logger import logger


class HtmlController(object):
	def __init__(self):
		self.path = cfg.RESULT_PATH
		self.is_success = 'Success! '
		self.start_time = time.time()
		date_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(self.start_time))
		test_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time))
		today = date_time.split('_')[0]
		self.html = cfg.HTML
		self.name = '{}_{}'.format(cfg.HEADER, date_time)
		self.title = cfg.TITLE.format('{}_{}'.format(cfg.HEADER, today))
		self.test_time = cfg.TEST_TIME.format(test_time)
		self.overview = cfg.H3.format('概览')
		self.overview1 = cfg.OVERVIEW1 + cfg.OVERVIEW2
		self.fail1 = cfg.H3.format('失败详情' + cfg.SPAN)
		self.fail2 = cfg.H3.format(cfg.SPAN)
		self.success = cfg.H3.format('测试结果详情')
		self.table = cfg.TABLE
		self.table_head = cfg.TABLE_HEAD
		self.tr = cfg.TR
		self.td = cfg.TD
		self.td_fail = cfg.TD_FAIL
		self.td_success = cfg.TD_SUCCESS
		self.bg_color = cfg.BG_COLOR
		self.last = cfg.LAST
		self.fail_step = []

		self._all_step = []
		self._scene_num = 0
		self._case_num = 0
		self._case_fail = 0

	@property
	def scene_num(self):
		return self._scene_num

	@scene_num.setter
	def scene_num(self, value):
		self._scene_num += value

	@property
	def case_num(self):
		return self._case_num

	@case_num.setter
	def case_num(self, value):
		self._case_num += value

	@property
	def case_fail(self):
		return self._case_fail

	@case_fail.setter
	def case_fail(self, value):
		self._case_fail += value

	@property
	def all_step(self):
		return self._all_step

	@all_step.setter
	def all_step(self, value):
		color = int(value['sceneId']) % 2
		caseId = self.td.format(value['caseId'])
		sceneId = self.td.format(value['sceneId'])
		caseName = self.td.format(value['caseName'])
		stepName = self.td.format(value['stepName'])
		shot_img = self.td.format(value['shotImg'])
		if value['result'] == 'Failure':
			result = self.td_fail.format(value['result'])
		else:
			result = self.td_success.format(value['result'])
		reason = self.td.format(value['reason'])
		res = self.tr.format(self.bg_color[color], '{}{}{}{}{}{}{}'.format(sceneId, caseId, caseName, stepName, result, shot_img, reason))

		if value['result'] == 'Failure':
			self.fail_step.append(res)

		self._all_step.append(res)

	def writeHtml(self):
		if len(self.fail_step) > 0:
			self.is_success = 'Failure! '

		all_step_num = len(self._all_step)
		success_rate = (1 - self.case_fail / self.case_num) * 100
		spend_time = time.time() - self.start_time

		fail_rows = ''.join(self.fail_step)
		all_rows = ''.join(self._all_step)

		fail_table = self.table.format('{}{}'.format(self.table_head, fail_rows))
		all_table = self.table.format('{}{}'.format(self.table_head, all_rows))

		detail = self.overview1.format(self.scene_num, self.case_num, all_step_num, spend_time, self.case_num-self.case_fail, self.case_fail, success_rate)
		header = '{}{}{}{}'.format(self.title, self.test_time, self.overview, detail)

		if success_rate == 100:
			fail_html = self.html.format('{}{}{}'.format(header, self.fail2, self.last))
		else:
			fail_html = self.html.format('{}{}{}{}'.format(header, self.fail1, fail_table, self.last))
		all_html = self.html.format('{}{}{}'.format(header, self.success, all_table))

		html_path = os.path.join(self.path, self.name + '.html')
		with open(html_path, 'w') as f:
			f.writelines(all_html)

		logger.logger.info('测试结果保存成功。')
		return fail_html, self.name

	def __del__(self):
		pass
