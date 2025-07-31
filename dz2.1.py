input_number = int(input('ВВЕДІТЬ ЧОТИРИЗНАЧНЕ ЦІЛЕ ЧИСЛО: '))

n1, n2 = divmod (input_number, 1000)
n2 = n2 // 100
n3, n4 = divmod (input_number % 100, 10)

print(n1)
print(n2)
print(n3)
print(n4)