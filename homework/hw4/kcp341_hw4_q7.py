def split_by_sign(lst, low, high):
    if low==high: 
        if lst[low]>0:
            val = lst.pop(low)
            lst.append(val) 
    else:
        split_by_sign(lst,low+1,high)
        if lst[low]>0:
            val = lst.pop(low)
            lst.append(val)
        return lst
        


