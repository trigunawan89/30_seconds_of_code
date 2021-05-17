#Inverts a dictionary with unique hashable values.


def invert_dictionary(obj):
  return {value: key for key, value in obj.items()}


ages = {
  'Peter': 10,
  'Joko': 9,
  'Ana': 7,
}

print(invert_dictionary(ages))

