# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = prev = ListNode(0)
        root.next = head
        tail = head
        for _ in range(m-1):
            prev = prev.next
            tail = tail.next
        node = tail.next
        for _ in range(n-m):
            tail.next = node.next
            node.next = prev.next
            prev.next = node
            node = tail.next
        return root.next
