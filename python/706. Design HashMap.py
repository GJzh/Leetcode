class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.size = 1001
        self.hashMap = [None] * self.buckets

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        idx1 = key % self.buckets
        idx2 = key / self.buckets
        if self.hashMap[idx1] == None:
            self.hashMap[idx1] = [None] * self.size
        self.hashMap[idx1][idx2] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx1 = key % self.buckets
        idx2 = key / self.buckets
        if self.hashMap[idx1] != None and self.hashMap[idx1][idx2] != None:
            return self.hashMap[idx1][idx2]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        idx1 = key % self.buckets
        idx2 = key / self.buckets
        if self.hashMap[idx1] != None and self.hashMap[idx1][idx2] != None:
            self.hashMap[idx1][idx2] = None