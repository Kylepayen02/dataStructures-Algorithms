def is_height_balanced(bin_tree):
    if bin_tree.root is None:
        def subtree_height(root):
            if root.left is None and root.right is None:
                return (0,0,True) 
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left = 1 + subtree_height(root.left)
                right = 1 + subtree_height(root.right)
                elif (root.left is None):
                return 1 + subtree_height(root.right)
            \
                
