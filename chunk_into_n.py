from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst)/n)
  return list(
    map(lambda x : lst[x*size: x*size+size],
    list(range(n)))
  )


a = chunk_into_n([1,2,3,4,4,5,6,7],3)

print(a)

