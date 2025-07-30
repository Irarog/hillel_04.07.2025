import string

text_input = input("Enter text for a hashtag: ")

punctuation_symbols = string.punctuation
words = text_input.split()
hashtag = "".join(word.capitalize() for word in words)

for symbol in punctuation_symbols:
    hashtag = hashtag.replace(symbol, "")

if len(hashtag) >=140:
    print("#" +  hashtag[:140])
else:
    print("#" + hashtag)