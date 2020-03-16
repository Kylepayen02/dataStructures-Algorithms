import ArrayStack

class Queue:
    def __init__(self):
        self.cap = 0;
        self.inflow = ArrayStack();
        slef.outflow = ArrayStack();
    def __len__(self):
        return len(self.inflow) + len(self.outflow);

    def is_empty(self):
        return len(self.inflow) + len(self.outflow) == 0;

    def enqueue(self,e):
        self.inflow.push(e);

    def dequeue(self):
        x = self.outflow.is_empty();
        if x:
            for token in range(len(self.inflow)):
                self.outflow.push(self.inflow.pop())
            return self.outflow.pop()
