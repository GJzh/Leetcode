Solution1:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def dfs(self, node, idx):
        res = str(node.val) + " " + str(idx) + " "
        if node.left: res += self.dfs(node.left, 2 * idx)
        if node.right: res += self.dfs(node.right, 2 * idx + 1)     
        return res
    
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        return self.dfs(root, 1)
        
    def _deserialize(self, q):
        n = len(q)
        node = TreeNode(q[self.pos][0])
        idx = q[self.pos][1]
        if self.pos+1 < n and q[self.pos+1][1] == 2 * idx:
            self.pos += 1
            node.left = self._deserialize(q)
        if self.pos+1 < n and q[self.pos+1][1] == 2 * idx + 1:
            self.pos += 1
            node.right = self._deserialize(q)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.pos = 0
        q = []
        n = len(data)
        if n == 0: return None
        i = 0
        while i < n:
            temp = ""
            while i < n and data[i] != ' ':
                temp += data[i]
                i += 1
            i += 1
            val = int(temp)
            temp = ""
            while i < n and data[i] != ' ':
                temp += data[i]
                i += 1
            i += 1
            idx = int(temp)
            q.append((val, idx))
        return self._deserialize(q)

Solution 2:
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

