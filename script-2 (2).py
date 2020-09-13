#deleting context of file

import os
path= "/home/ec2-user/foldery1"
os.chdir(path)
file= open("/home/ec2-user/foldery1/filexxx.txt","w")
file.close()
