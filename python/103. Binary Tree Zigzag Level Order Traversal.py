# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        res = []
        cur = [root]
        flag = True
        while len(cur) > 0:
            temp = []
            res.append([])
            if flag:
                for i in range(len(cur)): res[-1].append(cur[i].val)
            else:
                for i in range(len(cur)-1,-1,-1): res[-1].append(cur[i].val)
            for node in cur:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            cur = temp
            flag = not flag
        return res