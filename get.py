#Retrieves the value of the nested key indicated by the given selector list from a dictionary or list.


from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)

users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1,2,3]
  }

}

a = get(users, ['freddy', 'name', 'last'])
b = get(users, ['freddy','postIds', 1])

print(a)
print(b)

