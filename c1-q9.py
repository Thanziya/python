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
dict2.update(dict1)
print("the merged dictionary is",dict2)
