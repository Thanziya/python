def longest_word(l):
    l2=l.split()
    l3 = []
    for i in l2:
      l3.append(len(i))
    print("The length of the longest word is",max(l3))
l=input("enter a list of words")
longest_word(l)
