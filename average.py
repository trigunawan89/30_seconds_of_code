def average(*args):
  return sum(args, 0.0)/ len(args)


var1 = average(1,2,3,4,5)
var2 = average(*[1,2,3,4])
print(var2)