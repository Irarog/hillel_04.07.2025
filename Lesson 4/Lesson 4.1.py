lst = [0, 1, 0, 12, 3] # -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
n = 0

if len(lst) == 1:
    print(lst)
if len(lst) > 1:
    for _ in range(len(lst)):
        if lst[_] != 0:
            n += 1
            print(lst[_])
    for _ in range(len(lst)):
        if lst[_] == 0:
            n += 1
            print(lst[_])