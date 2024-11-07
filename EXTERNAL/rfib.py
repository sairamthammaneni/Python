def rfib(n): 
    if n<=1: 
       return 1 
    else: 
       return (rfib(n-1)+rfib(n-2)) 
a=int(input(" Enter No.of terms you want : ")) 
if a<=0: 
     print("!!! Enter a positive integer !!!") 
else: 
     print("Fibonacci sequence : ") 
     print(0) 
     for i in range(a-1): 
          print(rfib(i))