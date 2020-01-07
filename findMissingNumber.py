def findmissing(inp):
    listsum = sum(inp)
    n = int(len(inp))
    sumofn = (n+1)*(n+2)/2
    return sumofn - listsum
    
print findmissing([1,2,4,5,6])
