from math import comb

def binomial_coefficient(n,k):
  return comb(n,k)

a = binomial_coefficient(8, 2)

print(a)