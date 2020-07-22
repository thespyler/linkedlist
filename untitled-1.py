class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Print(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next
            
    def Insert_head(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

    def insert_node(self, val, pos):
        main = self.head
        for i in range(1, pos - 1):
            main = main.next
        new_node = Node(val)
        new_node.next = main.next
        main.next = new_node

def main():
    a = Node(12)
    b = Node(7)
    c = Node(11)
    d = Node(5)

    a.next = b
    b.next = c
    c.next = d

    ll = LinkedList()
    ll.head = a
    ll.Insert_head(19)
    ll.insert_node(99, 3)
    ll.Print()
if __name__ == '__main__':
    main()