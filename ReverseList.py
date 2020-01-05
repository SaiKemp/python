# Reverse without inbuilt function
def reverse(input):
    if input is None or len(input)<2:
        return input
    reverse =  []
    for i in range(len(input)):
        reverse.append(input[len(input)-1-i])
    return reverse

print(reverse([1,2,3,4,5]))

# Reversing a list using reverse() 
def Reverse(lst): 
    lst.reverse() 
    return lst 
    
# Reversing a list using slicing technique 
def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst
