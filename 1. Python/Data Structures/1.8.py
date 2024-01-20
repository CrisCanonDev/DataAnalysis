from math import sqrt

def solve_quadratic(a,b,c):
    xPos = float(((-b)+(sqrt(b**2-(4*a*c))))/2*a)
    xNeg = float(((-b)-(sqrt(b**2-(4*a*c))))/2*a)
    return(f"({xPos},{xNeg})")
    

print(solve_quadratic(1,2,1))