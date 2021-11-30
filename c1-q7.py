l1=input("enter the list of colors")
l2=input("enter the 2nd list of colors")
a=l1.split()
b=l2.split()
print("the list1 colors not contained in list2")
for i in a:
    if i not in b:
        print(i)
