from LinkedBinaryTree import LinkedBinaryTree 

def binary_tree_even_sum(root):
    ''' Returns the sum of all even integers in the binary tree'''
    if (root is None):
        return 0
    else:
        count1 = binary_tree_even_sum(root.left)
        count2 = binary_tree_even_sum(root.right)
        if (root.data%2==0):
            even_num = root.data
            return even_num + count1 + count2
        else:
            return count1 + count2



a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)

mytree = LinkedBinaryTree(f)

print(binary_tree_even_sum(f))
        
