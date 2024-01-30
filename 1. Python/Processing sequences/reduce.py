#Reduce function

#- Sum function ->Returns sum of numeric list
# By reducing a list to a single element

# Provide operator(Addition/substraction)]
#         starting value (if not added, first elements used as starting value)

L=[2,4,6,8]
def sumreduce(L):
    s=0
    for x in L:
        s = s+x
    return s

from functools import reduce
print(sumreduce(L))
print(reduce(lambda x,y: x+y, L, 0))
print(reduce(lambda x,y: x*y, L, 1)) #Corresponds to  (((1*2)*4)*6)*7