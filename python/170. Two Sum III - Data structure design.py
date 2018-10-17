class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.nums:
            self.nums[number] = 1
        else:
            self.nums[number] += 1
        
            
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num, count in self.nums.items():
            if value - num in self.nums and (value - num != num or count > 1):
                return True
        return False