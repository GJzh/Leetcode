class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.status = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.status:
            self.status[val] = []
        self.status[val].append(len(self.nums))
        self.nums.append((val, len(self.status[val])-1))
        return len(self.status[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.status or len(self.status[val]) == 0: return False
        idx = self.status[val][-1]
        self.status[val].pop()
        if idx == len(self.nums)-1:
            self.nums.pop()
        else:
            # exchange nums[idx] with nums[-1]
            self.nums[idx] = self.nums[-1]
            self.nums.pop()
            self.status[self.nums[idx][0]][self.nums[idx][1]] = idx
        
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx][0]