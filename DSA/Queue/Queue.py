# from QueueClassList import Queue
# import math

# Queue1 = Queue()

# print(Queue1.isEmpty())#True

# for i in range(1,int(math.pow(3,5))+1):
#     Queue1.add(round(math.sqrt(i),3))

# print(Queue1.size())#243
# print(Queue1.see())#1.0
# print(Queue1.remove())#1.0
# print(Queue1.size())#242
# print(Queue1.add(100))#None
# print(Queue1.size())#243
# print(Queue1.see(len(Queue1.items)-1))#100
# print(Queue1.display())#whole queue items

# Queue1.clear()

from QueueClassLinkedList import Queue
import math

Queue2 = Queue()

for i in range(1,int(math.pow(3,5))+1):
    Queue2.add(round(math.pow(i,1/3),3))
    addedItem = round(math.pow(i,1/3),3)
    print(f"Added: {addedItem}") 

print(Queue2.display())#whole queue items