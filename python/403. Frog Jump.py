class Solution(object):
    def dfs(self, stones, idx, last_jump, max_jump, status):
        if idx == len(stones)-1: return True
        for i in range(idx+1, len(stones)):
            jump = stones[i] - stones[idx]
            if jump > max_jump: break
            if jump >= last_jump-1 and jump <= last_jump+1 and (idx, jump) not in status:
                if self.dfs(stones, i, jump, max_jump, status):
                    return True
                else:
                    status[(idx, jump)] = True
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
        max_distance = (n-1) * n / 2
        if max_distance < stones[-1]: return False
        max_jump = min(n-1, math.sqrt(2 * stones[-1]) + 1)
        status = {}
        return self.dfs(stones, 1, 1, max_jump, status)