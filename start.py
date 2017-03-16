import os
import sys
import translate as ts

to_translate = sys.argv[1]
translated = sys.argv[2]

dir = str(to_translate)
output_dir = str(translated)

srt_files = []
for filename in os.listdir(dir):
    srt_files.append(filename)

print srt_files

for file in srt_files:
    ts.translate(file,dir,output_dir)
