class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_head(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    else:
      temp = self.head
      self.head = new_node
      new_node.next = temp
      return
  
  def insert_at_tail(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = new_node

  def insert_at_index(self, index, data):
    new_node = Node(data)
    count = 0
    if not self.head and index == 0:
      self.head = new_node
      return
    else:
      temp = self.head
      while count != (index  - 1):
        temp = temp.next
        count += 1
      temp1 = temp.next
      temp.next = new_node
      new_node.next = temp1
  
  def delete_at_head(self):
    if not self.head:
      return
    else:
      self.head = self.head.next
      return

  def delete_at_tail(self):
    if not self.head:
      return
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp = None
      return

  def delete_at_index(self,index):
    count = 0
    if index == 0:
      self.delete_at_head()
      return
    else:
      temp = self.head
      while count != index - 1:
        temp = temp.next
        count += 1
      temp2 = temp.next
      temp3 = temp2.next
