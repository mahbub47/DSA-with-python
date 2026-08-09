class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def insert_at_head(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

    self.size += 1

  def insert_at_tail(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
    else:
      current = self.head

      while current.next:
        current = current.next

      current.next = new_node

    self.size += 1

  def insert_at_index(self, index, data):
    if index < 0 or index > self.size:
      return None

    if index == 0:
      return self.insert_at_head(data)

    if index == self.size:
      return self.insert_at_tail(data)

    new_node = Node(data)

    count = 0
    current = self.head

    while count < index - 1:
      current = current.next
      count += 1

    new_node.next = current.next
    current.next = new_node

    self.size += 1

  def delete_at_head(self):
    if self.head is None:
      return None

    temp = self.head
    self.head = self.head.next

    data = temp.data

    del temp

    self.size -= 1

    return data

  def delete_at_tail(self):
    if self.head is None:
      return None

    if self.head.next is None:
      data = self.head.data

      self.head = None
      self.size -= 1

      return data

    current = self.head

    while current.next.next:
      current = current.next

    data = current.next.data

    current.next = None

    self.size -= 1

    return data

  def delete_at_index(self, index):
    if index < 0 or index >= self.size:
        return None

    if index == 0:
      return self.delete_at_head()

    if index == self.size - 1:
      return self.delete_at_tail()

    count = 0
    current = self.head

    while count < index - 1:
        current = current.next
        count += 1

    node_to_delete = current.next

    current.next = node_to_delete.next

    data = node_to_delete.data

    del node_to_delete

    self.size -= 1

    return data

  def display(self):
    current = self.head

    while current:
      print(current.data, end=" -> ")
      current = current.next

    print("None")
