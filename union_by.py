#Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [ item for item in b if fn(item) not in _a]))


from math import floor

a = union_by([2.1],[1.2,2.3], floor)

print(a)

