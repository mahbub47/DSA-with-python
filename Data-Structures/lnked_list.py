class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
      return self.tail
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      return self.tail

linked_list = DoublyLinkedList()
node_1 = linked_list.append(1)
node_2 = linked_list.append(2)
node_3 = linked_list.append(3)
node_22 = linked_list.append(22)
node_32 = linked_list.append(32)

temp1 = node_3
temp2 = node_3.prev

while temp1 or temp2:
  if temp1:
    print(temp1.data)
    temp1 = temp1.next
  if temp2:
    print(temp2.data)
    temp2 = temp2.prev


