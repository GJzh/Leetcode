# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        status = {}
        minIdx = 0
        if root == None: return []
        q = Queue()
        q.put((root, 0))
        while q.qsize() > 0:
            node, idx = q.get()
            minIdx = min(minIdx, idx)
            if idx not in status:
                status[idx] = [node.val]
            else:
                status[idx].append(node.val)
            if node.left:
                q.put((node.left, idx-1))
            if node.right:
                q.put((node.right, idx+1))
        res = [None] * len(status)
        for key, nums in status.items():
            res[key-minIdx] = status[key]
        return res