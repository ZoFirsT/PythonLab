def x_positive(x):
    if x > 0:
        return "x is positive"
    else:
        return "x is not positive"

def xtreeseven(x):

  if x > 0 and x % 3 == 0 and x % 7 == 0:
    return "x is divisible by 3 and 7"
  else:
    return "x is not divisible by 3 and 7"
  
def endswith_one(x):

  if x % 10 == 1:
    return "x is ending with 1"
  else:
    return "x is not ending with 1"
    
x = int(input())
result = x_positive(x) + "\n" + xtreeseven(x) + "\n" + endswith_one(x)
print(result)
