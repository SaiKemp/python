def binarysearch(mylist,x):
    left = 0
    right = len(mylist)
    while left<=right:
        mid = int(left + ((right - left)/2))
        if mylist[mid] == x:
            return mid
        elif mylist[mid]<x:
            left = mid +1
        else:
            right = mid -1
    return -1
print(binarysearch([1,2,4,6,8,9],8))
            
