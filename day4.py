#day 4 =ds

#linked list

#first step in liked list is  creating nodes :

#basic which create node

class Node:
    def __init__(self,data):
        self.data=data #stored val
        self.next=None #pointer to next


#create node

node1= Node(10)
node2=Node(20)
node3=Node(30)

print(f"node1: data={node1.data},next={node1.next}")
print(f"node2: data={node2.data},next={node2.next}")
print(f"node3: data={node3.data},next={node2.next}")
print()

#link nodes:

node1.next=node2
node2.next=node3

print(f"node1.next.data={node1.next.data}")
print(f"node2.next.next.data={node2.next.next.data}")
print()
 


#traverse: used to travall from one node to other node:

current = node1
while current is not None:
    print(f"{current.data}",end="->")
    current = current.next
print(f"None")

#advance liked list

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
      
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("->".join(elements) + " -> None")
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def search(self,target):
        current=self.head
        while current is not None:
           if current.data== target:
              return True
           current=current.next
        return False
    def delete(self,data):
        if self.head is None:
           return
        if self.head.data==data:
           self.head=self.head.next
           return
          
        current = self.head
        while current.next is not None:
              if current.next.data==data:
                 current.next=current.next.next
                 return
              current = current.next
          
       
        
      
        
   
l1 = Linkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.display()  # Output: 10->20->30->40 -> None


l1.prepend(5)
l1.display()

print(f"{l1.search(20)}")
print(f"{l1.search(99)}")

l1.delete(30)
l1.display()

#stack lifo last in first out

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

s = stack()
s.push("A")
s.push("B")
s.push("C")
print(f"  Stack after pushing A, B, C:")
print(f"    Peek: {s.peek()}")
print(f"    Size: {s.size()}")
print(f"    Pop: {s.pop()}")
print(f"    Stack is empty: {s.is_empty()}\n")

#queue

from  collections import deque
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print("{queue}")

front = queue.popleft()
print(f"Depueued {front}, queue is now :{queue}")

#advence:
class Queue:
    def __init__(self):
        self.items=deque()
    def enqueue(self,items):
        self.items.append(items)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

q=Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")
print(f"  Queue after enqueuing Alice, Bob, Charlie:")
print(f"    Front: {q.peek()}")
print(f"    Size: {q.size()}")
print(f"    Dequeue: {q.dequeue()}")
print(f"    Queue is empty: {q.is_empty()}\n")
