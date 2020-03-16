from BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    mytree = BinarySearchTreeMap() 
    for i in range(1,n+1):
        mytree.insert(i,None)
    return mytree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst,1,n)
    return bst

def add_items(bst,low,high):
    if low==high:
        bst.insert(int(low))
    else:
        bst.insert(int((low+high)/2))
        add_items(bst,low,((low+high)/2)-1)
        add_items(bst,((low+high)/2)+1,high)






        


    

