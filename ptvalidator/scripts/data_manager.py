import logging

import ptvalidator.scripts.sentence_analyzer as sa


class DataManager:
    def __init__(self, basic_sentence, container):
        self.basic_sentence = basic_sentence
        self.workers = []
        self.sentence_analyzer = sa.SentenceAnalyzer()
        self.container = container

    def verify_information(self):

        self.container.filter_trash()
        similarities = []

        saa = sa.SentenceAnalyzer()
        bs_obj = self.basic_sentence
        logging.info('Essentials hashtags : ', bs_obj.essential_htgs)
        for info in self.container.infos:
            for sentence in info.text:
                newsen_obj = saa.create_sentence(sentence)
                simil = saa.compare_sentence(bs_obj, newsen_obj)
                if simil > 0.2:
                    logging.info('sim: %f %s', simil, newsen_obj.doc_sentence.string)
                    similarities.append(
                        {'info': newsen_obj.doc_sentence.string, 'credibility': info.properties.count_credibility(),
                         'src': info.properties.get_source()})

        if len(similarities) > 5:
            res = Result(True)
        else:
            res = Result(False)

        for info in similarities:
            res.add_source(info['info'], info['src'])

        return res


class Result:
    def __init__(self, is_true):
        self.is_true = is_true
        self.sources = []

    def add_source(self, text, src):
        self.sources.append((text, src))

    def display_sources(self):
        for (text, src) in self.sources:
            print(text + ' ~ ' + src.split('//')[1].split('/')[0] + '( ' + src + ' )')
