import random

lst_length = random.randint(3,10)

random_lst = [random.randint(1,10) for element in range(lst_length)]
print(random_lst)

new_list = [random_lst[0], random_lst[2], random_lst[-2]]
print(new_list)
