class Solution(object):
    def dfs(self, stones, pos, lastJump, visited):
        if pos == len(stones) - 1: return True
        if (pos, lastJump) in visited: return False
        i = pos + 1
        while i < len(stones):
            jump = stones[i] - stones[pos]
            if jump > lastJump + 1: break
            if jump >= lastJump - 1 and jump <= lastJump + 1:
                if self.dfs(stones, i, jump, visited):
                    return True
            i += 1
        visited[(pos, lastJump)] = True
        return False
        
    
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        # of jumps <= n-1
        jump_max <= n-1
        jump_max * (jumm_max+1) / 2 <= distance = stones[-1] => jump_max <= sqrt(2 * stones[-1])
        distance_max = (n-1) * n / 2 >= stones[-1]
        """
        n = len(stones)
        maxDistance = n * (n-1) / 2
        if maxDistance < stones[-1]: return False
        visited = {}
        return self.dfs(stones, 1, 1, visited)