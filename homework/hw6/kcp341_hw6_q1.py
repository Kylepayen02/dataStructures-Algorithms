from DoublyLinkedList import DoublyLinkedList
class LinkedQueue:
    def __init__(self):
        self.data_dll = DoublyLinkedList()
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self,elem):
        self.data_dll.add_last(elem)
        self.num_of_elems+=1 

    def dequeue(self):
        if self.num_of_elems == 0:
            raise Exception("The LinkedQueue is Empty")
        return(self.data_dll.delete_first())

    def first(self):
        if self.num_of_elems == 0:
            raise Exception("The LinkedQueue is empty")
        return(self.data_dll.header.next.data) 
