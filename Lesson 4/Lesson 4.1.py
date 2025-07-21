lst = [0, 1, 0, 12, 3] # -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

not_zero_lst = [x for x in lst if x != 0]
not_zero_lst.extend([0] * (len(lst) - len(not_zero_lst)))
print(not_zero_lst)
