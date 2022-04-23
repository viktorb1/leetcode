class Codec:
    
    def __init__(self):
        self.longtoshort = dict()
        self.shorttolong = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = "tinyurl.com/" + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        self.longtoshort[longUrl] = short_url
        self.shorttolong[short_url] = longUrl
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shorttolong[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))