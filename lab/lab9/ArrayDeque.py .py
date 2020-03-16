import ctypes

def make_array(n):
    return (n* ctypes.py_object)()

class ArrayDeque:

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]
    def last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[(self.front_ind + self.num_of_elems)/len(self.data_arr)]
    def enqueue_first(self,elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            self.num_of_elems += 1
    def enqueue_last(self,elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            self.data_arr[self.num_fo_elems] = elem
            self.num_of_elem +=1
    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception ("Queue is empty")
        self.data_arr[self.front_ind] = None
        val = self.data_arr[self.front_ind]
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    
    
        
