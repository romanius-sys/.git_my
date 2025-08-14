# Отримуємо число секунд
seconds_total = int(input("Введіть кількість секунд: "))

# Кількість секунд у добі, годині, хвилині
seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60

# Розрахунок днів
days, remainder = divmod(seconds_total, seconds_in_day)
hours, remainder = divmod(remainder, seconds_in_hour)
minutes, seconds = divmod(remainder, seconds_in_minute)

# Функція для правильного відмінка слова "день"
def day_word(n):
    if 11 <= n % 100 <= 14:
        return "днів"
    elif n % 10 == 1:
        return "день"
    elif 2 <= n % 10 <= 4:
        return "дні"
    else:
        return "днів"

# Форматований вивід з нулями
print(f"{days} {day_word(days)}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
