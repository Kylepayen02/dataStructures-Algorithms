def find_max_even(lst,low,high):
    if low==high:
        if lst[low]%2==0:
            return lst[low]
        else:
            return None
    else:
        max_even=find_max_even(lst,low+1,high)
        if (lst[low]>max_even) and lst[low]%2==0:
            return lst[low]
        #have to check if it is not none 
        elif
            return max_even

print(find_max_even([13, 9, -16, 3, 4, 2],0,5))
