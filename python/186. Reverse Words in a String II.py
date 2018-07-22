class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        n = len(str)
        for i in range(n//2):
            temp = str[i]
            str[i] = str[n-1-i]
            str[n-1-i] = temp
        left = 0
        right = 0
        while left < n:
            while right < n and str[right] != ' ':
                right += 1
            i = left
            j = right - 1
            for k in range((right-left+1)//2):
                temp = str[i]
                str[i] = str[j]
                str[j] = temp
                i += 1
                j -= 1
            right += 1
            left = right

