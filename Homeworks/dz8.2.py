import string

def is_palindrome(text):
    # літери та цифри, у нижньому регістрі
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    # перевіряємо чи рядок = своєму зворотному запису
    return cleaned == cleaned[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
