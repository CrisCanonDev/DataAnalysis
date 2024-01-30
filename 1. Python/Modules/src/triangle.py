import math

__version__ = "1.0.0"
__author__ = "Cristhian Canon Pineda."

def hypotenuse(l1,l2):
    """
    Returns hypotenuse of right-angled triangle
    
    Parameters:
    - l1, l2: cathethers of a triangle  
    """
    return math.sqrt(math.pow(l1,2)+math.pow(l2,2))

def area(base,height):
    """
    Returns the are of right-angled traingle
    
    Parameters:
    - base, height: cathethers of a triangle  
    """
    return((base*height)/2)
    