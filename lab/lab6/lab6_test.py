
def func1(n):
    if (n<=1):
        return 0
    else:
        return 10+func1(n-2)



def func2(n):
    if (n<=1):
        return 1
    else:
        return 1+func2(n//2)



def func3(lst):
    if (len(lst)==1):
        return lst[0]
    else:
        return lst[0] + func3(lst[1:])

