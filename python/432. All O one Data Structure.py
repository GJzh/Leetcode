class AllOne(object):
    class Node():
        def __init__(self, val):
            self.val = val
            self.keys = {}
            self.prev = None
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.status = {}
    def addHead(self):
        node = self.Node(1)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.Node(1)
            self.tail = self.head
            
    def remove(self, key, node):
        del node.keys[key]
        if len(node.keys) == 0:
            if node == self.head:
                self.head = self.head.next
            elif node == self.tail:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            del node
            
    def upgrade(self, key, node):
        if node == self.tail:
            self.tail = self.Node(node.val+1)
            self.tail.keys[key] = True
            self.tail.prev = node
            node.next = self.tail
            newNode = self.tail
        else:
            if node.next.val == node.val+1:
                node.next.keys[key] = True
                newNode = node.next
            else:
                newNode = self.Node(node.val+1)
                newNode.keys[key] = True
                newNode.prev = node
                newNode.next = node.next
                node.next.prev = newNode
                node.next = newNode
        self.remove(key, node)
        return newNode
        
    def degrade(self, key, node):
        if node == self.head:
            self.head = self.Node(node.val-1)
            self.head.keys[key] = True
            self.head.next = node
            node.prev = self.head
            newNode = self.head
        else:
            if node.prev.val == node.val-1:
                node.prev.keys[key] = True
                newNode = node.prev
            else:
                newNode = self.Node(node.val-1)
                newNode.keys[key] = True
                newNode.prev = node.prev
                newNode.next = node
                node.prev.next = newNode
                node.prev = newNode
        self.remove(key, node)
        return newNode
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.status:
            if self.head == None or self.head.val != 1:
                self.addHead()
            self.head.keys[key] = True
            self.status[key] = self.head
        else:
            self.status[key] = self.upgrade(key, self.status[key])

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.status:
            return
        else:
            if self.status[key].val == 1:
                self.remove(key, self.status[key])
                del self.status[key]
            else:
                self.status[key] = self.degrade(key, self.status[key])
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail:
            return self.tail.keys.keys()[0]
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head:
            return self.head.keys.keys()[0]
        else:
            return ""