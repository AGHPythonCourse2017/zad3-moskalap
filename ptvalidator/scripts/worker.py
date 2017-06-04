import logging
import threading
from urllib.error import HTTPError


class GoogleSearchWorker(threading.Thread):
    def __init__(self, query, sources, container):
        threading.Thread.__init__(self)
        self.query = query
        self.container = container
        self.sources = sources

    def run(self):

        import google
        logging.info('GoogleCrawler started searching.')
        sources = google.search(self.query, num=25)
        try:

            for i in range(20):
                self.sources.append(GoogleWorker(next(sources), self.container, i))

        except HTTPError:
            print('upps')
        logging.info('GoogleCrawler recieved urls')
        logging.info('GoogleCrawler started to crawl websites')


class GoogleWorker(threading.Thread):
    """Class for extracting information form given list of sentences."""

    def __init__(self, url, results, index_no):
        threading.Thread.__init__(self)
        self.index_no = index_no
        self.site = url
        self.results = results

    def run(self):
        from newspaper.article import ArticleException
        logging.info('Google Worker started reading ' + self.site)
        from newspaper import Article
        from ptvalidator.scripts.information import GoogleProperties, Information
        prop = GoogleProperties(self.site, self.index_no)
        try:
            art = Article(self.site)
            art.download()
            art.parse()
            logging.info('Parsed an article from site ' + self.site)
            text = art.text.split(".")
            information = Information(text, prop)
            self.results.add_information(information)
        except ArticleException:
            pass


class TwitterWorker(threading.Thread):
    def __init__(self, query, key, results, mixed=True, popular=True, latest=True):
        threading.Thread.__init__(self)
        self.query = query
        self.key = key
        self.results = results
        self.mixed = mixed
        self.popular = popular
        self.latest = latest

    def run(self):
        from ptvalidator.scripts.information import TwitterProperties, Information

        def build_information(dict_post):
            props = TwitterProperties(dict_post['user']['name'], dict_post['created_at'], dict_post['retweet_count'],
                                      dict_post['favorite_count'],
                                      dict_post['user']['verified'], dict_post['user']['statuses_count'],
                                      dict_post['user']['followers_count'], dict_post['user']['friends_count'],
                                      str(dict_post['id']))
            text = dict_post['text']

            return Information(text, props)

        logging.info('Twitter Worker started reading ' + str(self.query))

        import twython
        APP_KEY = b'Mi0uNAofDBIPIAINAg4xDCVSBQAwXzguKA=='
        APP_SEC = b'EyUsVBYiOTcqO14RGwReGicqDB4XJRE+J0w5ODsSHFY9VxYUBQEvFDRbWgAYCicpF1I='
        ACC_TOK = b'VFlWXFRZXEFYTFQoKAc4DBYzKBUYGSJdBTkuLDQlVBsoPxITBRwKHCstCSASDDojIQI='
        ACC_TOK_SEC = b'KxswFVIzIgIrAB4KLBUlNy1XMi0ZXFgvGhg0CjsxW1kRWDk5I1gkP1UlLiww'
        from Crypto.Cipher import XOR
        import base64

        def decrypt(key_dec, ciphertext):
            cipher = XOR.new(key_dec)
            return cipher.decrypt(base64.b64decode(ciphertext))

        key = self.key
        logging.info('key = %s', key)
        twitter = twython.Twython(decrypt(key, APP_KEY).decode(), decrypt(key, APP_SEC).decode(),
                                  decrypt(key, ACC_TOK).decode(), decrypt(key, ACC_TOK_SEC).decode())
        tweets = []

        if self.popular:
            statuses = twitter.search(q='#' + self.query, count=150, result_type='popular')['statuses']
            logging.info('Downloaded ' + str(len(statuses)) + ' popular tweets for query ' + self.query)
            tweets += statuses

        if self.mixed:
            statuses = twitter.search(q='#' + self.query, count=150, result_type='mixed')['statuses']
            logging.info('Downloaded ' + str(len(statuses)) + ' mixed tweets for query ' + self.query)
            tweets += statuses

        if self.latest:
            statuses = twitter.search(q='#' + self.query, count=100, result_type='latest')['statuses']
            logging.info('Downloaded ' + str(len(statuses)) + ' latest tweets for query ' + self.query)
            tweets += statuses

        for tweet in tweets:
            self.results.add_information(build_information(tweet))
