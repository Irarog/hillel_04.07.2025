lst = [12, 3, 4, 10]
# lst = [1]
# lst =[]
# lst = [12, 3, 4, 10, 8]

if len(lst) > 1:
    last_number = lst.pop(-1)
    lst.insert(0,last_number)
    print(lst)
else:
    print(lst)