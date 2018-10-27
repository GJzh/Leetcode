class PhoneDirectory(object):
    class Node():
        def __init__(self, num):
            self.num = num
            self.next = None
            
    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.head = node = self.Node(-1)
        self.numbers = {}
        for i in range(maxNumbers):
            node.next = self.Node(i)
            node = node.next
            self.numbers[i] = (node, True)

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.head.next == None:
            return -1
        node = self.head.next
        self.head.next = node.next
        node.next = None
        self.numbers[node.num] = (node, False)
        return node.num
        
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.numbers and self.numbers[number][1]
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number not in self.numbers or self.numbers[number][1] == True: return
        node = self.numbers[number][0]
        self.numbers[number] = (node, True)
        node.next = self.head.next
        self.head.next = node
        return