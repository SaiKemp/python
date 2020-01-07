def getPairsofSum(inplist,sum):
    for i in range(len(inplist)):
        for j in range(i+1,len(inplist)):
            if inplist[i]+inplist[j]==sum:
                print("("+str(inplist[i])+","+str(inplist[j])+")")

getPairsofSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
