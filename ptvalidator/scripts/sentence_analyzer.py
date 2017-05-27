from spacy.symbols import nsubj, VERB, NOUN, PROPN
import spacy
import logging

class SentenceAnalyzer:
    class Sentence:
        def __init__(self, sentence_str, subject, predicate, verbs):
            self.sentence = sentence_str
            self.subject = subject
            self.predicate = predicate
            self.verbs = verbs
        def get_similar(self):
            pass

        def find_verbs(self):

            verbs = set()
            for possible_subject in self.sentence:
                if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                    verbs.add(possible_subject.head)
            return verbs

        def get_subject(self):
            subject = set()
            for possible_subject in self.sentence:

                if possible_subject.dep == nsubj:
                    subject.add(possible_subject)

            subject = list(subject)
            returns = subject[0].text
            if len(subject) > 1:
                returns += ' ' + subject[1].text

            return returns

        def get_category(self):
            return 'person'

        def get_string(self):
            return self.sentence_s

    def __init__(self):

        logging.info('init sentence analyzer')
        self.nlp = spacy.load('en')

    def parse_sentence(self, sentence):
        doc = self.nlp(sentence)
        subject_temp = None
        subject_m = ""
        for word in doc:
            #print('text', word.text, 'pos', word.pos_, 'dep', word.dep_, 'head', word.head.text)
            if word.dep == nsubj:
                subject_temp = word.text
        if not subject_temp:
            for word in doc:
                print('text', word.text, 'pos', word.pos_, 'dep', word.dep_, 'head', word.head.text)


        for word in doc:
            if word.head.text == subject_temp and word.pos == PROPN:
                subject_m+=word.text+' '
        subject_m += subject_temp
        return self.Sentence(sentence,subject_m,"","")




