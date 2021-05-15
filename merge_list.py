from itertools import zip_longest

lst = zip(['a', 'b'], [1, 2], [True, False]) 
print(list(lst))

lst = zip_longest(['a'], [1, 2], [True, False])
print(list(lst))