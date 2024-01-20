# SETS
#     Dynamic, unordered container
    # Like dictionary, but only keys are stored. Each key stored once
    
s={1,1,1}
print(s)
s=set([1,2,2,'a'])
print(s)
s=set()  # empty set
print(s)
s.add(7) # add one element
print(s)

s="missisipi"
print("there are {} distinct characters in {}".format(len(set(s)),s))


s=set([1,2,7])
t=set([2,8,9])
print("Union:", s|t) #s.union(t)
print("Intersection:", s&t) #s.intersection(t)
print("Difference:", s-t) #s.differce(t)
print("Symmetric difference", s^t) #s.symmetric_difference(t)