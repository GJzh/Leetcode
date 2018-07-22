# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0: return []
        if n == 1: return lists[0]
        return self.mergeTwo(self.mergeKLists(lists[:n//2]), self.mergeKLists(lists[n//2:]))
        
    def mergeTwo(self, a, b):
        head = prev = ListNode(0)
        head.next = a
        while a and b:
            if b.val < a.val:
                #insert b into the front of a
                prev.next = b
                b = b.next
                prev.next.next = a
            else:
                a = a.next
            prev = prev.next
        if b:
            prev.next = b
        return head.next

