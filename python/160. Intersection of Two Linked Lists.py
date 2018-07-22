# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        m = n = 0
        while nodeA:
            nodeA = nodeA.next
            m += 1
        while nodeB:
            nodeB = nodeB.next
            n += 1
        if m > n:
            for i in range(m-n): headA = headA.next
        if n > m:
            for i in range(n-m): headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

