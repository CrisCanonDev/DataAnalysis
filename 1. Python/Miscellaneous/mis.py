#Find whether a container includes an element, in operator
#Returns a truth value    

print(1 in [1,2]) #True

d= dict(a=1, b=3)
print("b" in d) #True

s= set()
print(1 in s) #False
print("x" in "text") #True

#Check if a string is part to another string
print("issi" in "missisippi") # True
print("issp" in "missisippi") # False