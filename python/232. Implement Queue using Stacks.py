class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.data:
            self.helper.append(self.data.pop())
        self.data.append(x)
        while self.helper:
            self.data.append(self.helper.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.data.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.data[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

