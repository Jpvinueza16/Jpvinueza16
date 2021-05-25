
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
tokens = word_tokenize(text)
stop_words = set(stopwords.words('spanish'))
words = [w for w in words if not w in stop_words]
print(words)
f = open("nuevo.txt", "wb")
for i in words:
    f.write(i+" - ")
f.close()







