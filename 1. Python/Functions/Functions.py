def double(x):
    "This functions multiplies its argument by two"
    return x*2
print(double(2), double(5), double("xyz"))

#double doc
print("The docstring is:", double.__doc__)
help(double)   


def sumOfSquares(lst):
    "Computes the sum of squares of elements in list given as parameter"
    s=0
    for x in lst:
        s += x**2
    return s
print(sumOfSquares([-6]))
print(sumOfSquares([5,9,5]))
