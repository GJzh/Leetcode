class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        digit_1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        digit_11 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        digit_2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        numbers = ["", "Thousand", "Million", "Billion"]
        ans = []
        for i in range(3, -1, -1):
            base = 10 ** (3 * i)
            cur = num / base
            num %= base
            if cur == 0: continue
            if cur >= 100:
                ans.append(digit_1[cur/100])
                ans.append("Hundred")
            cur %= 100
            if cur >= 20:
                ans.append(digit_2[cur/10])
                cur %= 10
                if cur > 0: ans.append(digit_1[cur])
            elif cur >= 10:
                ans.append(digit_11[cur%10])
            elif cur > 0:
                ans.append(digit_1[cur])
            if i > 0: ans.append(numbers[i])
        return " ".join(ans)