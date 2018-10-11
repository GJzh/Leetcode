"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def dfs(self, node):
        '''
        :param: Node
        :return: head, tail
        '''
        head = node
        tail = node
        if node.left:
            head, node.left = self.dfs(node.left)
            node.left.right = node
            head.left = None
        if node.right:
            node.right, tail = self.dfs(node.right)
            node.right.left = node
            tail.right = None
        return head, tail
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None
        head, tail = self.dfs(root)
        tail.right = head
        head.left = tail
        return head