m=int(input("enter the 1st integer:"))
n=int(input("enter the 2nd integer:"))
a=b=0
count=0
if n>m:
  a=m
  b=n 
else:
  a=n 
  b=m
for i in range(1,b+1):
  if b%i==0 and a%i==0:
    print(i)
    count+=1    
print(f"no of common factors of {m} and {n} is {count}")