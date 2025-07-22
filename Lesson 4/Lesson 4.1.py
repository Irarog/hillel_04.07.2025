lst = [0, 1, 0, 12, 3] # -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

if len(lst) == 0:
    print(0)

if len(lst) >= 1:

    position = 0

    for not_zero_number in lst:
        if not_zero_number != 0:
            lst[position] = not_zero_number
            position += 1
            # print(not_zero_number)

    for zero in range(position, len(lst)):
        lst[zero] = 0

    print(lst)
