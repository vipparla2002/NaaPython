class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def add(self,item):
        self.items.append(item)
    
    def remove(self):
        if self.isEmpty():
            raise IndexError("remove from empty queue")
        else:
            removed = self.items.pop(0)
            return removed
    
    def see(self, index=0):
        if self.isEmpty():
            raise IndexError("see from empty queue")
        return self.items[index]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items[:]
    
    def clear(self):
        self.items = []