from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()

    for val in lst:
        queue.enqueue([val])

    while (len(lst) != len(queue.first())):
        for integer in lst:
            if integer not in queue.first():
                stack.push([integer])
            for i in range(len(stack)):
                queue.enqueue(queue.first()+stack.pop())
            queue.dequeue()

    while queue.is_empty==False:
        permuations_array.append(q.dequeue())

    return permuations_array
