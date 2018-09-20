class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n :
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n + 1) / 2
        l = 0
        r = m
        #start binarysearch
        while l <= r:
            partitionX = (l + r) / 2
            partitionY = k - partitionX
            maxLeftX = nums1[partitionX-1] if partitionX > 0 else float('-inf')
            maxLeftY = nums2[partitionY-1] if partitionY > 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < m else float('inf')
            minRightY = nums2[partitionY] if partitionY < n else float('inf')
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) & 1 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            elif maxLeftX > minRightY:
                r = partitionX - 1
            else:
                l = partitionX + 1
