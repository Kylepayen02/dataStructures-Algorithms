import LinkedBinaryTree
def​ ​binary_tree_even_sum​(root):
'''​ Returns the sum of all even integers in the binary tree​
if root.left==None and root.right==None:
    return 0
else:
     if root.right%2==0:
         return 1+binary_tree_even_sum(root.)

'''
    if root:
        return binary_tree_even_sum(root.left)+ binary_tree_even_sum(root.right) + root.data*(root.data%2==0)
    return 0 
