def max_two_products(lst):
    max1=0
    max2=0
    for i in lst:
        if (max1<i):
            max1=i
    for j in lst:
        if (max2<j and max1!=j):
            max2=j
    return (max1*max2)

print(max_two_products([11, 3, 4, 9, 2, 7, 8, 10, 5]))
