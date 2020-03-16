def is_palindrome(s):
    '''
    :param s type: str
    :return type: bool
    '''
    count = 0
    mid = len(s)//2
    for i in range(mid):
        front = s[i]
        back = s[(len(s)-1)-i]
        if front != back:
            return False
    return True

print(is_palindrome("handnah"))


