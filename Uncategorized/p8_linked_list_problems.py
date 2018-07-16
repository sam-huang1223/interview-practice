class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        if value:
            self.head = Node(value)
        
    def addFront(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        
    def printList(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
    
    def getKth(self, k):
        p1 = self.head
        p2 = self.head
        
        while k > 0:
            if p2 == None:
                return "ERROR: k value greater than length of linked list"
            p2 = p2.next
            k -= 1
            
        while p2.next:
            p1 = p1.next
            p2 = p2.next
            
        return p1.value
    

def recurseKth(node, k):
    if node.next:
        return k - 1
    
    k = recurseKth(node.next, k)
    
    
    if k == 0:
        return node.value
        
    
            
LL = LinkedList()

LL.addFront(3)
LL.addFront(5)
LL.addFront(7)
LL.addFront(8)
LL.addFront(9) #x
LL.addFront(10)  
LL.addFront(11)
LL.addFront(12) 

print(LL.getKth(7))