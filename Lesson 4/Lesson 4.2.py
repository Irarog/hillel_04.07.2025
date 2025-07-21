lst = [0, 1, 7, 2, 4, 8] # => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

if len(lst) == 0:
    print(0)

if len(lst) >= 1:
    last_number = lst[-1]
    sum_numbers = 0

    for i in range(0, len(lst), 2):
        sum_numbers += lst[i]
    print(sum_numbers * last_number)
