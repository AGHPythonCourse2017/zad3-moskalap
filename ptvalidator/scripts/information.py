import logging


class Information:
    def __init__(self, text, properties):
        self.text = text
        self.properties = properties

    def get_credibility(self):
        return self.properties.count_credibility()


class Properties:
    def __init__(self):
        raise NotImplementedError('There is no implementation for this kind of crawler')

    def count_credibility(self):
        raise NotImplementedError('There is no implementation for this kind of crawler')


class TwitterProperties(Properties):
    def __init__(self, user_name, created_at, retweets, favorites, verified, statuses_count, followers, following, i_d):
        self.retweets = retweets
        self.favorites = favorites
        self.verified = verified
        self.statuses_count = statuses_count
        self.followers = followers
        self.following = following
        self.user_name = user_name
        self.created_at = created_at
        self.id = i_d

        self.source = 'twitter.com/statuses' + self.id

    def count_credibility(self):
        credibility = 0.0
        if self.verified:
            credibility += 1.0
        credibility += self.retweets / 1000.0
        credibility += self.favorites / 100.0
        credibility += self.statuses_count / 10000
        credibility += self.followers / 1000
        credibility += self.following / 10000

        return credibility

    def get_source(self):
        return self.source


class GoogleProperties(Properties):
    def __init__(self, source, index_no):
        self.source = source
        self.index_no = index_no

    def get_source(self):
        return self.source

    def count_credibility(self):
        cred = 10 / (self.index_no + 0.01)

        if 'dailymail' in self.source:
            cred *= 10
        if 'co.uk' in self.source:
            cred *= 2
        if 'wikipedia' in self.source:
            cred *= 15
        return cred


class CrawledDataContainer:
    def __init__(self):
        self.infos = []

    def add_information(self, information):
        self.infos.append(information)

    def filter_trash(self):
        logging.info('Rejecting trashes')
        new_list = list(filter(lambda x: len(x.text) > 15, self.infos))
        logging.info('Rejected %d trash infos', len(self.infos) - len(new_list))
        self.infos = new_list
