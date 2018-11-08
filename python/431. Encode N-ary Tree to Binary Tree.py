"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:   
    
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if root == None: return None
        node = TreeNode(root.val)
        if len(root.children) == 0: return node
        if len(root.children): node.left = self.encode(root.children[0])
        cur = node.left
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right
        return node

    def _decode(self, root):
        if root == None: return []
        children = []
        cur = root
        while cur:
            children.append(Node(cur.val, self._decode(cur.left)))
            cur = cur.right
        return children
    
    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if data == None: return None
        children = self._decode(data)
        return children[0]
