# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = ListNode(0)
        prev.next = node
        while node.next:
            node.val = node.next.val
            node = node.next
            prev = prev.next
        prev.next = None

