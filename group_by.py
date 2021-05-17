from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)


from math import floor

a = group_by([6.1,4.2,6.3], floor)
b =group_by(['one','two','three'], len)

print(a)
print(b)