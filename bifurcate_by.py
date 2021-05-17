def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]


a = bifurcate_by(['beep','boop','foo','bar'], lambda x: x[0] == 'b')


print(a)