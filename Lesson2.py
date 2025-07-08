#task 2.1
user_input = int(input("Enter 4 digits number: ")) #1234

print(user_input // 1000) #1234/1000=1 answer=1
print(user_input // 100 % 10) #1234/100=12 12/10=1.2 answer=2
print(user_input // 10 % 10) #1234/10=123 123/10=12.3 answer=3
print(user_input // 1 % 10) #1234/1=1234 1234/10=123.4 answer=4