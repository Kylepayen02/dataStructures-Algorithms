def is_palindrome(input_str, low, high):
    """
    : input_str type: str
    : low, high type: int
    : return type: bool
    """
    if low==high:
        return True
    else:
        if input_str[low]==input_str[high]:
            return is_palindrome(input_str, low+1, high-1)
            
        else: 
            return False 


        
