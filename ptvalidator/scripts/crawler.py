import numpy as np
import logging

logging.basicConfig( level=logging.DEBUG,
format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class Crawler:
    def __init__(self, sentence, num_of_sources=10):
       self.sentence = sentence
       self.num_of_sources = num_of_sources
       self.crawled = False


    def crawl(self):
        raise NotImplementedError('There is no implementation for this kind of crawler')
    def get_sentences(self):
        if self.crawled:
            return self.crawled
        else:
            raise CrawlerException('not crawled yet')

class GoogleCrawler(Crawler):

    def crawl(self):
        self.crawled = {}
        import google
        logging.info('started searching')
        sources = google.search(self.sentence, num=self.num_of_sources)
        logging.info('finished searching')
        weight = self.num_of_sources

        for i in range(self.num_of_sources):

            url = next(sources)
            logging.info('site: ' + url)
            self.crawled[url] = (url, self.count_credibility(url) * weight/self.num_of_sources)
            weight-=1
        logging.info('end crawling')

    def count_credibility(self, url):

        if str(url).find('gov') != -1:
            return 1.00
        if str(url).find('wikipedia') != -1:
            return 0.9
        if str(url).find('https')!= -1:
            return 0.7
        return 0.4


class TwitterCrawler:
    pass


class FacebookCrawler:
    pass
class CrawlerException(Exception):
    pass