
#a

def print_triangle(n):
    if n==0:
        return 1
    else:
        print_triangle(n-1)
        return("*"*n)

#b

def print_opposite_triangles(n):
   if n==0:
       return 1
   else:
       return("*"*n)
       print_opposite_triangles(n-1)
       return("*"*n)


#c
def print_ruler(n):
    if n==0:
        return 1
    else:
        print_ruler(n-1)
        return("-"*n)
        print_ruler(n-1)

