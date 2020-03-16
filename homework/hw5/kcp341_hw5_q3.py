from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:

    def __init__(self):
        self.data = ArrayStack()
        self.reorder = ArrayDeque()

    def __len__(self):
        return len(self.data.data)

    def is_empty(self):
        return len(self) == 0
    
    def push(self,e):
        self.data.push(e)

    def top(self):
        return self.data.top()
        
    def pop(self):
        return self.data.pop()
        
    def mid_push(self,e):
        if len(self)%2==0:
            for i in range((len(self)//2), len(self)):
                self.reorder.enqueue_first((self.pop()))
        else:
            for i in range(((len(self)//2)+1), len(self)):
                self.reorder.enqueue_first((self.pop()))
        self.push(e)
        for i in range(len(self.reorder)):
            self.push(self.reorder.dequeue_first())

