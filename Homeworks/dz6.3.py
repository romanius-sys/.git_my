number = int(input("Введіть число: "))

while number > 9:  # Поки число більше 9 — перемножуємо цифри
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product

print(number) # Результат в консоль і готово)
