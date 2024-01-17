#Two dice
number = int(input("Enter a number to see the possible options: "))
for x in range(1,7):
    for y in range(1,7):
        if x+y==number:
            print("({}, {})".format(x,y))
        