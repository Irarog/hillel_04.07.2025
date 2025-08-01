import keyword
import string

user_name = input("Add your name here: ")
allowed_characters = set(string.ascii_letters + string.digits + "_")
upper_case_letters = set(string.ascii_uppercase)

if not user_name:
    print(False)
# elif user_name in allowed_characters and user_name.count("_") > 1:
#     print(True)
elif user_name[0].isdigit():
    print(False)
elif any(ch not in allowed_characters for ch in user_name):
    print(False)
elif any(ch in upper_case_letters for ch in user_name):
    print(False)
elif user_name.count("_") > 1 and not allowed_characters:
    print(False)
elif user_name in keyword.kwlist:
    print(False)
else:
    print(True)