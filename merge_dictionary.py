def merge_dictionary(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res


ages_one = {
  'Peter': 10,
  'Andy': 11,
}

ages_two = {
  'Ana': 9,
}

a = merge_dictionary(ages_one, ages_two)

print(a)





