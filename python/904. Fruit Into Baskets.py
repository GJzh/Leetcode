class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        n = len(tree)
        if n == 0: return 0
        ans = 0
        types = {}
        left, right = 0, 0
        while right < n:
            while right < n and (len(types) < 2 or tree[right] in types):
                if tree[right] not in types:
                    types[tree[right]] = 1
                else:
                    types[tree[right]] += 1
                right += 1
            ans = max(ans, right - left)
            if right >= n: break
            while left < right and len(types) == 2:
                types[tree[left]] -= 1
                if types[tree[left]] == 0:
                    del types[tree[left]]
                left += 1
        ans = max(ans, right - left)
        return ans