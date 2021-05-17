#Converts a number to a list of digits.


def digitize(n):
  return list(map(int, str(n)))


a = digitize(123455)


print(a)

