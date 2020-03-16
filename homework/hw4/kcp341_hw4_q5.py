def count_lowercase(s,low,high):
    if low==high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        count = count_lowercase(s, low + 1, high)
        if s[low].islower():
            count+=1
        return count

def is_number_of_lowercase_even(s,low,high):
    if low==high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            count = 1+count_lowercase(s, low + 1, high)
        else:
            count = 0 + count_lowercase(s, low + 1, high)
        if count==0:
            return False
        else:
            return count%2==0 
        

