#READIND CONTENT OF FILE 

import os
path= "/home/ec2-user/"
os.chdir(path)
file= open("/home/ec2-user/file.txt","r")
content=file.read()
print(content)
