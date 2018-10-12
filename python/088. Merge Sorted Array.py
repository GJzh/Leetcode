class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m-1
        idx2 = n-1
        idx = m + n - 1
        while idx2 >= 0:
            if idx1 < 0 or nums2[idx2] > nums1[idx1]:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
                idx -= 1
            else:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
                idx -= 1