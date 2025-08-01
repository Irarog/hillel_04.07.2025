import keyword
import string

user_name = input("Add your name here: ")
punctuation = set(string.punctuation)
allowed_characters = set(string.ascii_letters + string.digits + "_")
upper_case_letters = set(string.ascii_uppercase)

if not user_name:
    print(False)
elif user_name[0].isdigit():
    print(False)
elif any(ch not in allowed_characters for ch in user_name):
    print(False)
elif any(ch in upper_case_letters for ch in user_name):
    print(False)
elif all(ch in punctuation for ch in user_name):
    print(False)
elif user_name.count("_") > 1 and not allowed_characters:
    print(False)
elif user_name in keyword.kwlist:
    print(False)
else:
    print(True)