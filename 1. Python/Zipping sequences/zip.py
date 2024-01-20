# Zipping sequences
#     Combine two or more sequence into one sequence.

l1 = [1,2,3]
l2 = ["First", "Second", "Third"]
print(zip(l1, l2)) #Does not return zip as range

print(list(zip(l1, l2))) #Return as tuple pair


days="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
weathers="rainy rainy sunny cloudy rainy sunny sunny".split()
temperatures=[10,12,12,9,9,11,11]

for day, weather, temperature in zip(days, weathers, temperatures):
    print("On {} there was a {} and a temperature was {} degrees".format(day, weather, temperature))  