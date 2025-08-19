import string

def first_word(text: str) -> str:
        words = text.split()

        for word in words:
            cleaned_word = word.strip(string.punctuation)
            if not cleaned_word:
                continue
            if '.' in cleaned_word:
                cleaned_word = cleaned_word.split('.')[0]
            return cleaned_word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
