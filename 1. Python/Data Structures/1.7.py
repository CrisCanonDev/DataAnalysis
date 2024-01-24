import math


while True:
    shape = input("Choose a shape (triangle, rectangle, circle): ")
    shape = shape.lower()
    if shape == "triangle":
        base = float(input(("Give base of triangle: ")))
        height = float(input(("Give height of triangle: ")))
        print(f"The area of tringle is {(base*height)/2}")
    elif shape == "rectangle":
        width = float(input(("Give width of rectangle: ")))
        height = float(input(("Give height of rectangle: ")))
        print(f"The area of tringle is {base*height}")    
    elif shape == "circle":
        radius = float(input(("Give radius of circle: ")))
        print(f"The area is {radius*math.pi}")
    else:
        print("Unknown shape!")
        break
        
    