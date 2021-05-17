def sort_dict_by_value(d, reverse=False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

a = sort_dict_by_value(d)
b = sort_dict_by_value(d, True)

print(a)
print(b)


