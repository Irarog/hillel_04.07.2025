#task 2.2
user_input = int(input("Enter 5-digit number: ")) #12345
number_one = (user_input // 1 % 10)
number_two = (user_input // 10 % 10)
number_three = (user_input // 100 % 10)
number_four = (user_input // 1000 % 10)
number_five = (user_input // 10000 % 10)
print(int(number_one), int(number_two),  int(number_three),  int(number_four), int(number_five))