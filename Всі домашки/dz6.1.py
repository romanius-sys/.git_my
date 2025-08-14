import string

# Отримуємо вхідні дані
start, end = input("Введіть діапазон (наприклад, a-c): ").split("-")

letters = string.ascii_letters  # abc...xyzABC...XYZ

# Знаходимо позиції початкової та кінцевої літери
start_index = letters.index(start)
end_index = letters.index(end)

# Беремо зріз і друкуємо
print(letters[start_index:end_index+1])
