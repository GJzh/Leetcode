Solution 1:
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0: return []
        nums.sort()
        res = []
        i = 0
        while i <= n-4:
            a = nums[i]
            if target - a < 3 * a: break
            j = i+1
            while j <= n-3:
                b = nums[j]
                e = target - a - b
                left, right = j + 1, n - 1
                if e < 2 * b: break
                while left < right:
                    if nums[left] + nums[right] == e:
                        res.append([a, b, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                    elif nums[left] + nums[right] < e:
                        left += 1
                    else:
                        right -= 1
                while j <= n-3 and nums[j] == b: j += 1
            while i <= n-4 and nums[i] == a: i += 1
        return res

Solution 2:
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0: return []
        nums.sort()
        status = {}
        res = set()
        for i in range(n-1):
            for j in range(i+1, n):
                sum2 = nums[i] + nums[j]
                if sum2 not in status: status[sum2] = []
                status[sum2].append((i,j))
        for i in range(n-3):
            for j in range(i+1,n-2):
                t = target - nums[i] - nums[j]
                if t not in status: continue
                for x, y in status[t]:
                    if x > j: res.add((nums[i], nums[j], nums[x], nums[y]))
        res = [list(item) for item in res]
        return res