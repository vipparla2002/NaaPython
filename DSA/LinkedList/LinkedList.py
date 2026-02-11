class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        print(f"Node value is: {self.value}")

class LinkedList:
    def __init__(self,head):
        self.head = head

    def traverse(self):
        currentNode = self.head
        while (currentNode.next != None):
            print(f"{currentNode.value} -> ")
            currentNode = currentNode.next
        print(currentNode.value)

    def nodesCount(self):
        currentNode = self.head
        count = 1
        while(currentNode.next != None):
            count += 1
            currentNode = currentNode.next
        print(f"number of nodes is : {count}")
    
    def delNode(self):
        node = self.node
        if (self.node.next.node != None):
            self.node.next = self.node.next.node.next
        else:
            self.node.next = None
        
        self.node.value = None

       

n1 = Node(3)
n2 = Node(35)
n3 = Node(67)
n4 = Node(99)
n5 = Node('Neelu ')
n6 = Node(n5.value*n1.value)
n7 = Node([n1.value,n3.value,n5.value])
n8 = Node(f"rrrrrrrrrrrrr........ {len(n7.value)}")


n2.next = n3
n3.next = n1
n1.next = n6
n6.next = n5
n5.next = n4
n4.next = n7
n7.next = n8

ll1 = LinkedList(n2)

ll1.traverse()
ll1.nodesCount()

ll1.delNode(n5)
ll1.traverse()