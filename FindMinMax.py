def findMinMax(inplist):
    maxval = inplist[0]
    minval = inplist[0]
    for i in range(1,len(inplist)):
        if inplist[i]>maxval:
            maxval = inplist[i]
        if inplist[i]<minval:
            minval = inplist[i]
    return "Maximum value is-"+str(maxval)+'\n' + "Minimum value is-"+str(minval)
    
print findMinMax([3,51,8,24,7])
