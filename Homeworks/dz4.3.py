import random

# створюємо список випадкових чисел (довжина від 3 до 10)
lst = [random.randint(0, 9) for _ in range(random.randint(3, 10))]

# формуємо новий список з першого, третього і другого з кінця елементів
new_lst = [lst[0], lst[2], lst[-2]]

# вивід результату
print(lst, "==", new_lst)
