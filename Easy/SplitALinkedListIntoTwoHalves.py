#
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        cur = self.head
        first = Node(data)

        first.next = cur

        if cur == None:
            first.next = first
        else:
            while cur.next != self.head:
                cur = cur.next
            
            self.head = first

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def split_list(self):

        cur = self.head
        length = 0
        
        while cur:
            cur = cur.next
            length += 1

            if cur is self.head:
                break
        
        # Length is known
        left_end = 0
        pos = 0

        if length % 2 == 0:
            left_end = length // 2 - 1
        else:
            left_end = length // 2

        while pos < left_end:
            cur = cur.next
            pos += 1

        cur2 = cur.next
        start2 = cur2
        cur.next = self.head
        cur = cur.next
        
        while cur2.next != self.head:
            cur2 = cur2.next
        
        cur2.next = start2
        cur2 = cur2.next

        return cur, cur2


'''
cll = CircularLinkedList()
cll.append_node(0)
cll.append_node(1)
cll.append_node(2)
cll.append_node(3)
cll.append_node(4)
#cll.append_node(6)
cll.print_list()
print("Separator")
cll.split_list()
'''
