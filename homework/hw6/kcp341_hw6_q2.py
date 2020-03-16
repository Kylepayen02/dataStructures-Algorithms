from DoublyLinkedList import DoublyLinkedList
class Integer:
  def __init__(self,num_str):
    self.data = DoublyLinkedList()
    for i in num_str:
      self.data.add_last(i)
  def __add__(self,other):
    carry=0
    lst=[]
    length=len(self.data)
  if (len(self.linked)>len(other.linked)) else len(other.linked)
    for i in range (length):
      first_data=0 if self.linked.is_empty() else int(self.linked.last_node().data)
      second_data =0 if other.linked.is_empty() else int(other.linked.last_node().data)
      Sum=first_data+second_data+carry
      if Sum>=10:
        carry=1
        Sum=Sum%10
      else:
        carry=0
      lst.append(Sum)
      if not self.linked.is_empty():
        self.linked.delete(self.linked.trailer.prev)
      if not other.linked.is_empty():
        other.linked.delete(other.linked.trailer.prev)
    self.linked.header.next=self.linked.trailer
    self.linked.trailer.prev=self.linked.header
    return int(''.join(map(str,reversed(lst))))
