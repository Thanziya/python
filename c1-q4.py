a=input("enter a list of numbers")
b=a.split()
c=list(map(int,b))
print("list of no:s",c)
n=len(c)
for i in range(n):
    if(c[i]>100):
        c[i]='over'

print(c)

        
