#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : leeyoshinari

import threading


class TimeOutException(Exception):
	pass


def timeoutlimit(timeout):
	def decorator(functions):
		def decorator1(*args, **kwargs):
			class Timeoutlimit(threading.Thread):
				def __init__(self):
					super(Timeoutlimit, self).__init__()
					self.result = None
					self.error = None

				def run(self):
					try:
						self.result = functions(*args, **kwargs)
					except Exception as err:
						self.error = err

			t = Timeoutlimit()
			t.setDaemon(True)
			t.start()
			t.join(timeout)

			if t.error is not None:
				return t.error

			return t.result

		return decorator1

	return decorator


if __name__ == '__main__':
	@timeoutlimit(1)
	def sleep():
		import time
		time.sleep(3)
		raise Exception('asdfg')
		# return True


	print(sleep())
	print(1)