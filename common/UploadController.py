#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

from fdfs_client.client import *
from common.logger import logger
import config as cfg


class FDFS(object):
	def __init__(self):
		self.client_path = cfg.CLIENT_PATH
		self.client = Fdfs_client(get_tracker_conf(self.client_path))

	def upload_file(self, file_path):
		try:
			res = self.client.upload_by_file(file_path)
			logger.logger.info(res)
			if res['Status'] == 'Upload successed.':
				return res['Remote file_id'].decode()
			else:
				logger.logger.error(res['Status'])
				return None
		except Exception as err:
			logger.logger.error(err)
			return None

	def __del__(self):
		pass
