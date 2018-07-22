class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = right = 0
        n = len(chars)
        while right < n:
            cnt = 0
            c = chars[right]
            while right < n and chars[right] == c: 
                right += 1
                cnt += 1
            chars[left] = c
            left += 1
            if cnt >= 2:
                num = str(cnt)
                for i in range(len(num)):
                    chars[left] = num[i]
                    left += 1     
        return left

