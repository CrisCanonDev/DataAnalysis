
c= float(input("Give a number: "))
if c>0:
    print("{} is positive".format(c))
elif c<0:
    print("{} is negative".format(c))
else:
    print("{} is neutral".format(c))
    
    #Break - Continue loop
l = [1,3,6.3,-4.1,7,66]
for x in l:
    if x<0:
        break
print("The first negative number is",x)

from math import sqrt,  log
for x in l:
    if x<0:
        continue
    print(f"the square root of {x} is {sqrt(x)}")
    print(f"Natural algoritm of {x} is {log(x):.4f}\n")