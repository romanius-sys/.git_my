def sum_even_index_mult_last(lst):
    if not lst:
        return 0
    return sum(lst[::2]) * lst[-1]

# Перевірка з прикладів
print(sum_even_index_mult_last([0, 1, 7, 2, 4, 8]))  # 88
print(sum_even_index_mult_last([1, 3, 5]))           # 30
print(sum_even_index_mult_last([6]))                 # 36
print(sum_even_index_mult_last([]))                  # 0