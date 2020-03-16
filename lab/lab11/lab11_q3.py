def​ ​invert_binary_tree1​(root):
'''​ Inverts the binary tree using recursion '''
    if root:
        root.left,root.right=root.right,root.left
        invert_binary_tree1(root.left)
        invert_binary_tree1(root.right)

def​ ​invert_binary_tree2​(root):
'''​ Inverts the binary tree without recursion '''
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.isempty():
        node = queue.dequeue
        node.left, nofe.right = node.right, node.left

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right) 
