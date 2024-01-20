def merge(l1,l2):
    lists = l1+l2
    return (lists)
    
list1 = [1,2,3,5,7]
list2 = [2,4,6,7,8]
fList = sorted(merge(list1,list2))
print(fList)