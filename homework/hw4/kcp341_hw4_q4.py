def list_min(lst, low, high):
    if low==high:
        return lst[high]
    else:
        part = list_min(lst,low+1,high)
        if lst[low]<part:
            return lst[low]
        else:
            return part






