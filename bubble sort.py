

a= int(input("enter a number"))
b = int(input("enter a number"))
c= int(input("enter a number"))
d=int(input("enter a number"))
e = int(input("enter a number"))

ulist= [a,b,c,d,e]

def bubble_sort():
    n = len(ulist)
    while ulist[n] > ulist[n+1]:
        ulist[n], ulist[n+1] = ulist[n+1], ulist[n]
        n = n + 1
    return ulist
slist = bubble_sort(ulist)
print(slist)
     
