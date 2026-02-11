# from StackClassList import Stack
import math 
# stack1 = Stack()

# for i in range(1,int(math.pow(3,5))+1):
#     stack1.push(round(math.sqrt(i),3))

# print(stack1.items)

# print(stack1.size())
# print(stack1.is_empty())
# print(stack1.pop())
# print(stack1.peek())
# print(stack1.push(100))

# print(stack1.items)


from StackClassLinkedList import Stack

stack2 = Stack()

for i in range(1,int(math.pow(3,5))+1):
    stack2.add(round(math.pow(i,1/3),3))

#print(stack2.size)
print(stack2.isEmpty())
print(stack2.see())
print(stack2.remove())
#print(stack2.size)
print(stack2.add(100))
#print(stack2.size)
print(stack2.see())
print(stack2.display())