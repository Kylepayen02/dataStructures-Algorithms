from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    
    if bin_tree.root == None:
        raise Exception("EmptyTree")
    
    def subtree_min_and_max(root): 
        if (root.left is None and root.right is None):
            return (root.data,root.data)
        elif (root.left is None):
            right = subtree_min_and_max(root.right)
            return (min(root.data,right[0]),max(root.data,right[1]))
        elif (root.right is None):
            left = subtree_min_and_max(root.left)
            return (min(root.data,left[0]),max(root.data,left[1]))
        else:
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            return (min(root.data,left[0],right[0]),max(root.data,left[1],right[1]))
    return subtree_min_and_max(bin_tree.root)



