from ArrayStack import ArrayStack 

def stack_sum(s):
    """
    : s type: ArrayStack
    : return type: int
    """
    if len(s)==1:
        return s.top()
    else:
        val = s.pop()
        res = val + stack_sum(s)
        s.push(val)
        return res
        
        

s=ArrayStack()
s.push(-8)
s.push(-5)
s.push(10)
s.push(9)
s.push(-7)
s.push(6)
s.push(5)
s.push(-14)
s.push(1)

print(stack_sum(s))

        
