import os
import sys
import translate as ts

to_translate = sys.argv[1]
translated = sys.argv[2]

# get dir
dir = str(to_translate)
output_dir = str(translated)

# read file list
srt_files = []
finished_files = []
target_files = []
for filename in os.listdir(dir):
    srt_files.append(filename)
for filename in os.listdir(output_dir):
    finished_files.append(filename)

# filter srt fils
for s in srt_files:
   if not s in finished_files:
       target_files.append(s)
            


for file in target_files:
    ts.translate(file,dir,output_dir)
