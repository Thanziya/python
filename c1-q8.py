dict1={ }
n1=int(input("enter the no:s in dict1"))
for i in range(0,n1):
    k=input("enter the key")
    v=input("enter the value")
    dict1[k]=v
print(dict1)
print("the dictionary sorted in ascending order")
print(sorted(dict1.items()))
print("the dictionary sorted in descending order")
print(sorted(dict1.items(),reverse=1))
