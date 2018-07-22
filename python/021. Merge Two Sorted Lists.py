# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head= ListNode(0)
        prev = head
        prev.next = l1
        node1, node2 = l1, l2
        while node1 and node2:
            if node2.val < node1.val:
                temp = node2
                node2 = node2.next
                prev.next = temp
                prev.next.next = node1
                prev = prev.next
            else:
                node1 = node1.next
                prev = prev.next
        if node2: prev.next = node2
        return head.next

