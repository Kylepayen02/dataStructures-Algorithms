def find_max(lst, low, high):
    """
    : lst type: list[int]
    : low, high type: int
    : return type: int
    """
    if low==high:
        return lst[high] 
    else:
        if lst[low]<lst[low+1] :
            find_max(lst,low+1,high)
        else:
             lst[low+1]=lst[low]
             find_max(lst,low+1,high)
        return(lst[high])
             

print(find_max([13,9,16,3,4,2],0,5))
        
        
