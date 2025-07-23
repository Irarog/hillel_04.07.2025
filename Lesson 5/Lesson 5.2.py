while True:
    number_1 = int(input("Enter the first number: "))
    math_action = str(input("Enter math action: "))
    number_2 = int(input("Enter the second number: "))

    if math_action == "+":
        result = number_1 + number_2
    elif math_action == "-":
        result = number_1 - number_2
    elif math_action == "*":
        result = number_1 * number_2
    elif math_action == "/" and number_2 != 0:
        result = number_1 / number_2
    else:
        print("Oops! Something went wrong!")
    print(result)

    reply = input("Please type 'yes' or 'y' to continue: ").lower()
    if reply == "y" and "yes":
        continue
    else:
        print('Thank you for using calculator')
        break