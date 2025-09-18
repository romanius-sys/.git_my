import string

def first_word(text):
    # замінюємо всі знаки пунктуації на пробіли
    exclude = string.punctuation.replace("'", "")  # залишаємо апостроф
    for ch in exclude:
        text = text.replace(ch, " ")
    # розбиваємо рядок на слова. Повертаємо перше
    for word in text.split():
        if word:
            return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
