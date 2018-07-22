# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        parent = s = ListNode(0)
        node = s.next = head        
        while node != None:
            cnt = 0
            while True:
                node = node.next
                cnt += 1
                if cnt == k or node == None: break
            
            if cnt == k:
                # do reverse
                t = node
                temp = s.next
                self.reverseList(s,t, k)
                s = temp
        return parent.next

    def reverseList(self, s, t, k):
        node = s.next
        for i in range(k):
            temp = node.next
            node.next = t
            t = node
            node = temp
        s.next = t

