class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        the collected rain at position x: max(min(leftBars[x-1],right[x+1]) - height[x], 0)
        leftBars[x]: the highest bar between 0 and x
        rightBars[x]: the highest bar between x and n-1
        """
        n = len(height)
        if n < 3: return 0
        leftBars = [0] * n
        rightBars = [0] * n
        leftBars[0] = height[0]
        rightBars[n-1] = height[n-1]
        for i in range(1, n):
            leftBars[i] = max(leftBars[i-1], height[i])
        for i in range(n-2, -1, -1):
            rightBars[i] = max(rightBars[i+1], height[i])
        res = 0
        for k in range(1, n-1):
            res += max(0, min(leftBars[k-1], rightBars[k+1]) - height[k])
        return res