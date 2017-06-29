#coding:utf-8

import pynoise
import time


th = pynoise.System(1)
th.settone(60)
th.stop = False
th.start()

time.sleep(1)
th.removes()
th.settone(61)

time.sleep(1)
th.removes()
th.settone(62)

time.sleep(1)
th.removes()
th.settone(63)

time.sleep(1)
th.removes()
th.settone(64)

time.sleep(1)
th.removes()
th.settone(65)

time.sleep(1)
th.removes()
th.settone(66)

print("adad")