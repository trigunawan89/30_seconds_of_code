def find_last_index(lst, fn):
  return len(lst)-1- next(i for i, x in enumerate(lst[::-1]) if fn(x))


a = find_last_index([1,2,3,4,5,], lambda x : x %2 ==0)

print(a)


