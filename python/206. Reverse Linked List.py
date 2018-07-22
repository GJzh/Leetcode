# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
Solution1: iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
Solution2: recursively
class Solution(object):
    def _reverseList(self, head):
        if not head.next: return head
        temp = head.next
        node = self._reverseList(head.next)
        temp.next = head
        head.next = None
        return node
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        return self._reverseList(head)

