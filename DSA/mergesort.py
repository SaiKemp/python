def mergeSort(mylist):
    if len(mylist)<=1:
        return mylist
    n =int(len(mylist)/2)
    print(n)
    left,right = mylist[:n],mylist[n:]
    #print(left)
    #print(right)
    leftsorted = mergeSort(left)
    rightsorted = mergeSort(right)
    return merge(leftsorted,rightsorted)

def merge(left,right):
    result = []
    while len(left)!=0 and len(right)!=0:
        leftHead = left[0]
        rightHead = right[0]
        if leftHead<=rightHead:
            result.append(leftHead)
            left = left[1:]
        else:
            result.append(rightHead)
            right = right[1:]
    if len(left)!=0:
        result.extend(left)
    elif len(right)!=0:
        result.extend(right)
    return result
    
    

mylist= [5,4,3,2,1]
print(mylist)
print(mergeSort(mylist))
