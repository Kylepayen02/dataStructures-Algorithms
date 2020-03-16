from ArrayStack import ArrayStack 

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data.data) 

    def is_empty(self):
        return len(self) == 0

    def push(self,e):
        if len(self)==0:
            self.data.push((e,e))
        else:
            if self.data.data[-1][1]>e:
                self.data.push((e,self.data.data[-1][1]))
            else:
                self.data.push((e,e))
                
    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.data[-1][0]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()[0]

    def max(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        else:
            return self.data.data[-1][1]




