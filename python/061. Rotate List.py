# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        cnt = 0
        node = head
        tail = None
        while node:
            tail = node
            node = node.next
            cnt += 1
        k %= cnt
        if not k: return head
        node = head
        for i in range(cnt - k - 1):
            node = node.next
        newHead = node.next
        node.next = None
        tail.next = head
        head = newHead
        return head