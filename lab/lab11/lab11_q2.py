def​ ​binary_tree_contains​(root, val):
'''​ Returns True if val exists in the binary tree and false if not'''
    if root:
        return root.data==val or binary_tree_contains(root.right,val) or binary_tree_contains(root.left,val)
    return False
