import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Читаємо HTML-файл
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видаляємо всі HTML-теги
    cleaned_text = re.sub(r'<.*?>', '', html)

    # Прибираємо порожні рядки
    cleaned_text = '\n'.join([line for line in cleaned_text.splitlines() if line.strip()])

    # Записуємо результат у файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

# Приклад виклику:
# delete_html_tags('draft.html')
