def pos(x):
    return x>0 
def positive_list(lst):
    print(list(filter(pos,lst)))

positive_list([2,-2,0,1,-7])