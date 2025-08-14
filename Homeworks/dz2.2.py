input_number = int(input('ВВЕДІТЬ ПЯТИЗНАЧНЕ ЦІЛЕ, ПОЗИТИВНЕ ЧИСЛО: '))

n1, n2 = divmod (input_number, 10000)
n2 = n2 // 1000
n3 = (input_number // 100) % 10
n4, n5 = divmod (input_number % 100, 10)

reversed_number = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1

print("Перевернуте число:", reversed_number)