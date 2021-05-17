from math import ceil

def chunk(lst, size):
  return list(
    map( lambda x: lst[x*size: x*size+size],
    list(range(ceil(len(lst)/ size))))
  )

a = chunk([1,2,3,4,5,],2)

print(a)



