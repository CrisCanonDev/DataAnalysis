

def find_matching(lst, s):
    indexWords = list()
    for key, val in enumerate(lst):
        if s in val:
            indexWords.append(key)
    return indexWords


print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
