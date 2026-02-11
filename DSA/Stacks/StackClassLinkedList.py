class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
            self.top = None
    
    def add(self,data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def remove(self):
        if self.top is None:
            return None
        removedNode = self.top
        self.top = self.top.next
        return removedNode.data
    
    def see(self):
        if self.top is None:
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    def display(self,interval=1):
        current = self.top
        while current:
            print(current.data)
            current = current.next