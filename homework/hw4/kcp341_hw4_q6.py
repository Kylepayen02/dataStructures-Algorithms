def appearances(s,low,high):
    if low>high:
        return {}
    else:
        my_dict = appearances(s,low+1,high)
        if s[low] in my_dict:
            my_dict[s[low]]+=1
            return my_dict
        else:
            my_dict[s[low]]=1
            return my_dict



