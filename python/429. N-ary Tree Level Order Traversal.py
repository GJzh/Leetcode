"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from Queue import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None: return []
        q = Queue()
        q.put((root, 0))
        ans = []
        while q.qsize():
            cur, level = q.get()
            if level == len(ans):
                ans.append([])
            ans[level].append(cur.val)
            for node in cur.children:
                q.put((node, level+1))
        return ans