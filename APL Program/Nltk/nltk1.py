import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('punkt')

text = "Hello! Welcome to the world of NLTK."

tokens = word_tokenize(text)

print("Tokenized Words:", tokens)
