import string
def is_palindrome(text_input:str) -> bool:
    text_input_join = "".join(ch for ch in text_input if ch not in string.punctuation).replace(" ", "").lower()
    text_input_reverse = text_input_join[::-1]
    if text_input_join == text_input_reverse:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
