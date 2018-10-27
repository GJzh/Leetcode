# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        node = head
        while node:
            if node.val == 9:
                stack.append(node)
            else:
                stack = [node]
            node = node.next
        carry = 1
        while len(stack):
            node = stack[-1]
            stack.pop()
            val = node.val + carry
            node.val = val % 10
            carry = val / 10
        if carry > 0:
            node = ListNode(1)
            node.next = head
            head = node
        return head