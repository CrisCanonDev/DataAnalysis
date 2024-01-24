def transform(str1, str2):
    lis1 = list(map(int,str1.split()))
    lis2 = list(map(int,str2.split()))
    return list(map(lambda x,y : x*y, lis1, lis2))
            
print( transform("1 5 3", "2 6 -1"))