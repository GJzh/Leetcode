Solution 1:
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        self.queue[self.start]: the current front
        self.queue[self.end]: the next available position
        start == end -> queue is full
        start == -1 -> queue is empty
        """
        self.queue = [None] * k
        self.start = -1
        self.end = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # queue if full
        if self.start == self.end: return False
        self.queue[self.end] = value
        if self.start == -1: self.start = 0
        self.end = (self.end + 1) % len(self.queue)
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.start < 0: return False
        self.start = (self.start + 1) % len(self.queue)
        # queue is empty
        if self.start == self.end: 
            self.start = -1
            self.end = 0
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.start >= 0:
            return self.queue[self.start]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.start < 0: return -1
        idx = (len(self.queue) + self.end - 1) % len(self.queue)
        return self.queue[idx]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.start < 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.start == self.end

Solution 2:
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        self.queue[self.start]: the current front
        self.queue[self.end]: the current end
        start == end -> queue is full
        start == -1 -> queue is empty
        """
        self.queue = [None] * k
        self.start = -1
        self.end = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # queue if full
        cur = (self.end + 1) % len(self.queue)
        # queue is full
        if cur == self.start: return False
        self.end = cur
        self.queue[self.end] = value
        if self.start == -1: self.start = 0
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.start < 0: return False
        # only one element before deQueue
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % len(self.queue)
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.start >= 0:
            return self.queue[self.start]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.end < 0: return -1
        return self.queue[self.end]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.start < 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.start == (self.end + 1) % len(self.queue)