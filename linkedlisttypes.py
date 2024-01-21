import random
import climenu

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
        
class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.size=0
    
    def insert(self, item):
        if self.head == None:
            self.head = Node(item)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(item)
            temp.next.next = self.head
        self.size+=1
        
            
    def insertAt(self, item, index):
        index=int(index)
        # if index == 0:
        #     self.insert(item)
        # else:
        index=index%self.size
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        n = Node(item)
        n.next = temp.next
        temp.next = n
        self.size+=1
    
    def removeAt(self,index):
        index=int(index)
        if index==0:
            self.head=self.head.next
        else:
            index=index%self.size
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
        self.size-=1
        
    def traverse(self):
        print('Circular Linked List: ', end="")
        temp = self.head
        while temp.next != self.head:
            print(temp.item, end="->")
            temp = temp.next
        print(temp.item)
        print(temp.next.item)  # to show that it is circular
        

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(item)
            temp.next.prev = temp
        self.size+=1
        
    def insertAt(self, item, index):
        index = int(index)
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")

        new_node = Node(item)

        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            new_node.next = temp.next
            new_node.prev = temp
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node

        self.size += 1

    
    def removeAt(self,index):
        index=int(index)
        if index==0:
            self.head=self.head.next
        else:
            # index=int(index)%self.size
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp
        self.size-=1
        
    def traverse(self):
        print('Doubly Linked List: ', end="")
        temp = self.head
        while temp.next != None:
            print(temp.item, end="->")
            temp = temp.next
        print(temp.item)
    
    def traverseReverse(self):
        print('Doubly Linked List (Reverse): ', end="")
        temp = self.head
        while temp.next != None:
            temp = temp.next
        while temp.prev != None:
            print(temp.item, end="->")
            temp = temp.prev
        print(temp.item)
    

if __name__=='__main__':
    
    
    # cll=CircularLinkedList()
    # functionChoices = [
    #     ("Insert", cll.insert, ["Enter item to insert: "]),
    #     ("Insert At", cll.insertAt,[ "Enter item to insert: ", "Enter index to insert at: "]),
    #     ("Remove At", cll.removeAt,[ "Enter index to remove at: "]),
    #     ("Traverse", cll.traverse,[])
    # ]
    # climenu.menu(functionChoices, "Circular Linked List", "Enter choice: ")
    
    dll=DoublyLinkedList()
    functionChoices = [
        ("Insert", dll.insert, ["Enter item to insert: "]),
        ("Insert At", dll.insertAt,[ "Enter item to insert: ", "Enter index to insert at: "]),
        ("Remove At", dll.removeAt,[ "Enter index to remove at: "]),
        ("Traverse", dll.traverse,[]),
        ("Traverse Reverse", dll.traverseReverse,[])
    ]
    
    climenu.menu(functionChoices, "Doubly Linked List", "Enter choice: ")
        