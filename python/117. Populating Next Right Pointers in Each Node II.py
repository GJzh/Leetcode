# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None: return
        node = root
        head = TreeLinkNode(0)
        cur = head
        while node:
            if node.left:
                cur.next = node.left
                cur = cur.next
            if node.right:
                cur.next = node.right
                cur = cur.next
            node = node.next
            if node == None:
                node = head.next
                cur = head
                head.next = None

