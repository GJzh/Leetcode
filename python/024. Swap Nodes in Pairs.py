# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        helper = node = ListNode(0)
        node.next = head
        while node.next and node.next.next:
            temp = node.next
            node.next = node.next.next
            temp.next = node.next.next
            node.next.next = temp
            node = node.next.next
        return helper.next

