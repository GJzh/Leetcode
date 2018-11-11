from Queue import Queue
class Solution(object):
    def findShorestPath(self, target):
        n = int(math.ceil(math.log(target+1) / math.log(2)))
        if self.dp[target] > 0: return self.dp[target]
        if target == (1 << n) - 1: 
            self.dp[target] = n
            return self.dp[target]
        self.dp[target] = n + 1 + self.findShorestPath((1 << n) - 1 - target)
        for m in range(n-1):
            cur = (1 << (n-1)) - (1 << m)
            self.dp[target] = min(self.dp[target], n + m + 1 + self.findShorestPath(target - cur))
        return self.dp[target]
        
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = int(math.ceil(math.log(target+1) / math.log(2)))
        self.dp = [0] * (1 << n)
        self.findShorestPath(target)
        return self.dp[target]