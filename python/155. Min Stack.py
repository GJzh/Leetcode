class MinStack(object):
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.mins = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        node = self.Node(x)
        node.next = self.head
        self.head = node
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)
        return
            

    def pop(self):
        """
        :rtype: void
        """
        if not self.head: return
        x = self.head.val
        self.head = self.head.next
        if x == self.mins[-1]:
            self.mins.pop()
        return
        

    def top(self):
        """
        :rtype: int
        """
        if self.head:
            return self.head.val
        else:
            return -1

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.mins) > 0:
            return self.mins[-1]
        else:
            return -1