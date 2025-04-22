import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

text = "Hello! Welcome to the world of Natural Language Processing. Let's explore NLTK."

sentences = sent_tokenize(text)
print("Sentences:", sentences)

words = word_tokenize(text)
print("Words:", words)
