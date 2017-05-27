class Crawler:
    class GoogleCrawler:
        pass
    class TwitterCrawler:
        pass
    class FacebookCrawler:
        pass

    def __init__(self, google_crawl = True, twitter_crawl = False, fb_crawl = False):
        if google_crawl:
            self.google = self.GoogleCrawler()
        if twitter_crawl:
            self.twitter = self.TwitterCrawler()
        if fb_crawl:
            self.facebook = self.FacebookCrawler()

