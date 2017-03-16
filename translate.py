# -*- coding: UTF-8 -*-
from textblob import TextBlob
import re

def check_contain_english(check_str):
    for en in check_str:
         if re.search('^[a-zA-Z]+$', en):
            return True
    return False
    
def check_contain_full_stop(check_str):
    for s in check_str:
        if s == ".":
            return True
    return False
    

# ====== extract English text and translate======
file_name = "en-test.srt"

# open files
en_file = open("en-us/" + file_name,"r")
zh_file = open("zh-cn/" + "translated_" + file_name , "w")

# translate
sentence = []
next_to_sentence = []
en_position = 0
zh_position = 0
count = 0

while True:
    line = en_file.readline()
    if not line:
        break
    # write number and time axis
    if not check_contain_english(line):
        zh_file.write(line)
        count += 0.5

    # add to sentence while not contain full stop
    elif not check_contain_full_stop(line):
        # save current file position
        en_position = en_file.tell()
        zh_position = zh_file.tell()
        sentence.append(line)
        
    # translate if sentence have a full stop
    else:
        sentence.append(line)
        en_blob = TextBlob("".join(sentence).replace('\n', " "))
        sentence = []
        return_str = en_blob.translate(to='zh')
        return_str = str(return_str)
        return_str = return_str.replace('，'," ") # strip the ',' the API returned
        zh_file.write(return_str)



# close files
en_file.close()
zh_file.close()
        