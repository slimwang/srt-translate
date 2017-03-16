from textblob import TextBlob
import re

# en_blob = TextBlob('Now as you might have discovered,these four- or')
# en_blob2 = TextBlob('five-letter symbols represent particular funds.')
# print en_blob.translate(to='zh')
# print en_blob2.translate(to='zh')

def check_contain_english(check_str):
    for en in check_str:
         if re.search('^[a-zA-Z]+$', en):
            return True
    return False

# extract English text
file_name = "en-test.srt"
with open("en-us/" + file_name,"r") as en_file:
    with open("zh-cn/" + "output.srt", "w") as zh_file:
        for line in en_file.readlines():
            if not check_contain_english(line):
                zh_file.write(line)
                print line
            else:
                en_blob = TextBlob(line)
                return_str = en_blob.translate(to='zh')
                zh_file.write(str(return_str))
                print str
        