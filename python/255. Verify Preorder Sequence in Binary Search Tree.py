Solution 1 - time: O(nlogn) space: O(1)
class Solution(object):    
    def _verifyPreorder(self, preorder, left, right, lowerBound, upperBound):
        # empty tree
        if left > right: return True
        cur = preorder[left]
        left += 1
        if cur < lowerBound or cur > upperBound: return False
        if left > right: return True
        idx = left
        while idx <= right and preorder[idx] < cur:
            idx += 1
        return self._verifyPreorder(preorder, left, idx-1, lowerBound, cur) and self._verifyPreorder(preorder, idx, right, cur, upperBound)
            
    
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        n = len(preorder)
        if n < 3: return True
        lowerBound, upperBound = float('-inf'), float('inf')
        return self._verifyPreorder(preorder, 0, n-1, lowerBound, upperBound)

Solution 2 - time: O(n) space: O(n)
class Solution(object):        
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        n = len(preorder)
        stack = []
        low = float('-inf')
        for val in preorder:
            if val < low: return False
            while len(stack) and val > stack[-1]:
                low = stack[-1]
                stack.pop()
            stack.append(val)
        return True

Solution 3 - time: O(n) space: O(1)
class Solution(object):        
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        n = len(preorder)
        low = float('-inf')
        idx = -1
        for val in preorder:
            if val < low: return False
            while idx >= 0 and val > preorder[idx]:
                low = preorder[idx]
                idx -= 1
            idx += 1
            preorder[idx] = val
        return True
