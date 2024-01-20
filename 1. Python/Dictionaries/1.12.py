def distinct_characters(list):
    distint_list = dict()
    for l in list:
        distint_list[l] = len(set(l))
    return distint_list

print(distinct_characters(["check", "look", "try", "pop"]))