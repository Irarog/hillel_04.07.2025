number = int(input("Enter any number: "))
while number > 9:
    result = 1
    for digit in str(number):
        result *= int(digit)
    number = result
print(number)