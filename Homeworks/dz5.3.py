import string

text = input("Введіть рядок: ")

# Видаляю знаки пунктуації та пробіли
for char in string.punctuation:
    text = text.replace(char, "")

# Розбираю текст на слова
words = text.split()

# Роблю кожне слово з великої літери
words = [word.capitalize() for word in words]

# Об'єдную слова та додаю #
hashtag = "#" + "".join(words)

# Якщо довжина більше 140, обрізаю
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Завдання виконав :)
print(hashtag)
