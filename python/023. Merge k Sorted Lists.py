# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
Solution 1: recursive, time O(nlogK), space(O(1))
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

Solution 2: iterative, time: O(nlogK), space(O(1))
class Solution(object):
    def mergeTwo(self, list1, list2):
        head = ListNode(0)
        prev = head
        head.next = list1
        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
                prev.next.next = list1
                prev = prev.next
            else:
                prev = list1
                list1 = list1.next
                
        if list2:
            prev.next = list2
        return head.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        step = 1
        while step < n:
            for i in range(0, n - step, 2 * step):
                lists[i] = self.mergeTwo(lists[i], lists[i+step])
                lists[i+step] = None
            step *= 2
        return lists[0]