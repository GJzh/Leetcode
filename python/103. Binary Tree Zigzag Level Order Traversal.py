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
        cur = [root]
        flag = False
        res = [[root.val]]
        while len(cur) > 0:
            temp = []
            while len(cur) > 0:
                node = cur.pop()
                if flag:
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
                else:
                    if node.right: temp.append(node.right)
                    if node.left: temp.append(node.left)
            nums = []
            for node in temp:
                nums.append(node.val)
            if len(nums) > 0:
                res.append(nums)
            flag = not flag
            cur = temp
        return res

