class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.status = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.status:
            self.status[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.status:
            pos = self.status[val]
            if pos != len(self.nums)-1:
                self.status[self.nums[-1]] = pos
                self.nums[pos] = self.nums[-1]
            self.nums.pop()
            del self.status[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.nums) == 0: return -1
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]
        