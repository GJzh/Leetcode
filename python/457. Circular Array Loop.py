class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2: return False
        for i in range(n):
            if nums[i] == 0: continue
            prev = i
            cur = (i + nums[i]) % n
            cnt = 0
            while cnt < n:
                if nums[prev] * nums[cur] <= 0: break
                if prev == cur: nums[cur] = 0
                prev = cur
                cur = (cur + nums[cur] + n) % n
                cnt += 1
            if cnt == n: return True
            cur = i
            while nums[cur] != 0:
                prev = cur
                cur = (cur + nums[cur] + n) % n
                nums[prev] = 0
        return False