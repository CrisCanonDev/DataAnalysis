# JOINING
# join(seq)

x ="--".join(["123","456","789"])
print(x) # 123--456--789

L = [str(y) for y in range(100)]
s= ""
for y in L:
    s += " "+y #Avoid use as it create string every iteration
    
print(s)

print(" ".join(L)) #Correct way


# SPLIT
"123--456--789".split("--") #['123', '456', '789']