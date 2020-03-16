from DoublyLinkedList from DoublyLinkedList
class LinkedQueue:
  def __init__(self):
    self.link=DoublyLinkedList()
  def __len__(self):
    return len(self.link)
  def is_empty(self):
    return len(self.link)==0
  def enqueue(self,elem):
    self.link.add_last(elem)
  def dequeue(self):
    temp=self.link.first_node().data
    self.link.delete(self.link.header.next)
    return temp
  def first(self):
    return self.link.first_node().data
