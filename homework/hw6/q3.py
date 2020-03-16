import DoublyLinkedList from DoublylinkedList 
class CompactString:
    def __init__(self, orig_str):
        self.data_dll = DoublyLinkedList()
        temp_dict = {}
        for i in orig_str:
            if i not in temp_dict:
                self.data.dll.add_last(temp_dict.items()[0]) 
                temp_dict = {}
                temp_dict[i] = 1
            else:
                temp_dict[i] +=1
                
        
