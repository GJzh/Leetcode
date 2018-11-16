class Solution(object):
    def helper(self, nums):
        n = len(nums)
        if n == 0: return False
        if n == 1: 
            return True if abs(nums[0] - 24) < self.epsilon else False
        for i in range(n-1):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                res = [a + b, a - b, b - a, a * b]
                # check division
                if abs(b) > self.epsilon: res.append(1.0 * a / b)
                if abs(a) > self.epsilon: res.append(1.0 * b / a)
                cur = nums[:i] + nums[i+1:j] + nums[j+1:]
                for num in res:
                    cur.append(num)
                    if self.helper(cur):
                        return True
                    cur.pop()
        return False
        
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.epsilon = 10 ** (-8)
        return self.helper(nums)