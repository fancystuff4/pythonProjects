# CREATING  FOLDERS IN FOLDERS

import os
path= "/home/ec2-user/"
for i in range(1,3):
    os.chdir(path)
    newfolder="foldery"+str(i)
    os.mkdir(newfolder)
    path2="/home/ec2-user/"+newfolder
    os.chdir(path2)
    for i in range(0,1):
        newfolder="folderS"+str(i)
        os.mkdir(newfolder)
