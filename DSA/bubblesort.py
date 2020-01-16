def bubble(mylist):
    for i in range(0,len(mylist)-1):
        #swap = False
        for j in range(0,len(mylist)-i-1):
            print(len(mylist)-i-1)
            if mylist[j]>mylist[j+1]:
                temp = mylist[j+1]
                mylist[j+1] = mylist[j]
                mylist[j] = temp
                #swap = True
        #if swap == False:
            #break
    return mylist

mylist= [5,4,3,2,1]
