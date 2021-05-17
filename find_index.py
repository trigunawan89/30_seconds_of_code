#Finds the index of the first element in the given list that satisfies the provided testing function.



def find_index(lst, fn):
  return next(i for i, x in  enumerate(lst) if fn(x))

a = find_index([1,2,3,4,50], lambda x: x % 2 == 0)


print(a)

