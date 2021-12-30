a=input("enter the list of integers")
x=map(int,a.split())
y=[i for i in x if i > 0]
print(y)
