class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def get_size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next
        
        return count
    
    def get_middle_node(self, count):
        mid_count = count // 2
        current = self.head
        
        for i in range(mid_count):
            current = current.next
        
        return current.data
        
    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True
            current = current.next   
        return False
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_node(self, data):
        current = self.head
        previous = None
        
        if current is not None and current.data == data:
            self.head = current.next
            return
        
        while current is not None and current.data != data:
            previous = current
            current = current.next
            
        if not current:
            return
        
        previous.next = current.next
    
    
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
Third = Node(3)
Forth = Node(4)
Fifth = Node(5)

ll.head.next = second
second.next = Third
Third.next = Forth
Forth.next = Fifth

insert_data = 0
ll.insert_at_head(insert_data)

delete_data = 4
ll.delete_node(delete_data)


print("Linked list is: ", end="")
current = ll.head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()


print("Size of linked list is: ", ll.get_size())
print("Middle node of linked list is: ", ll.get_middle_node(ll.get_size()))
print("Searching for Target in linked list: ", ll.search(3))

