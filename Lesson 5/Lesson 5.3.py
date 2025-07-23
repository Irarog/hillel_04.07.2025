# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

text_input = input("Enter text for a hashtag: ")

hashtag = (text_input.title())

punctuation_symbols = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~'''

for symbol in punctuation_symbols:
    hashtag = hashtag.replace(symbol, "").replace(" ", "")

if len(hashtag) >=140:
    print("#" +  hashtag[:140])
else:
    print("#" + hashtag)