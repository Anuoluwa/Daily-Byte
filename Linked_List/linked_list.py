class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next=next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def  append(self, data):
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node
        else:
            self.head = new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    # Prints out the linked list in traditional Python list format. 
    def display(self):
        nodes = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            nodes.append(current_node.data)
        
        print(nodes)


    #def get(self, index):




      


    

a = LinkedListNode(3)
my_ll = LinkedList(a)
print(my_ll.display())
my_ll.append(4)
my_ll.append(5)
my_ll.append(6)
print(my_ll.head.data) #3
print(my_ll.head.next.data) #4
print(my_ll.head.next.next.data) #5
print(my_ll.head.next.next.next.data) #6
print(my_ll.length())
print(my_ll.display())
#print(my_ll.head.next.next.next.next.data) #NoneType