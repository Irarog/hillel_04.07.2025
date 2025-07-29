import string

first_letter, last_letter = input("Enter range of letters like a-b: ").split('-')
letters = string.ascii_letters
print(letters[letters.index(first_letter):letters.index(last_letter)+1])