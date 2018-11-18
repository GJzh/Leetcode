import struct
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append(":")
            ans.append(s)
        return "".join(ans)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n == 0: return []
        idx = 0
        ans = []
        while idx < n:
            start = idx
            while idx < n and s[idx] != ":":
                idx += 1
            length = int(s[start:idx])
            idx += 1
            ans.append(s[idx:idx+length])
            idx += length
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))