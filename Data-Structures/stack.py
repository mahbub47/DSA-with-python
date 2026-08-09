from singly_linked_list import SinglyLinkedList

class Stack:
  def __init__(self):
    self.stack = SinglyLinkedList()
    self.size = 0

  def push(self,data):
    self.stack.insert_at_head(data)
    self.size += 1

  def pop(self):
    data = self.stack.delete_at_head()
    if data:
      self.size -= 1
    return data

  def peek(self):
    if self.stack.head:
      return self.stack.head.data
    return None

  def is_empty(self):
    if self.stack.head:
      return False
    return True

  def size(self):
    return self.size