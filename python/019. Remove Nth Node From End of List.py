# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = node2 = head
        for _ in range(n):
            node1 = node1.next
        if node1 == None:
            # remove head
            return head.next
        node1 = node1.next
        while node1:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next
        return head