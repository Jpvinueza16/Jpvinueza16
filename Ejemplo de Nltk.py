

import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# cargando datos
filename = 'archivo.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# convirtiendo en palabras
tokens = word_tokenize(text)

# Quita los catacteres
caracter = re.compile('[%s]' % re.escape(string.punctuation))

# eliminar la puntuación de cada palabra
symbols = [caracter.sub('', w) for w in tokens]

# Coloca solo valores alfavetico
words = [word for word in symbols if word.isalpha()]

# Eliminar palabras inecesarias
filter_words = set(stopwords.words('spanish'))

words = [w for w in words if not w in filter_words]

print("======================================================= Palabras ======================================================")
print(words)
print("======================================================= Palabras ======================================================")

fi = open("archivo_nuevo.txt", "wb")
for i in words:
    fi.write(i+"\n ")
fi.close()





