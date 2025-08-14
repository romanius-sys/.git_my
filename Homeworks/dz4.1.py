# Всі нулі переміщуємо в кінець списку

my_list = [0, 1, 0, 12, 3, 66, 0, 4]

more_zero = []

zero_count = 0
for num in my_list:
    if num != 0:
        more_zero.append(num)
    else:
        zero_count += 1

more_zero += [0] * zero_count

my_list = more_zero

print(my_list)