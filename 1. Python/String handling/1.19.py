def sum_equation(list = ()):
    
    if not list:
        return "0=0"
    else:
        return sum(list)
    
x = sum_equation([1,2,3])
y = sum_equation()

print(x)
print(y)