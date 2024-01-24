d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}


def reverse_dictionary(dicts):
    newDict = dict()
    for key, val in dicts.items():
        for v in val:
            if not v in newDict:
                newDict[v] = [f'{key}']
            else:
                newDict[v].append(key)
    
    return newDict 


print(reverse_dictionary(d))