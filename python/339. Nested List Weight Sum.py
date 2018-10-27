Solution 1 (recursive) - time: O(# nestedInteger), e.g., [[1,1],2,[1,1]] -> 7
class Solution(object):
    def _depthSum(self, nestedList):
        if nestedList == None or len(nestedList) == 0: return 0, 0
        basicSum, weightSum = 0, 0
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                val = nestedInteger.getInteger()
                a, b = val, 0
            else:
                a, b = self._depthSum(nestedInteger.getList())
            basicSum += a
            weightSum += b
        return basicSum, weightSum + basicSum
    
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        _, res = self._depthSum(nestedList)
        return res