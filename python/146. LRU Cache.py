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

Solution 3:
class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = self.tail = None
        self.status = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.status:
            self.moveToEnd(self.status[key])
            return self.status[key].val
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.status:
            self.status[key].val = value
            self.moveToEnd(self.status[key])
        else:
            self.status[key] = self.Node(key, value)
            if self.capacity == 0:
                self.removeHead()
            self.insertToEnd(self.status[key])
                
    def removeHead(self):
        if self.head:
            del self.status[self.head.key]
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.capacity += 1
        
    def insertToEnd(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node
        self.capacity -= 1
        
    def moveToEnd(self, node):
        if node == self.tail: return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
