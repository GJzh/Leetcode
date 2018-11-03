class LRUCache(object):
    class Node():
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.status = {}
        self.capacity = capacity
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addToEnd(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        
    def moveToEnd(self, node):
        if node == self.tail.prev: return
        node.next.prev = node.prev
        node.prev.next = node.next
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        
    def removeStart(self):
        node = self.head.next
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.status: return -1
        self.moveToEnd(self.status[key])
        return self.status[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.status:
            self.status[key] = self.Node(key, value)
            self.addToEnd(self.status[key])
            self.capacity -= 1
            if self.capacity < 0:
                del self.status[self.head.next.key]
                self.removeStart()
                self.capacity += 1
        else:
            self.status[key].val = value
            self.moveToEnd(self.status[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)