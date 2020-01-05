def repeat(input):
    repeated = []
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            if input[i]==input[j] and input[j] not in repeated:
                repeated.append(input[i])
    
    return repeated
