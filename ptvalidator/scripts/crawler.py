import logging


class Crawler:
    """Class for crawling internet resources"""

    def __init__(self, num_of_sources=25):
        self.num_of_sources = num_of_sources
        self.crawled = False
        self.key = None

    def crawl(self, query):
        raise NotImplementedError('There is no implementation for this kind of crawler')

    def get_sources(self):
        if self.crawled:
            return self.crawled
        else:
            raise CrawlerException('not crawled yet')


class GoogleCrawler(Crawler):
    def crawl(self, queries):
        from ptvalidator.scripts.news import CrawledDataContainer
        from ptvalidator.scripts.worker import GoogleSearchWorker
        container = CrawledDataContainer()
        workers = []
        sources = []

        for query in queries:
            # for each query create worker, who receive websites to crawl
            workers.append(GoogleSearchWorker(query, sources, container))

        for worker in workers:
            worker.start()

        for worker in workers:
            worker.join()

        # at this moment we have a worker for each website, ready to start crawl website

        for worker in sources:
            # so let them crawl
            worker.start()

        for worker in sources:
            worker.join(5)

        # At this moment we have a data in container
        return container


class TwitterCrawler(Crawler):
    def crawl(self, queries):

        from ptvalidator.scripts.worker import TwitterWorker
        from ptvalidator.scripts.news import CrawledDataContainer
        workers = []
        container = CrawledDataContainer()

        for query in queries:
            logging.info('Create worker for query = ' + str(query))
            workers.append(TwitterWorker(query, self.key, container, True, True, True))

        for worker in workers:
            worker.start()

        for worker in workers:
            worker.join()
        return container


class FacebookCrawler:
    # TODO
    pass


class CrawlerException(Exception):
    pass
