def interleave(*t):
    lists = []
    for lists_intervealed in zip(*t):
        for items_into_lists in lists_intervealed:
            lists.append(items_into_lists)
    return lists

print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))