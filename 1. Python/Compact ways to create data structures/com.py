L = []
for x in range(10):
    L.append(x**2)
print(L)

#List comprehension  {a^3 : a ∈ {1,2,…,10}}
f = [i**3 for i in range(1,11)]
print("List comprehension",f)

#Dictionary comprehension 
d= {k: k**2 for k in range(10)}
print("Dictionary comprehension",d)

#Set comprehension
s = {i*j    for i in range(10)
            for j in range(10)}
print("Set comprehension",s)