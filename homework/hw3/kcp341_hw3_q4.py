def remove_all(lst, value):
    front=0
    back=len(lst)-1
    count=0
    for i in range(len(lst)):
        if lst[front] == value:
            lst[front],lst[back]=lst[back],lst[front]
            front+=1
            back-=1
            count+=1
        else:
            front+=1
    if count==0:
        raise ValueError("Value is not in list")
    else:
        for i in range(count):
            lst.pop()
    return lst 

print(remove_all([2,4,4,1,2],2))

