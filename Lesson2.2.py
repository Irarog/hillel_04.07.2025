#task 2.2
user_input = int(input("Enter 5-digit number: ")) #12345
number_one = (user_input // 1 % 10) #5
number_two = (user_input // 10 % 10) #4
number_three = (user_input // 100 % 10) #3
number_four = (user_input // 1000 % 10) #2
number_five = (user_input // 10000 % 10) #1
print(number_one * 10000 + number_two * 1000 + number_three * 100 + number_four * 10 + number_five)