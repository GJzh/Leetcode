# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None: return True
        prev = None
        node1 = head
        node2 = head.next
        while node2 and node2.next:
            # reverse the first half
            temp = node1.next
            node1.next = prev
            prev = node1
            node1 = temp
            # move fast pointer
            node2 = node2.next.next
        # even
        if node2:
            node2 = node1.next
            node1.next = prev
        # odd
        else:
            node2 = node1.next
            node1  = prev
        while node1:
            if node1.val != node2.val: return False
            node1 = node1.next
            node2 = node2.next
        return True
