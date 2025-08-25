def common_elements():
    list1 = [x for x in range(100) if x % 3 == 0]  # кратні 3
    list2 = [x for x in range(100) if x % 5 == 0]  # кратні 5
    return set(list1) & set(list2)  # майже готово


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")