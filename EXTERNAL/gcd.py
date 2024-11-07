def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(a,a%b) 
a=int(input("Enter value of a : ")) 
b=int(input("Enter value of b : ")) 
print(gcd(a,b))