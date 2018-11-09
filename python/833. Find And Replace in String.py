class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        cur = 0
        ans = ""
        replaces = [(indexes[i], sources[i], targets[i]) for i in range(len(indexes))]
        replaces.sort()
        for i in range(len(replaces)):
            idx, source, target = replaces[i]
            if S[idx:idx+len(source)] == source:
                ans += S[cur:idx]
                ans += target
                cur = idx + len(source)
        ans += S[cur:]
        return ans