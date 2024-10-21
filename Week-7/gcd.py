def gcd(x,y):
  if x==0:
    return y
  elif y==0:
    return x
  else:
    return gcd(y,x%y)
x=int(input("Enter X value : "))
y=int(input("Enter Y value : "))
print(gcd(x,y))
