#!/usr/bin/python3
import os, sys
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)
os.chdir("D:\myPython")
# 查看修改后的工作目录
retval = os.getcwd()
print ("目录修改成功 %s" % retval)
with open('test.txt','r') as f1:
    with open('f2.txt','w') as f2:
        while True:  
            line = f1.readline()
            if not line:  
                break
            if( "歌" not in line) :		
                f2.write(line)