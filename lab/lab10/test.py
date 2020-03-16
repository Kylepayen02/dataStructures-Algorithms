from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
dll.add_first(1)
dll.add_last(3)
dll.add_last(5)
dll.add_after(dll.header.next, 2)
dll.add_before(dll.trailer.prev, 4)
dll.delete_node(dll.trailer.prev)
dll.add_first(0)
print(dll)
