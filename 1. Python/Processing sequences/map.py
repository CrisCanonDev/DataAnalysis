#MAP
# Map functions gets a list and a function as paramenters
# returns a new list

def double(x):
    return 2*x
L=[12,4,-1]
print(map(double, L))
print(list(map(double,L)))

s="10 20 30 45"
X = s.split()

print(X)
print(sum(map(int, X))) #Converts string into integer

