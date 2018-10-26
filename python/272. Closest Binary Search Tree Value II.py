# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, target, k, q):
        if node == None: return
        diff = abs(target - node.val)
        isCandidate = False
        if len(q) < k:
            heapq.heappush(q, (-diff, node.val))
            isCandidate = True
        elif diff < -q[0][0]:
            heapq.heappop(q)
            heapq.heappush(q, (-diff, node.val))
            isCandidate = True
        if isCandidate:
            self.dfs(node.left, target, k, q)
            self.dfs(node.right, target, k, q)
        elif node.val < target:
            self.dfs(node.right, target, k, q)
        else:
            self.dfs(node.left, target, k, q)
        return
    
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        q = []
        self.dfs(root, target, k, q)
        res = []
        while len(q):
            res.append(heapq.heappop(q)[1])
        return res