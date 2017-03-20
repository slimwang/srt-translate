import os
import shutil

error_files = []
with open("error.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        error_files.append(line.split()[3])

if not os.path.isdir("error-file"):
    os.mkdir("error-file")
for e_file in error_files:
    try:
        src = 'zh-cn/' + e_file
        dst = 'error-file/' + e_file
        shutil.move(src,dst)
    except:
        print "No such file - " + e_file
