# Expt. No: 2
# Develop a Part-of-Speech (POS) Tagging System using NLTK
# and evaluate its accuracy on a corpus of news articles.
# Date: __________

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Get input from user
text = input("Enter a sentence: ")

# Tokenize the sentence
tokens = word_tokenize(text)

# Perform POS tagging
tagged_words = pos_tag(tokens)

# Display tokens
print("\nTokens:")
print(tokens)

# Display POS tags
print("\nPOS Tags:")
for word, tag in tagged_words:
    print(word, "->", tag)

# Display common tag meanings
print("\nTag Meanings:")
print("NN  -> Noun")
print("VB  -> Verb")
print("JJ  -> Adjective")
print("RB  -> Adverb")
print("PRP -> Pronoun")
print("DT  -> Determiner")

# Count total words
print("\nTotal Words:", len(tokens))
