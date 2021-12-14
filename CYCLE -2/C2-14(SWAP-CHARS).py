str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")
x=str1[0:1]
str1=str1.replace(str1[0:1],str2[0:1])
str2=str2.replace(str2[0:1],x)
print(str1+" "+str2)
