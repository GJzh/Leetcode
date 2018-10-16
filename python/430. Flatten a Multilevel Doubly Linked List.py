"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def _flatten(self, cur):
        if cur == None: return None, None
        node1, end1 = self._flatten(cur.child)
        node2, end2 = self._flatten(cur.next)
        cur.child = None
        if node1 == None and node2 == None:
            return cur, cur
        elif node1 == None:
            return cur, end2
        elif node2 == None:
            cur.next = node1
            node1.prev = cur
            return cur, end1
        else:
            cur.next = node1
            node1.prev = cur
            end1.next = node2
            node2.prev = end1
            return cur, end2   
    
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: return head
        self._flatten(head)
        return head