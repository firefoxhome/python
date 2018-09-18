#coding=utf-8

import os
import time

ret = os.fork()
if ret == 0:
	while Ture:
		print("-----1----")
		time.sleep(1)

else:
	while Ture:
		print("----2----")
		time.sleep(1)

		