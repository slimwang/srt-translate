import os
import shutil
import sys

def untranslated_filter(to_translate, translated):
    # mkdir
    if not os.path.isdir("untranslated"):
        os.mkdir("untranslated")
    # filt the srt files
    count = 0
    for file in os.listdir(to_translate):
        if not file in os.listdir(translated):
            try:
                shutil.copy(to_translate +"/" + file, "untranslated")
            except:
                print "An error occured with " + file
            else:
                count += 1
                print file + " added." + "No-" + str(count)

if __name__ == '__main__':
    to_translate = sys.argv[1]
    translated = sys.argv[2]
    untranslated_filter(to_translate,translated)
