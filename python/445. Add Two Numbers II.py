# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _addTwoNumbers(self, node1, node2, i, j):
        if i > j:
            nxt = self._addTwoNumbers(node1.next, node2, i-1, j)
            val = node1.val + self.carry
        else:
            if i == 0: return None
            else:
                nxt = self._addTwoNumbers(node1.next, node2.next, i-1, j-1)
                val = node1.val + node2.val + self.carry
        node = ListNode(val % 10)
        self.carry = val // 10
        node.next = nxt
        return node
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        m = n = 0
        self.carry = 0
        while node1: 
            node1 = node1.next
            m += 1
        while node2: 
            node2 = node2.next
            n += 1
        if m >= n:
            node = self._addTwoNumbers(l1, l2, m, n)
        else:
            node =  self._addTwoNumbers(l2, l1, n, m)
        if self.carry > 0:
            root = ListNode(self.carry)
            root.next = node
            return root
        else:
            return node

