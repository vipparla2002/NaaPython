class Node:
    def __init__(self,data):
      self.data = data
      self.next = None

class Queue:
    def __init__(self):
       self.last = None

    def add(self,data):
        newNode = Node(data)
        if self.last is None:
          self.last = newNode
        else:
          self.next = newNode
          newNode = self.last
        
    def remove(self):
        if self.last is None:
          return None
        else :
           removedItem = self.last.data
           return removedItem
    
    def clear(self):
        self.last = None