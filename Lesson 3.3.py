lst = [1,2,3,4,5,6] #[1, 2, 3], [1, 2, 3, 4, 5], [1], []
lst_first = lst[:len(lst) // 2]
lst_second = lst[len(lst) // 2:]

if len(lst) > 1 and len(lst_first) == len(lst_second):
    print([lst_first, lst_second])
if len(lst) > 1 and len(lst_first) != len(lst_second):
    lst_first = lst[:len(lst) // 2 + 1]
    lst_second = lst[len(lst) // 2 + 1:]
    print([lst_first, lst_second])
if len(lst) <= 1:
    lst_first = lst[:len(lst)]
    lst_second = lst[len(lst):]
    print([lst_first, lst_second])
