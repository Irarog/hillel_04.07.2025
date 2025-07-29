number_input = int(input("Enter any number: "))

def calculation(number):
   while number > 9:
       index = 0
       for digit in str(number):
           index += int(digit)
           number = index
       return number

result = calculation(number_input)
print(result)