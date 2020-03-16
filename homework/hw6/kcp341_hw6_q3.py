from DoublyLinkedList import DoublyLinkedList

class CompactString:
  def __init__(self, orig_str):
    self.l=DoublyLinkedList()
    self.string=orig_str
    index=0
    lst=[]
    for counter,i in enumerate(orig_str[:-1],1):
      if orig_str[counter-1]!=orig_str[counter]:
        lst.append((i,counter-index))
        index=counter
    index2=0
    lst2=[]
    newstr=orig_str[::-1]
    for counter,i in enumerate(newstr[:-1],1):
      if newstr[counter-1]!=newstr[counter]:
        lst2.append((i,counter-index2))
        index=counter
    lst.append(lst2[0])
    for i in lst:
      self.linked.add_last(i)
  def __add__(self,other):
    for i in iter(other.linked):
      self.linked.add_last(i)
    return self
  def __lt__(self,other):
    str1=''
    str2=''
    for i in range(len(self.linked)):
      str1+=self.linked.first_node().data[0]*int(self.linked.first_node().data[1])
      self.linked.delete(self.linked.first_node())
    for i in range(len(other.linked)):
      str2+=other.linked.first_node().data[0]*int(other.linked.first_node().data[1])
      other.linked.delete(other.linked.first_node())
    return str1<str2
  def __le__(self,other):
    str1=''
    str2=''
    for i in range(len(self.linked)):
      str1+=self.linked.first_node().data[0]*int(self.linked.first_node().data[1])
      self.linked.delete(self.linked.first_node())
    for i in range(len(other.linked)):
      str2+=other.linked.first_node().data[0]*int(other.linked.first_node().data[1])
      other.linked.delete(other.linked.first_node())
    return str1<=str2
  def __gt__(self,other):
    str1=''
    str2=''
    for i in range(len(self.linked)):
      str1+=self.linked.first_node().data[0]*int(self.linked.first_node().data[1])
      self.linked.delete(self.linked.first_node())
    for i in range(len(other.linked)):
      str2+=other.linked.first_node().data[0]*int(other.linked.first_node().data[1])
      other.linked.delete(other.linked.first_node())
    return str1>str2
  def __ge__(self,other):
    str1=''
    str2=''
    for i in range(len(self.linked)):
      str1+=self.linked.first_node().data[0]*int(self.linked.first_node().data[1])
      self.linked.delete(self.linked.first_node())
    for i in range(len(other.linked)):
      str2+=other.linked.first_node().data[0]*int(other.linked.first_node().data[1])
      other.linked.delete(other.linked.first_node())
    return str1>=str2
  def __str__(self):
    str1=''
    for i in range(len(self.linked)):
      str1+=self.linked.first_node().data[0]
      str1+=str(self.linked.first_node().data[1])
      self.linked.delete(self.linked.first_node())
    return str1
  def __repr__(self):
    return str(self)


p='dabbb'
o='ccdd'
test=CompactString(p)
test2=CompactString(o)
print(str(test))
