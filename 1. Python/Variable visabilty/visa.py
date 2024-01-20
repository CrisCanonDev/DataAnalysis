#Variable visability

i=4     #Global variable
def x():
    i= 2    #Local variable
    print(i) #2
x()
print(i)    #4


# Rebind a global variable
i=4     #Global variable
def x():
    global i
    i= 2    #Local variable
    print(i) #2
x()
print(i)    #2

