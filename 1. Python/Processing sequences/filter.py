#Filter
#Takes a function and list as parameters
# Must take one parameter and return truth values
# filter() creates new list from the original list

def is_odd(x):
    """Returns True if x is odd and False if x is even"""
    return x % 2 == 1
L =[1,3,4,10,15,16]
print(list(filter(is_odd, L))) #Even elements are out

print([l**2 for l in L if is_odd(l)]) # squares of odd values
