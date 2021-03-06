#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#Example:
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        curr_max = a[0]
        maxsum = a[0]
        max_so_far = a[0]
        for i in range(1,len(a)):
            maxsum =max(maxsum,a[i])
        if(maxsum<0 or len(a)==1):
            return maxsum
        maxsum = 0
        for i in range(1,len(a)): 
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
        return max_so_far
