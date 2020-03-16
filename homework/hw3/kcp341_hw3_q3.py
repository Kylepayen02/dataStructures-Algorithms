def find_duplicates(lst):
    duplicate_lst=[]
    for i in range(len(lst)): 
        if lst[abs(lst[i])] >= 0: 
            lst[abs(lst[i])] = -1* lst[abs(lst[i])] 
        else: 
            duplicate_lst.append(abs(lst[i]))
    return duplicate_lst






