# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        prev = ListNode(0)
        prev.next = node
        while node:
            if node.next == head: return True
            temp = node.next
            node.next = prev
            prev = node
            node = temp    
        return False

