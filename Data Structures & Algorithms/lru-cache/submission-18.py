class LRUCache:

    class Node:

        def __init__(self, key, value, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):

        # Cache
        self.head = None
        self.tail = None
        self.capacity = capacity
        # Values
        self.dct = {}

    def printH(self, node):
        ret = []
        while node:
            ret.append([node.key,node.value])
            node = node.next
        print(ret)

    def reassign(self, node):
        if len(self.dct) <= 1 or self.head == node:
            return 
        elif self.tail == node:
            self.tail.next.prev = None
            self.tail = self.tail.next
            self.head.next = node
            node.prev = self.head
            node.next = None
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.next = node
            node.prev = self.head
            node.next = None
            self.head = node 
        

    def get(self, key: int) -> int:
        print(self.dct.keys())
        if key in self.dct:
            self.reassign(self.dct[key])
            print(self.dct[key].value)
            return self.dct[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print('START')
        self.printH(self.tail)
        # Update case
        if key in self.dct:
            self.dct[key].value = value
            self.reassign(self.dct[key])
        # New Add Case
        else:
            # Check for space
            if len(self.dct) >= self.capacity:
                if len(self.dct) < 2:
                    self.dct.pop(self.tail.key)
                    new = self.Node(key, value)
                    self.dct[key] = new
                    self.head = new
                    self.tail = new
                    return
                self.dct.pop(self.tail.key)
                self.tail.next.prev = None
                self.tail = self.tail.next
                
            new = self.Node(key, value)
            # Empty 
            if not self.head:
                self.head = new
                self.tail = new
                self.dct[key] = new
                return
            # Non-Empty
            self.dct[key] = new
            self.head.next = new
            new.prev = self.head
            self.head = new
            print("END")
            self.printH(self.tail)
    


        
