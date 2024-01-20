l=[1,2,98,5,-1,2,0,5,10]
ocurrence = 0
for index,value in enumerate(l):
    print(index,value )
    
#Check the index when a value appears in the second time
for index, value in zip(range(len(l)),l):
    if l == 5:
        ocurrence += 1
        if ocurrence == 2:
            break   
print(index-1)