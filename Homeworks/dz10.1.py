def pow(x):
    return x ** 2

def some_gen(begin, n, func):

    count = 0
    current = begin
    while count < n:
        yield current
        current = func(current)
        count += 1


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
