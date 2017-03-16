# -*- coding: UTF-8 -*-
from textblob import TextBlob
import re


#====== check method ======

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
    
def translate(srt,dir,output_dir):
    try:
        # ====== extract English text and translate======
        file_name = srt
        
        # open files
        en_file = open( dir + "/" + file_name,"r")
        zh_file = open( output_dir + "/" + file_name , "w")
        
        # translate
        sentence = []
        dt = []
        count = 0
        
        while True:
            line = en_file.readline()
            if not line:
                break
            
            # write number and time axis
            if not check_contain_english(line):
                dt.append(line)
        
            # add to sentence while not contain full stop
            elif not check_contain_full_stop(line):
                sentence.append(line)
                
            # translate if sentence have a full stop
            else:
                sentence.append(line)
                en_blob = TextBlob("".join(sentence).replace('\n', " "))
                sentence = []
                return_str = en_blob.translate(to='zh')
                return_str = str(return_str)
                return_str = return_str.replace('，'," ").replace("。", "") # strip the ',' the API returned
                
                # split translation
                dt = filter(lambda s: s != '\n', dt)
                
                short_lis = return_str.split()
                sentence_count = len(dt) / 2
                if sentence_count == 0:
                    continue
                word_count = len(short_lis) / sentence_count
                
                # write to zh_file
                if sentence_count == 1:
                    zh_file.write(dt[0])
                    zh_file.write(dt[1])
                    zh_file.write(return_str)
                    zh_file.write("\n")
                    zh_file.write("\n")
                    
                if sentence_count == 2:
                     for i in range(0,len(dt),2):
                        zh_file.write(dt[i])
                        zh_file.write(dt[i+1])
                        if word_count == 1:
                            if i == 0:
                                zh_file.write(" ".join(short_lis[:1]))
                            if i == 2:
                                zh_file.write(" ".join(short_lis[1:]))
                        if word_count == 2:
                            if i == 0:
                                zh_file.write(" ".join(short_lis[:2]))
                            if i == 2:
                                zh_file.write(" ".join(short_lis[2:]))
                        zh_file.write("\n")
                        zh_file.write("\n")
                        
                if sentence_count == 3:
                    for i in range(0,len(dt),2):
                        zh_file.write(dt[i])
                        zh_file.write(dt[i+1])
                        if word_count == 1:
                            if i == 0:
                                zh_file.write(" ".join(short_lis[:1]))
                            if i == 2:
                                zh_file.write(" ".join(short_lis[1:2]))
                            if i == 4:
                                zh_file.write(" ".join(short_lis[2:]))
                        if word_count == 2:
                            if i == 0:
                                zh_file.write(" ".join(short_lis[:2]))
                            if i == 2:
                                zh_file.write(" ".join(short_lis[2:4]))
                            if i == 4:
                                zh_file.write(" ".join(short_lis[4:]))
                        zh_file.write("\n")
                        zh_file.write("\n")
                dt = []
    except:
        f = open("error.txt","a")
        f.write("script crashed with " + str(srt) + '\n')
    else:
        # close files
        en_file.close()
        zh_file.close()
    
    # print
    print str(srt) + " translated"
        