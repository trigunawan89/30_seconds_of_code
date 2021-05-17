
#Creates a list with the unique values filtered out.

from collections import Counter


def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


a = filter_unique([1, 2, 2, 3, 3, 4, 5])
print(a)
