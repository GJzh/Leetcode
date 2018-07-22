# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        ll = {}
        if not head: return None
        root = RandomListNode(0)
        node = root
        while head:
            if head not in ll:
                cur = RandomListNode(head.label)
                ll[head] = cur
            if head.random not in ll:
                random = RandomListNode(head.random.label) if head.random else None
                ll[head.random] = random
            node.next = ll[head]
            node.next.random = ll[head.random]
            
            node = node.next
            head = head.next    
        return root.next

