class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        n = len(heights)
        stack = []
        res = 0
        for i in range(n):
            curheight = heights[i]
            if len(stack) == 0 or curheight > heights[stack[-1]]:
                stack.append(i)
            elif curheight == heights[stack[-1]]:
                stack[-1] = i
            else:
                while len(stack) > 0 and heights[stack[-1]] > curheight:
                    pos = stack[-1]
                    height = heights[pos]
                    stack.pop()
                    if len(stack) == 0: width = i
                    else: width = i - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(i)
        return res
