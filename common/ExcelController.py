#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import xlrd
import config as cfg
from common.logger import logger


class ExcelController(object):
	def __init__(self):
		self.path = cfg.TESTCASE_PATH
		self.element_timeout = cfg.ELEMENT_TIMEOUT
		# self.scene_timeout = cfg.SCENE_TIMEOUT
		self.global_variables = {}
		self.objects = []
		self.testcase = []
		self.testscene = []

		self.readExcel()

	def readExcel(self):
		excel = xlrd.open_workbook(self.path)

		table = excel.sheet_by_name('global_variables')
		for i in range(1, table.nrows):
			self.global_variables.update({table.cell_value(i, 0): table.cell_value(i, 1)})

		table = excel.sheet_by_name('objects')
		for i in range(1, table.nrows):
			self.objects.append({
				'id': table.cell_value(i, 0),
				'name': table.cell_value(i, 1),
				'describe': table.cell_value(i, 2),
				'location_way': table.cell_value(i, 3),
				'location': table.cell_value(i, 4)
			})

		table = excel.sheet_by_name('testCase')
		max_case_id = table.nrows - 1
		for i in range(max_case_id):
			self.testcase.append([])

		for i in range(1, table.nrows):
			self.testcase[int(table.cell_value(i, 0))-1].append({
				'id': table.cell_value(i, 0),
				'name': table.cell_value(i, 1),
				'step_name': table.cell_value(i, 3),
				'location_way': self.objects[int(table.cell_value(i, 2))-1]['location_way'] if table.cell_value(i, 2) else None,
				'location': self.objects[int(table.cell_value(i, 2))-1]['location'] if table.cell_value(i, 2) else None,
				'method': table.cell_value(i, 5),
				'timeout': int(table.cell_value(i, 6)) if table.cell_value(i, 6) else 0,
				'input': table.cell_value(i, 7),
				'attribute': table.cell_value(i, 8),
				'javascript': table.cell_value(i, 9),
				'result': table.cell_value(i, 10),
				'truth': table.cell_value(i, 11),
				'expected': table.cell_value(i, 12),
				'verify': table.cell_value(i, 13)
			})

		table = excel.sheet_by_name('testScene')
		for i in range(1, table.nrows):
			self.testscene.append({
				'id': table.cell_value(i, 0),
				'name': table.cell_value(i, 1),
				'describe': table.cell_value(i, 2),
				'testcase': table.cell_value(i, 3),
				'is_run': table.cell_value(i, 4),
				'timeout': table.cell_value(i, 5) if table.cell_value(i, 5) else 0
			})

	def __del__(self):
		pass
