from spacy.symbols import nsubj, VERB, NOUN, PROPN, root, neg, ADV

import spacy
import logging


class SentenceAnalyzerException(Exception):
    pass


class SentenceAnalyzer:
    class Sentence:
        def __init__(self, sentence_str, subject, verb, verbs, negated):
            self.sentence = sentence_str
            self.subject = subject
            self.verb = verb
            self.verbs = verbs
            self.negated = negated
        def get_opposite(self):
            if self.negated:
                list = self.sentence.split()
                list.pop(self.negated)



                return SentenceAnalyzer.Sentence(' '.join(list), self.subject, self.verb, self.verbs, False)

            else:
                list = self.sentence.split()
                index = list.index(self.verb)
                list.insert(index+1, 'not')
                return SentenceAnalyzer.Sentence(' '.join(list),self.subject,self.verb,self.verbs,index+1)



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
        verb = None
        for word in doc:
            if word.dep == nsubj and (word.pos == NOUN or word.pos == PROPN):
                subject_temp = word.text
            if word.pos == VERB and word.head.text == word.text:
                verb = word.text
        negated = False

        if not subject_temp or not verb:

            msg = ""
            for word in doc:
                msg+= str(('text', word.text, 'pos', word.pos_, 'dep', word.dep_, 'head', word.head.text))+'\n'
                logging.error(msg)
                raise SentenceAnalyzerException(msg)


        for word in doc:
            if word.head.text == subject_temp and word.pos == PROPN:
                subject_m+=word.text+' '
            if word.dep == neg and (word.head.text == verb or word.pos == ADV):
                negated = sentence.split().index(word.text)
        subject_m += subject_temp
        return self.Sentence(sentence,subject_m,verb,verb + sentence.split(verb)[1], negated)




