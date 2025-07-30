def say_hi(name_input, age_input):

    name_input = str(input("What is your name?: "))
    age_input = int(input("What is your age?: "))

    if name_input and age_input > 0:
        return f"Hi. My name is {name_input} and I'm {age_input} years old"
    else:
        return "Error"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print("ОК")