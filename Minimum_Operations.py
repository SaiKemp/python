# You are given a number N. You have to find the number of operations required to reach N from 0. You have 2 operations available:

# Double the number
# Add one to the number
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N.

# Output:
# For each test case, in a new line, print t
#Example:
#Input:
#2
#8
#7
#Input:
#4
#5

iters = int(input())

while(iters>0):
    n = int(input())
    i=0
    while(n>0):
        if(n%2==0):
            n=n/2
            i = i+1
        else:
            n=n-1
            i=i+1
    print(i)
    iters = iters - 1
