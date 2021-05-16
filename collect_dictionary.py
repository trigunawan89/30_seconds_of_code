from collections import defaultdict

def collect_dictinary(obj):
  inv_obj = defaultdict(list)

  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)

ages = {
  'Peter':10,
  'Isable':10,
  'Anna':9,
}

print(collect_dictinary(ages))