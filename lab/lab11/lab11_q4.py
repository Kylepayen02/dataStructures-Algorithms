def is_full(root):
    if root:
        has_2_children = root.left and root.right
        has_0_children = not (root.left or root.right)
        #either has 2 children or 0 children
        return(has_2_children or has_0_children) and is_full(root.left) and is_full(root.right)
    return True

    
