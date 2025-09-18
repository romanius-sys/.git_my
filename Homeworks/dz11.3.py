def is_even(number):
    """Перевірка парності без ділення"""
    return (number & 1) == 0  # перевіряємо останній біт


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print("OK")
