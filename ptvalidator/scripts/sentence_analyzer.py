from spacy.symbols import nsubj, VERB
import spacy


class SentenceAnalyzer:
    from enum import Enum

    class Category(Enum):
        PERSON = 1
        COUNTRIES = 2
        BUILDINGS = 3

    def __init__(self, sentence):


        nlp = spacy.load('en')
        self.sentence = nlp(sentence)

    def find_verbs(self):

        verbs = set()
        for possible_subject in self.sentence:
            if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                verbs.add(possible_subject.head)
        return verbs
    def find_subject(self):
        subject = set()
        for possible_subject in self.sentence:
            if possible_subject.dep == nsubj:
                subject.add(possible_subject)
        return subject

    def_



if __name__ == '__main__':

    sa = SentenceAnalyzer('yesterday donald become president')
    v =sa.find_subject()
    print(v)