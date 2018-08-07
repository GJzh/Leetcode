class Codec:
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    long2short = {}
    short2long = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.long2short: 
            word = ""
            for i in range(6): word += self.s[random.randint(0, 61)]
            while word in self.short2long:
                word = ""
                for i in range(6): word += self.s[random.randint(0, 61)]
            self.long2short[longUrl] = word
            self.short2long[word] = longUrl
        return "http://tinyurl.com/" + self.long2short[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long[shortUrl[19:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
