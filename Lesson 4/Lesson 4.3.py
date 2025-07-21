import random

lst_length = random.randint(3,10)

random_lst = [random.randint(1,10) for i in range(lst_length)]

print(random_lst)

if lst_length >= 3:
    new_list = [random_lst[0], random_lst[2], random_lst[-2]]
    print(new_list)
