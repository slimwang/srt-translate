from textblob import TextBlob

en_blob = TextBlob('A couple of other things to mention.')
print en_blob.translate(to='zh')