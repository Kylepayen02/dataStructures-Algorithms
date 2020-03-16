from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    def restore_sub_bst(bst,prefix_lst,low,high):
        if low == high:
            bst[prefix_lst[low]] = None
        else:
            bst[prefix_lst[low]] = None
            new_low = high+1
            for i in range(low+1,high+1):
                if prefix_lst[i]>prefix_lst[low]:
                    new_low=i
                    break
            restore_sub_bst(bst,prefix_lst,low+1,new_low-1)
            restore_sub_bst(bst,prefix_lst,new_low,high)
    bst = BinarySearchTreeMap()
    restore_sub_bst(bst,prefix_lst,0,len(prefix_lst)-1)

restore_bst([9,7,3,1,5,13,11,15])

for i in bst:
    print(i)

