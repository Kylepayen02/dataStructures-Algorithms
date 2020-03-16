from DoublyLinkedList import DoublyLinkedList 

class Integer:
    def __init__(self, num_str):
        self.data.dll = DoublyLinkedList()
        for i in num_str:
            self.data.dll.add_last(int(i))
        self.size = len(num_str) 

    def __add__(self, other):
        sum = 0 
        if self.size(self) > self.size(other):
            for i in self.data.dll:
                new_str += str(i)
        new_int = Integer(new_str) 
                

    def __repr__(self):
        ''' Creates and returns the string representation
        of self'''
