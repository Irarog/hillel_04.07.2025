number_1 = int(input("Enter the first number: "))
math_action = str(input("Enter math action: "))
number_2 = int(input("Enter the second number: "))

if math_action == "+":
    print(number_1 + number_2)
elif math_action == "-":
    print(number_1 - number_2)
elif math_action == "*":
    print(number_1 * number_2)
elif math_action == "/" and number_2 != 0:
    print(number_1 / number_2)
else:
    print("Something went wrong!")