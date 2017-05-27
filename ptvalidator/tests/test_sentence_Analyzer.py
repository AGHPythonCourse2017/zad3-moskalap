import ptvalidator.scripts.sentence_analyzer as sa
sentence = sa.SentenceAnalyzer('donald trump is president of usa')

def test_sentence():
    verbs =  sentence.find_verbs()
    verbs = list(verbs)
    assert verbs[0].lower_ == 'is'