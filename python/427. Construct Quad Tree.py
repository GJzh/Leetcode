"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def build(self, grid, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2: return Node(grid[x1][y1], True, None, None, None, None)
        midX = (x1 + x2) / 2
        midY = (y1 + y2) / 2
        topLeft = self.build(grid, x1, y1, midX, midY)
        topRight = self.build(grid, x1, midY+1, midX, y2)
        bottomLeft = self.build(grid, midX+1, y1, x2, midY)
        bottomRight = self.build(grid, midX+1, midY+1, x2, y2)
        node = Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val and node.topLeft.val != None:
            node.val = node.topLeft.val
            node.isLeaf = True
            node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None
        return node
        
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        m = len(grid)
        n = len(grid[0])
        return self.build(grid, 0, 0, m-1, n-1)