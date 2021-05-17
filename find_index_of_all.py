#Finds the indexes of all elements in the given list that satisfy the provided testing function.


def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]

a = find_index_of_all([1,2,3,4], lambda x: x % 2 == 1)

print(a)

