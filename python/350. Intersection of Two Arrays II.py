Solution 1:
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.intersect(nums2, nums1)
        visited = {}
        for num in nums1:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1
        res = []
        for num in nums2:
            if num in visited and visited[num] > 0:
                res.append(num)
                visited[num] -= 1
        return res

Solution 2:
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.intersect(nums2, nums1)
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        res = []
        while p1 < n1 and p2 < n2:
            if nums1[p1] == nums2[p2]:
                cur = nums1[p1]
                while p1 < n1 and p2 < n2 and nums1[p1] == nums2[p2] and nums1[p1] == cur:
                    res.append(cur)
                    p1 += 1
                    p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res