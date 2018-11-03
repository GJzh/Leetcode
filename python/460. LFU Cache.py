class LFUCache(object):
    class Node():
        def __init__(self, key, val, freq):
            self.key = key
            self.val = val
            self.freq = freq
            self.prev = None
            self.next = None
        
    def __init__(self, capacity):
        """
        :type capacity: int
        freqs[freq]: the last node with frequency = freq
        status: key -> node
        """
        self.capacity = capacity
        self.status = {}
        self.freqs = {}
        self.head = self.Node(0, 0, 0)
        self.tail = self.Node(0, 0, float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, prevNode, node):
        node.next = prevNode.next
        node.prev = prevNode
        prevNode.next.prev = node
        prevNode.next = node
        
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def upgrade(self, node):
        freq = node.freq
        node.freq += 1
        if self.freqs[freq] == node:
            if node.prev.freq == freq: self.freqs[freq] = node.prev
            else: del self.freqs[freq]
        if freq + 1 in self.freqs:
            self.remove(node)
            prevNode = self.freqs[freq + 1]
            self.insert(prevNode, node)
        else:
            if freq in self.freqs:
                self.remove(node)
                prevNode = self.freqs[freq]
                self.insert(prevNode, node)
        self.freqs[freq+1] = node
        return
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.status: return -1
        node = self.status[key]
        self.upgrade(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0 and self.head.next == self.tail: return
        if key not in self.status:
            node = self.Node(key, value, 1)
            self.status[key] = node
            if self.capacity == 0:
                startNode = self.head.next
                key = startNode.key
                freq = startNode.freq
                self.remove(startNode)
                del self.status[key]
                if startNode == self.freqs[freq]:
                    del self.freqs[freq]
                self.capacity += 1
            if 1 in self.freqs:
                self.insert(self.freqs[1], node)
            else:
                self.insert(self.head, node)
            self.freqs[1] = node
            self.capacity -= 1
        else:
            node = self.status[key]
            node.val = value
            self.upgrade(node)
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)