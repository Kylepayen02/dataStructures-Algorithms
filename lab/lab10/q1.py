from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __ init__(self):
        self.data = DoublyLinkedList()
        
    def __len__(self):
    ''' Returns the number of elements in the stack. '''
        return len(self.data)
    
    def is_empty(self):
    ''' Returns true if stack is empty and false otherwise.'''
        return (len(self)==0) 
    
    def push(self, e):
    ''' Adds an element, e, to the top of the stack. '''
        self.data.add_last(e) 
    
    def top(self):
    ''' Returns the element at the top of the stack.
    An exception is raised if the stack is empty. '''
        if len(self)==0:
            raise Exception("The linkedStack is empty")
        return self.data.trailer.prev 
    
    def pop(self):
    ''' Removes and returns the element at the top of the stack.
    An exception is raised if the stack is empty. '''
        if len(self)==0:
            raise Exception("The linkedStack is empty")
        last_node = self.top()
        self.data.delete_last()
        return last_node 
    
