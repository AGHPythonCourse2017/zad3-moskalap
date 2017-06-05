import ptvalidator.scripts.sentence_analyzer as sa


def test_sentence():
    sen_analzr = sa.SentenceAnalyzer()
    sentence = sen_analzr.create_sentence('Russia will attack USA with missiles')
    sentence.get_essential_hashtag()

    htgs = list(map(lambda x: x.text, sentence.essential_htgs))
    assert htgs[0] == 'USA'
    assert htgs[1] == 'missiles'


def test_sentence2():
    sen_analzr = sa.SentenceAnalyzer()
    sentence = sen_analzr.create_sentence('Adolf Hitler died in 1945')
    sentence.get_essential_hashtag()

    htgs = list(map(lambda x: x.text, sentence.essential_htgs))
    assert htgs[0] == '1945'
    subject = list(map(lambda x: x.text, sentence.get_subject()))
    assert subject[0] == 'Adolf'
    assert subject[1] == 'Hitler'
    hashtags = sentence.get_twitter_queries()
    assert ['#adolf', '#hitler', '#adolf #hitler', '#adolf #1945',
            '#hitler #1945', '#adolf #hitler #1945', 'Adolf Hitler died in 1945'] == hashtags


def test_sentence2():
    sen_analzr = sa.SentenceAnalyzer()
    sentence = sen_analzr.create_sentence('The Earth is flat.')
    sentence.get_essential_hashtag()

    htgs = list(map(lambda x: x.text, sentence.essential_htgs))
    assert htgs[0] == 'flat'
    subject = list(map(lambda x: x.text, sentence.get_subject()))
    assert subject[0] == 'Earth'

    hashtags = sentence.get_twitter_queries()
    assert ['#earth', '#earth #flat'] == hashtags[:2]
