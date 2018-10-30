"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import struct
class Codec:
    def _serialize(self, node):
        self.data += struct.pack('i', node.val)
        self.data += struct.pack('i', len(node.children))
        for child in node.children:
            self._serialize(child)
        return
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        if root == None: return ""
        self.data = ""
        self._serialize(root)
        return self.data
        
    def _deserialize(self, data):
        val = struct.unpack('i', data[self.idx:self.idx+4])[0]
        childrenNum = struct.unpack('i', data[self.idx+4:self.idx+8])[0]
        self.idx += 8
        children = []
        for i in range(childrenNum):
            children.append(self._deserialize(data))
        return Node(val, children)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if data == "": return None
        self.idx = 0
        return self._deserialize(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))