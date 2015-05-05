Default Varibles
var = 0  --  Temporary -- Number of threads being created
var1 = 16 -- Number of threads to be created
path = "/" -- Path for looking for editable files
name1 = str(randint(1,1000000000000000)) -- Name for new python file
newFile = "%s.py" % name1 -- Add ".py" extension. Room to change
dir1 = str(inspect.getfile(inspect.currentframe())) -- Currently running file
dir2 = str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) -- Currently running directory
newDirec = "%s/%s" % (dir2, newFile) -- Central