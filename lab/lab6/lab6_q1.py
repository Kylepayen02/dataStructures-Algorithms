def sum_to(n):
    """
    : n type: int
    : return type: int
    """
    if n==0:
        return 0
    else:
        return n+sum_to(n-1)

#print(sum_to(8))

