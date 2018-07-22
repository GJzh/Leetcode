class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n :
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n - 1) / 2
        l = 0
        r = min(m, k)
        #start binarysearch
        while l < r:
            midNums1 = (l + r) / 2
            midNums2 = k - midNums1
            if nums1[midNums1] < nums2[midNums2]:
                l = midNums1 + 1
            else:
                r = midNums1
        # after binary search, we almost get the median because it must be between
        # these 4 numbers: A[l-1], A[l], B[k-l], and B[k-l+1] 
    
        # if (n+m) is odd, the median is the larger one between A[l-1] and B[k-l].
        # and there are some corner cases we need to take care of.
        a = max(nums1[l-1] if l > 0  else float('-inf'), nums2[k-l] if k-l >= 0 else float('-inf'))
        if (m + n) & 1 == 1:
            return a
        b = min(nums1[l] if l < m else float('inf'), nums2[k-l+1] if k-l+1 < n else float('inf'))
        return (a+b)/2.0


Solution：
class Solution:
    def _findMedianSortedArrays(self, idx1, idx2, k):
        m = len(self.nums1)
        n = len(self.nums2)
        if idx1 >= m: return self.nums2[idx2+k-1]
        if idx2 >= n: return self.nums1[idx1+k-1]
        if k == 1: return min(self.nums1[idx1], self.nums2[idx2])
        v1 = self.nums1[idx1 + k//2 - 1] if idx1 + k//2 - 1 < m else sys.maxsize
        v2 = self.nums2[idx2 + k//2 - 1] if idx2 + k//2 - 1 < n else sys.maxsize
        if v1 <= v2:
            return self._findMedianSortedArrays(idx1 + k//2, idx2, k - k//2)
        else:
            return self._findMedianSortedArrays(idx1, idx2 + k//2, k - k//2)
    
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        sum = m + n
        if sum&1 == 1: 
            return self._findMedianSortedArrays(0, 0, (m+n)//2+1)
        else:
            return (self._findMedianSortedArrays(0, 0, (m+n)//2) + self._findMedianSortedArrays(0, 0, (m+n)//2+1)) / 2

