def common_elements() -> set:
    set_3 = set(el for el in range(0,100) if el % 3 == 0)
    set_5 = set(el for el in range(0,100) if el % 5 == 0)
    return set_3.intersection(set_5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())