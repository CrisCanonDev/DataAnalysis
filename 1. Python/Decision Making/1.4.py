for x in range(1,11):
    for y in range(1,11):
        print(f"{x * y}", end="\t")
    print("")
    
#Absolute Value
x = int(input("Enter a integer: "))
if x >= 0:
    a = x
else:
    a = -x
print("The absolute value of %i is %i "%(x,a))