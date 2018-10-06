# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, p):
        prev = None
        while p:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return prev
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        p1 = head
        p2 = head
        # find the node with the index (n+1)/2
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        p2 = p1.next
        # reverse the second-half
        p2 = self.reverseList(p2)
        p1.next = None
        p1 = head
        # merge the two lists
        while p2:
            temp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp