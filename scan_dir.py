#!/usr/bin/python
import os
u = open('users.txt','r')
for user in u.readlines():
  user = user.replace("\n","")
  path = '/data/users/'+ user + '/'
  tmp = os.path.isdir(path)
  if tmp == True:
    print "True",path
    dir = open('dirs.txt','r')
    for dir in dir.readlines():
      dir = dir.replace("\n","")
      path2=path + dir
      tmp2=os.path.isdir(path2)
      if tmp2 == True:
        print "True", path2