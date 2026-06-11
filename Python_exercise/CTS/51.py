import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short] = url
        return short

    def get_url(self, short):
        return self.urls.get(short, "URL not found")

shortener = URLShortener()

short = shortener.shorten_url("https://google.com")

print("Short URL:", short)
print("Original URL:", shortener.get_url(short))