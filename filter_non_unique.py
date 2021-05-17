#Creates a list with the non-unique values filtered out.
from collections import Counter


def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count ==1 ]

a = filter_non_unique([1,2,2,3,3,4,5])

print(a)


