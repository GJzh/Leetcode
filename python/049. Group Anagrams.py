class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        status = {}
        res = []
        for s in strs:
            key = ''.join(sorted(s))
            if key not in status:
                status[key] = len(res)
                res.append([s])
            else:
                res[status[key]].append(s)
        return res
        
