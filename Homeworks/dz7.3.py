def second_index(text, some_str):
    first = text.find(some_str)           # пошук першого входження
    if first == -1:                       # якщо його не знайшли
        return None
    second = text.find(some_str, first+1) # пошук другого входження
    return second if second != -1 else None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')