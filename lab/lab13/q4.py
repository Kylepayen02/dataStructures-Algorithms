def is_BST(BST):
    return is_BST_helper(BST.root)[2]


def is_BST_helper(root):
    ''' Returns a tuple (min, max, bool)'''
    if not root.left and not root.right:
        return(True,root.item.key,root.item.key)
    if root.left and root.right 
