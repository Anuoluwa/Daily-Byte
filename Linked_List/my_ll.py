class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    
    def __repr__(self):
        return f"Listnode({repr(self.data)})"

    def print_list(self, head):
        elem = head.data
        while elem is not None:
            print(elem)
            elem = elem.next




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(head.next.data)
print(head.next.next.data)