def generate_cube_numbers(end):
    """Генератор кубів чисел від 2 до числа, поки куб <= end"""
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return
        yield cube
        n += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'Test1'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test3'

print("OK")
