# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import struct
class Codec:
    def _serialize(self, node):
            if node == None:
                return
            else:
                self.res = self.res + struct.pack('i', node.val)
                self._serialize(node.left)
                self._serialize(node.right)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        self.res = ""
        self._serialize(root)
        return self.res
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit(s, left, right):
            if self.pos == len(s): return None
            val = struct.unpack('i', s[self.pos:self.pos+4])[0]
            if val < left or val > right: return None
            node = TreeNode(val)
            self.pos += 4
            node.left = doit(s, left, val)
            node.right = doit(s, val, right)
            return node
            
        self.pos = 0
        return doit(data, -sys.maxint-1, sys.maxint)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))