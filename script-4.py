# CREATING more FOLDER

import os
path= "/home/ec2-user"
os.chdir(path)
for i in range(1,5):
    newfolder="tutorial-"+str(i)
    os.mkdir(newfolder)
