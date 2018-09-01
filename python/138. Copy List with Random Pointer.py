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
        if not head:
            return None
        root = RandomListNode(0)
        prev = root
        cur = head
        visited = {}
        while cur:
            if cur not in visited:
                visited[cur] = RandomListNode(cur.label)
            prev.next = visited[cur]
            if cur.random and cur.random not in visited:
                visited[cur.random] = RandomListNode(cur.random.label)
            if cur.random:
                visited[cur].random = visited[cur.random] 
            prev = visited[cur]
            cur = cur.next
        return root.next
        
