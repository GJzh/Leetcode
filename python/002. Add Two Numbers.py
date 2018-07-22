# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        cur = head 
        while l1 or l2:
            cnt = 0
            if l1: 
                cnt += l1.val
                l1 = l1.next
            if l2: 
                cnt += l2.val
                l2 = l2.next
            cnt += carry
            carry = cnt//10
            cnt %= 10
            cur.next = ListNode(cnt)
            cur = cur.next
            
        if carry: cur.next = ListNode(carry)
        return head.next

