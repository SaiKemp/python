def binarysearch(mylist,x):
    print(len(mylist))
    if len(mylist) <= 1:
        return mylist
    else:
        mid = len(mylist)//2
        #print(mid)
        if mylist[mid] == x:
            return mid
        elif x > mylist[mid]:
            binarysearch(mylist[mid:],x)
        elif x < mylist[mid]:
            #print(mylist[0:mid])
            binarysearch(mylist[0:mid],x)

m =[4,5,6,7,8,9]
print(binarysearch(m,4))
        
