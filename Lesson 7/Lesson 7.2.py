def correct_sentence(text:str) -> str:
    text = str(input("Add your text: "))
    text = text[0].capitalize() + text[1:]
    last_el = text[-1]
    if last_el == ".":
        return text
    else:
        return text + "."


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
