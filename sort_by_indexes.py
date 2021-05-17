def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: x[0], reverse= reverse)]

a = ['eggs', 'bread','oranges','jam','apples', 'milk']

b = [3,2,6,4,1,5]

lst1 =  sort_by_indexes(a,b)
lst2 = sort_by_indexes(a,b, True)

print(lst1)
print(lst2)
