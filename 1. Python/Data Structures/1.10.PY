def detect_ranges(lst):
    check = True
    start = lst[0]
    end = lst[0]
    final_list = []
    lst = sorted(lst)
    for current_val in lst[1:]:
        if current_val == end+1:
            end = current_val
        else:
            if start == end:
                final_list.append(start)
            else:
                final_list.append((start, end+1))
            start = end = current_val
        
    if start == end:
        final_list.append(start)
    else:    
        final_list.append((start, end+1))
    
    return final_list
        
lst = [2,5,4,8,12,6,7,10,13]
print(sorted(lst))
print(detect_ranges(lst))
