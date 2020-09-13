#CREATING A FILE WITH CONTEXT

import os
path= "/home/ec2-user/"
os.chdir(path)
file= open("/home/ec2-user/file.txt","w")
file.write("have good day")

