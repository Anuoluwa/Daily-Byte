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
            while current.next:
                current = current.next

            current.next = new_node
        else:
            self.head = new_node





      


    

a = LinkedListNode(3)
my_ll = LinkedList(a)
my_ll.append(4)
my_ll.append(5)
my_ll.append(6)
print(my_ll.head.data) #3
print(my_ll.head.next.data) #4
print(my_ll.head.next.next.data) #5
print(my_ll.head.next.next.next.data) #6
print(my_ll.head.next.next.next.next.data) #NoneType