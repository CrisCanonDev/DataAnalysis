#Two dice (1.5 exercise)
       
l = [ (i,j) for i in range(1,7) for j in range(1,7) if i+j==5]
for x in l:
    print(x)