#Returns a list of elements that exist in both lists, after applying the provided function to each list element of both.


def intersection_by(a, b, fn):
  _b = set(map(fn,b))
  return [item for item in a if fn(item) in _b]

from math import floor

a = intersection_by([2.1,1.2], [2.3,3.4], floor)

print(a)
