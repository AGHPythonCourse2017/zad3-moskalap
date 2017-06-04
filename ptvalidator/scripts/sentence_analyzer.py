import logging

import spacy
from spacy.symbols import nsubj, NOUN, PROPN, dobj, iobj, pobj, nsubjpass, acomp


class SentenceAnalyzerException(Exception):
    pass


class SentenceAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en')

    @staticmethod
    def compare_sentence(basic_sentence, other_sentence):
        hashtags = list(map(lambda x: x.lemma_, basic_sentence.essential_htgs))
        words_basic = list(map(lambda x: x.lemma_, basic_sentence.doc_sentence))
        required = basic_sentence.required_ht
        matched = 0
        matched_htgs = 0
        all_words = 0.01
        for word in other_sentence.doc_sentence:
            if word.lemma_ in hashtags:
                matched_htgs += 1
                matched += 1
            elif word.lemma_ in words_basic:
                matched += 1
            all_words += 1

        if matched_htgs < required:
            return 0.0
        else:
            return matched / all_words

    def create_sentence(self, sentence_string):
        return Sentence(self.nlp(sentence_string))


class Sentence:
    def __init__(self, doc_sentence, subject=None):
        if subject is None:
            subject = []
        self.doc_sentence = doc_sentence
        self.essential_htgs = []
        self.required_ht = 0
        self.subject = subject

    def get_subject(self):
        subject_temp = None
        for word in self.doc_sentence:
            print(word, word.dep_, word.pos_)
            if (word.dep == nsubjpass or word.dep == nsubj) and (word.pos == NOUN or word.pos == PROPN):
                subject_temp = [word]

        if subject_temp:
            for word in self.doc_sentence:
                if word.head.text == subject_temp[0].text and word.pos == PROPN:
                    subject_temp = [word] + subject_temp

        return subject_temp

    def get_essential_hashtag(self):
        if not self.essential_htgs:
            for word in self.doc_sentence:
                if word.text.isdigit():
                    self.essential_htgs.append(word)
                elif word.dep == pobj:
                    self.essential_htgs.append(word)
                elif word.dep == iobj:
                    self.essential_htgs.append(word)
                elif word.dep == dobj:
                    self.essential_htgs.append(word)
                elif word.dep == acomp:
                    self.essential_htgs.append(word)
            if len(self.essential_htgs) > 4:
                self.required_ht = 2
            elif len(self.essential_htgs) != 0:
                self.required_ht = 1

    def get_google_queries(self):
        subjs = list(map(lambda x: x.lemma_, self.get_subject()))

        self.get_essential_hashtag()
        for es in self.essential_htgs:
            subjs = list(map(lambda x: x + ' ' + es.lemma_, subjs))

        subjs = [self.doc_sentence.string] + subjs
        logging.info('google queries ' + str(subjs))
        return subjs[:5]

    def get_twitter_queries(self):
        subjs = list(map(lambda x: '#' + x.lemma_, self.get_subject()))
        if len(subjs) > 1:
            subjs.append(' '.join(subjs))

        self.get_essential_hashtag()
        for es in self.essential_htgs:
            subjs += list(map(lambda x: x + ' #' + es.lemma_, subjs))

        subjs.append(self.doc_sentence.string)
        logging.info('twitter queries = ' + str(subjs))
        return subjs
