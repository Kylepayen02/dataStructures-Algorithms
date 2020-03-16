from BinarySearchTreeMap import BinarySearchTreeMap

def min_max_BST(bst):
    curr_left = bst.root
    curr_right= bst.root
    while curr_left.left:
        curr_left = curr_left.left
    while curr_right.right:
        curr_right = curr_right.right

    return (curr_left.item.key,curr_right.item.key)


a = BinarySearchTreeMap.Item(5)
b =  BinarySearchTreeMap.Item(2)
c = BinarySearchTreeMap.Item(1)
d = BinarySearchTreeMap.Item(3)
e = BinarySearchTreeMap.Item(12)
f = BinarySearchTreeMap.Item(9)
g = BinarySearchTreeMap.Item(21)
h = BinarySearchTreeMap.Item(19)
i = BinarySearchTreeMap.Item(25)

node1 = BinarySearchTreeMap.Node(c)
node2 = BinarySearchTreeMap.Node(d)
node3 = BinarySearchTreeMap.Node(b)
node4 = BinarySearchTreeMap.Node(a)
node5 = BinarySearchTreeMap.Node(e)
node6 = BinarySearchTreeMap.Node(f)
node7 = BinarySearchTreeMap.Node(g)
node8 = BinarySearchTreeMap.Node(h)
node9 = BinarySearchTreeMap.Node(i)


mytree = BinarySearchTreeMap()
mytree.root = node4
node4.left = node3
node4.right = node5
node3.left = node1
node3.right = node2
node5.left = node6
node5.right = node7
node7.left = node8
node7.right= node9


print(min_max_BST(mytree))
        
