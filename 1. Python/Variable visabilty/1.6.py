#Triple Square
def triple(x):
    return x*2

def square(x):
    return x**2 

for x in range(1,11):
    print("triple({})=={} square({})=={}".format(x,triple(x),x,square(x)))
    if triple(x) < square(x):
        break