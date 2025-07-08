#task 2.2
user_input = int(input("Enter 5-digit number: ")) #12345
number_one = int(user_input // 1 % 10)
number_two = int(user_input // 10 % 10)
number_three = int(user_input // 100 % 10)
number_four = int(user_input // 1000 % 10)
number_five = int(user_input // 10000 % 10)
print(number_one, number_two, number_three, number_four, number_five)