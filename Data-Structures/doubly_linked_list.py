class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    self.tail = None

  def insert_at_head(self, data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    else:
      self.head = new_node
      self.tail = new_node
    self.size += 1

  def insert_at_tail(self, data):
    new_node = Node(data)
    if self.tail:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
    self.size += 1

  def insert_at_index(self, index, data):
    if index < 0:
      return
    count = 0
    if index == 0:
      self.insert_at_head(data)
      return
    if index >= self.size:
      self.insert_at_tail(data)
      return
    new_node = Node(data)
    current = self.head
    while count < index - 1:
      current = current.next
      count += 1
    temp = current.next
    current.next = new_node
    new_node.prev = current
    new_node.next = temp
    temp.prev = new_node
    self.size += 1

  def remove_at_head(self):
    if self.head:
      temp = self.head
      data = temp.data
      if self.head.next:
        self.head = self.head.next
        self.head.prev = None
      else:
        self.head = None
        self.tail = None
      del temp
      self.size -= 1
      return data
    return None

  def remove_at_tail(self):
    if self.tail:
      temp = self.tail
      data = temp.data
      if self.head is self.tail:
        self.head = None
        self.tail = None
      else:
        self.tail = self.tail.prev
        self.tail.next = None
      del temp
      self.size -= 1
      return data
    return None

  def remove_at_index(self, index):
    if index < 0:
      return None
    if index == 0:
      return self.remove_at_head()
    if index >= self.size:
      return None
    if index == self.size - 1:
      return self.remove_at_tail()
    mid = self.size // 2
    count = 0
    current = self.head
    if index > mid:
      count = self.size - 1
      current = self.tail
      while index < count:
        current = current.prev
        count -= 1
    else:
      while index > count:
        current = current.next
        count += 1
    current.prev.next = current.next
    current.next.prev = current.prev
    data = current.data
    self.size -= 1
    del current
    return data
    
