#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import time
import config as cfg
from common.Testing import Testing


def run():
	t = Testing()
	t.test()
	del t


def main():
	if cfg.QUERY_TYPE == 0:
		run()
	elif cfg.QUERY_TYPE == 1:
		run()
		start_time = time.time()
		while True:
			if time.time() - start_time > cfg.INTERVAL:
				start_time = time.time()
				run()
			else:
				time.sleep(30)
	else:
		run()
		set_hour = int(cfg.TIMER_SET.split(':')[0])
		set_minute = int(cfg.TIMER_SET.split(':')[1])
		while True:
			current_hour = int(time.strftime('%H', time.localtime(time.time())))
			if current_hour - set_hour == -1 or current_hour - set_hour == 23:
				time.sleep(50)
			elif current_hour - set_hour == 0:
				current_minute = int(time.strftime('%M', time.localtime(time.time())))
				if current_minute - set_minute == 0:
					run()
				else:
					time.sleep(30)
				if current_minute - set_minute > 2:
					time.sleep(36000)
			else:
				time.sleep(3000)


if __name__ == '__main__':
	main()
