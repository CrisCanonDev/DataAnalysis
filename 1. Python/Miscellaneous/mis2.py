a,b,c ="bye"

print(b,a,c) # y b e

d = dict(x=5, y=10)

key1, key2 = d #Stored in key1 and key2 variable the key values 
print(key1, key2)

for key, value in d.items():
    print(f"For key '{key}', value {value} was stored.")
    
#Remove var
s = "Hello"
del s
print(s) #Error

    #Delete item from a container
L = [10,103,55,150]
del L[1]
print(L) # [10,55,150]
