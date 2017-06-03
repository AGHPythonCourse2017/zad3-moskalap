import logging
from urllib.error import HTTPError

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class Crawler:
    def __init__(self, num_of_sources=25):
        self.num_of_sources = num_of_sources
        self.crawled = False

    def crawl(self, query):
        raise NotImplementedError('There is no implementation for this kind of crawler')

    def get_sources(self):
        if self.crawled:
            return self.crawled
        else:
            raise CrawlerException('not crawled yet')


class GoogleCrawler(Crawler):
    def crawl(self, query):
        from ptvalidator.scripts.news import CrawledDataContainer
        self.container = CrawledDataContainer()
        self.workers = []
        from ptvalidator.scripts.worker import GoogleWorker
        import google
        logging.info('GoogleCrawler started searching.')
        sources = google.search(query, num=self.num_of_sources)
        try:

            for i in range(self.num_of_sources):
                self.workers.append(GoogleWorker(next(sources), self.container, i))



        except HTTPError:
            print('upps')
        logging.info('GoogleCrawler recieved urls')
        logging.info('GoogleCrawler started to crawl websites')

        for worker in self.workers:
            worker.start()

        for worker in self.workers:
            worker.join()

        # At this moment we havea data in container
        return self.container

    def count_credibility(self, url):

        if str(url).find('gov') != -1:
            return 2
        if str(url).find('wikipedia') != -1:
            return 1.7
        if str(url).find('https') != -1:
            return 1
        return 0.9


class TwitterCrawler(Crawler):
    def crawl(self, queries):

        from ptvalidator.scripts.worker import TwitterWorker
        from ptvalidator.scripts.news import CrawledDataContainer
        self.workers = []
        self.container = CrawledDataContainer()

        for query in queries:
            logging.info('Create worker for query = ' + str(query))
            self.workers.append(TwitterWorker(query, self.container, True, True, True))

        for worker in self.workers:
            worker.start()

        for worker in self.workers:
            worker.join()
        return self.container


class FacebookCrawler:
    pass


class CrawlerException(Exception):
    pass
