def maxSubArraySum(a,size):
    temp = 0
    maxsum = 0
    start = 0
    end  = 0
    s=0
    for i in range(size):
        temp = temp+a[i]
        if(maxsum<temp):
            maxsum = temp
            start=s
            end=i
            
        if(temp<0):
            temp=0
            s = i+1
    print(start,end)
    print(a[start:end+1])
    return maxsum

a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(maxSubArraySum(a,len(a)))
