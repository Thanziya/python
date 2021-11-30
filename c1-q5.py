a=input("enter the 1st list of integers")
b=input("enter the 2nd list of integers")
l1=a.split()
c=list(map(int,l1))
l2=b.split()
d=list(map(int,l2))
if(len(c)==len(d)):
    print("the lists are of same length")
else:
    print("the lists are of different length")
s1=0
for i in range(0,len(c)):
    s1+=c[i]
print("sum of list1=",s1)

    
s2=0
for j in range(0,len(d)):
    s2+=d[j]
print("sum of list2=",s2)
if(s1==s2):
    print("the sums are equal")
else:
    print("the sums are different")
for i in range(0,len(d)):
    if(c[i] in d):
        print("%i occurs in both lists"%(c[i]))
