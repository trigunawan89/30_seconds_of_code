#Returns the difference between two lists, after applying the provided function to each list element of both.


def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]



from math import floor 

a = difference_by([2.1,1.2], [2.3,3.4], floor)
b = difference_by([{'x': 2}, {'x':1}], [{'x':1}], lambda v : v['x'])


print(a)
print(b)

