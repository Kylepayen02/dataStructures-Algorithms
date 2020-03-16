def product_evens(n):
    """
    : n type: int
    : return type: int
    """
    if (n%2==1):
        n=n-1
    if (n<=1):
        return 1
    else:
        if (n%2==0):
            return n * product_evens(n-2)

print(product_evens(8))
        
