s=input("Enter a string : ")
r=""
for i in s :
    r=i+r
if s==r :
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")