#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import re
import xlrd
import config as cfg
from common.logger import logger


class ExcelController(object):
	def __init__(self):
		self.path = cfg.TESTCASE_PATH
		self.element_timeout = cfg.ELEMENT_TIMEOUT
		self.scene_timeout = cfg.SCENE_TIMEOUT
		self.global_variables = {}
		self.objects = []
		self.testcase = []

	def readExcel(self):
		excel = xlrd.open_workbook(self.path)
		sheets = excel.sheet_names()

		table = excel.sheet_by_name('global_variables')
		for i in range(1, table.nrows):
			self.global_variables.update({table.cell_value(i, 0): table.cell_value(i, 1)})

		table = excel.sheet_by_name('objects')
		for i in range(1, table.nrows):
			self.objects.append({'id': table.cell_value(i, 0),
			                     'name': table.cell_value(i, 1),
			                     'describe': table.cell_value(i, 2),
			                     'location_way': table.cell_value(i, 3),
			                     'location': table.cell_value(i, 4)})

		table = excel.sheet_by_name('testCase')
		steps = []
		case_id = 1
		for i in range(1, table.nrows):
			if case_id != i:
				self.testcase.append({'id': table.cell_value(i, 0),
				                      'steps': steps})
				case_id = i

			steps.append({'name': table.cell_value(i, 3),
			              'location_way': self.objects[int(table.cell_value(i, 2))-1]['location_way'] if table.cell_value(i, 3) else None,
			              'location': self.objects[int(table.cell_value(i, 2))-1]['location'] if table.cell_value(i, 3) else None,
			              'method': table.cell_value(i, 5),
			              'element_timeout': int(table.cell_value(i, 6)) if table.cell_value(i, 6) else self.element_timeout,
			              'input': table.cell_value(i, 7),
			              'attribute': table.cell_value(i, 8),
			              'result': table.cell_value(i, 9),
			              'truth': table.cell_value(i, 10),
			              'expect': table.cell_value(i, 11),
			              'verify': table.cell_value(i, 12)})

		for sheet in sheets:
			table = excel.sheet_by_name(sheet)
			for i in range(1, table.nrows):
				if table.cell_value(i, 0):
					caseId = table.cell_value(i, 0).strip()

					if not int(table.cell_value(i, 2)):
						logger.logger.info('用例Id {} 不执行，已跳过'.format(caseId))
						continue

					caseName = table.cell_value(i, 1).strip()
					priority = int(table.cell_value(i, 3))
					interface = table.cell_value(i, 4).strip()
					protocol = table.cell_value(i, 5)
					method = table.cell_value(i, 6)
					data = self.compile(table.cell_value(i, 7))
					expectedResult = table.cell_value(i, 8)
					assertion = table.cell_value(i, 9).strip()

					if method == 'get' and data:
						request_data = data.split(',')
						interface = interface.format(*request_data)

					yield {'caseId': caseId,
					       'caseName': caseName,
					       'priority': priority,
					       'interface': interface,
					       'protocol': protocol,
					       'method': method,
					       'data': data,
					       'expectedResult': expectedResult,
					       'assertion': assertion}

	def compile(self, data):
		pattern = '<(.*?)>'
		res = re.findall(pattern, data)
		try:
			return res[0]
		except Exception as err:
			logger.logger.error(err)
			return None

	def __del__(self):
		pass
