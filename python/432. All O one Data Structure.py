class AllOne(object):
    class Node():
        def __init__(self):
            self.keys = {}
            self.val = 1
            self.next = None
            self.prev = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.status = {}
        self.head = self.Node()
        self.head.val = 0
        self.tail = self.Node()
        self.tail.val = float('inf')
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.status:
            if self.head.next.val == 1:
                self.head.next.keys[key] = True
                self.status[key] = self.head.next
            else:
                node = self.Node()
                self.status[key] = node
                node.keys[key] = True
                node.next = self.head.next
                node.prev = self.head
                self.head.next.prev = node
                self.head.next = node
        else:
            node = self.status[key]
            val = self.status[key].val
            del node.keys[key]
            if node.next.val == val + 1:
                node.next.keys[key] = True
                self.status[key] = node.next
            else:
                newNode = self.Node()
                newNode.keys[key] = True
                newNode.val = val + 1
                newNode.next = node.next
                newNode.prev = node
                node.next.prev = newNode
                node.next = newNode
                self.status[key] = newNode
            if len(node.keys) == 0:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.status:
            return
        else:
            node = self.status[key]
            val = self.status[key].val
            del node.keys[key]
            if node.prev.val == val - 1:
                if val - 1 > 0:
                    node.prev.keys[key] = True
                    self.status[key] = node.prev
                else:
                    del self.status[key]
            else:
                newNode = self.Node()
                newNode.keys[key] = True
                newNode.val = val - 1
                newNode.next = node
                newNode.prev = node.prev
                node.prev.next = newNode
                node.prev = newNode
                self.status[key] = newNode
            if len(node.keys) == 0:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        else:
            return self.tail.prev.keys.items()[0][0]

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        else:
            return self.head.next.keys.items()[0][0]
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()