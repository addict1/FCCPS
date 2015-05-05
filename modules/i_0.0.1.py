import os
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py" or fname[-3:] == ".sh" or fname[-3:] == ".pl":
            for line in open(path+"/"+fname):
                    break
            if 1 == 1:
				print (path+"/"+fname)
                #filestoinfect.append(path+"/"+fname)
    return filestoinfect
	
search("/")
#        elif fname[-3:] == ".py":