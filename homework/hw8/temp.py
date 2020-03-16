
def restore_bst(prefix_lst):
        bst = BinarySearchTreeMap()
        bst.root = bst.Node(bst.Item(prefix_lst[0]))
        prev = bst.root
        for i in range(1,len(prefix_lst)):
            if prefix_lst[0]>prefix_lst[i]:
                curr = bst.Node(bst.Item(prefix_lst[i]))
                if curr.item.key<prev.item.key:
                    prev.left = curr
                    curr.parent = prev 
                    prev = curr 
                else:
                    if prev == bst.root:
                        prev.right = curr
                        curr.parent = prev
                        prev = curr
                    else:
                        while curr.item.key>prev.parent.item.key:
                            prev = prev.parent
                            if prev == bst.root:
                                break 
                        prev.right = curr
                        curr.parent = prev
                        prev = curr
            else:
                
        return bst 
    


x = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])

for i in x:
    print(i)
