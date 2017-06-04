import logging

from ptvalidator.scripts.crawler import GoogleCrawler, TwitterCrawler


class DataReceiver:
    def __init__(self, sentence, key):
        self.sentence = sentence
        self.google_crawler = GoogleCrawler()
        self.twitter_crawler = TwitterCrawler()
        self.twitter_crawler.key = key

    def get_data(self):
        tr = self.twitter_crawler.crawl(self.sentence.get_twitter_queries())
        gr = self.google_crawler.crawl(self.sentence.get_google_queries())
        logging.info('received ' + str(len(tr.infos) + len(gr.infos)) + ' source informations')
        return tr, gr
