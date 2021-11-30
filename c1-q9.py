dict1={ }
dict2={ }
n1=int(input("enter the no:s in dict1"))
n2=int(input("enter the no:s in dict2"))
for i in range(0,n1):
    k=input("enter the key")
    v=input("enter the value")
    dict1[k]=v
print(dict1)
for i in range(0,n2):
    k=input("enter the key")
    v=input("enter the value")
    dict2[k]=v
print(dict2)
for key in dict1:
    if key in dict2:
        dict2[key]+=dict1[key]
    else:
        pass
dict1.update(dict2)
print("the merged dictionary is",dict1)

