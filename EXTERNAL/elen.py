s=input("Enter a String :") 
k=s.split() 
for i in k: 
    if(len(i)%2==0): 
        print("Words with Even Length : ",i)