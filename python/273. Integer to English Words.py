class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        diction = ["Billion", "Million", "Thousand", ""];
        digits_10 = ["", "", "Twenty", "Thirty", "Forty", "Fifty",  "Sixty", "Seventy", "Eighty", "Ninety"]
        digits_1 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                    "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        res = ""
        while num > 0: 
            for i in range(4):
                base = 10 ** (9 - 3 * i)
                val = num // base
                if val > 0:
                    hundreds = val // 100
                    residual = val % 100
                    val_10 = residual // 10
                    val_1 = residual % 10 if residual >= 10 and residual < 20 else -1
                    val_0 = residual % 10
                    if hundreds > 0:
                        res += digits[hundreds]
                        res += " Hundred "
                    if val_1 >= 0:
                        res += digits_1[val_1]
                        res += " "
                    else:
                        if val_10:
                            res += digits_10[val_10]
                            res += " "
                        if val_0:
                            res += digits[val_0]
                            res += " "
                    
                    res += diction[i]
                    res += " "
                    
                num %= base
            
        i = len(res)-1
        while i >= 0 and res[i] == " ":
            i -= 1
        return res[:i+1]

