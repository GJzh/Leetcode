class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        status = {}
        res = []
        for num1 in nums1:
            status[num1] = 1
        for num2 in nums2:
            if num2 in status:
                status[num2] = 2
        for key, value in status.items():
            if value == 2:
                res.append(key)
        return res
        
