a=input("enter the list")
x=map(int,a.split())
y=[i for i in x if i % 2 != 0]
print(y)
