class LRUCache:
    class Node:
        def __init__(self, k, x):
            self.val = x
            self.key = k
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = self.tail = self.Node(0, 0)
        self.capacity = capacity
        self.h = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.h:
            self.moveToEnd(self.h[key])
            return self.h[key].val
        else:
            return -1
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.h:
            self.h[key].val = value
            self.moveToEnd(self.h[key])
        else:
            node = self.Node(key, value)
            if len(self.h) == self.capacity:
                del(self.h[self.head.next.key])
                self.head.next = self.head.next.next
                if self.head.next:
                    self.head.next.prev = self.head
                else:
                    self.tail = self.head
                 
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.h[key] = node

    def moveToEnd(self, node):
        if node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node
Solution 2:
class LRUCache:
    class Node:
        def __init__(self, k, x):
            self.val = x
            self.key = k
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = self.tail = None
        self.capacity = capacity
        self.h = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.h:
            self.moveToEnd(self.h[key])
            return self.h[key].val
        else:
            return -1
            
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.h:
            self.h[key].val = value
            self.moveToEnd(self.h[key])
        else:
            node = self.Node(key, value)
            if len(self.h) == self.capacity:
                self.removeHead()
            
            if not self.head: self.head = self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.h[key] = node

    
    def moveToEnd(self, node):
        if node != self.tail:
            if node == self.head:
                self.head = self.head.next
            else:
                node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node
    
    def removeHead(self): 
        temp = self.head
        self.head = self.head.next
        del(self.h[temp.key])
        if self.head: self.head.prev = None
        else: self.tail = self.head

