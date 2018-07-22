class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N < 2: return
        k %= N
        if k == 0: return
        head = idx = 0
        temp1 = nums[0]
        for cnt in range(N):
            idx = (idx+k) % N
            temp2 = nums[idx]
            nums[idx] = temp1
            temp1 = temp2
            if(idx == head):
                head += 1
                idx = head
                temp1 = nums[idx]

