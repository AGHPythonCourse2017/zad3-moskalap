import ptvalidator.scripts.sentence_analyzer as sa


def test_sentence_parser():
    sentences = {
        'Donald Trump is president of USA': {'subject': 'Donald Trump', 'verb': 'is',
                                             'predicate': 'is president of USA', 'negated':False},
        'Donald Trump is not president of USA': {'subject': 'Donald Trump', 'verb': 'is',
                                             'predicate': 'is not president of USA', 'negated': 3},

        'Ariana Grande dies at manchester terrorist attack': {'subject': 'Ariana Grande', 'verb': 'dies',
                                              'predicate': 'dies at manchester terrorist attack',  'negated':False},
        "Ariana Grande does not die at manchester terrorist attack": {'subject': 'Ariana Grande', 'verb': 'die',
                                              'predicate': 'die at manchester terrorist attack',  'negated':3},
        'World War II was in 1940': {'subject': 'World War II', 'verb': 'was', 'predicate': 'was in 1940', 'negated':False},
        'World War II was not in 1940': {'subject': 'World War II', 'verb': 'was', 'predicate': 'was not in 1940', 'negated':4},
        'Audi is russian car': {'subject': 'Audi', 'verb': 'is', 'predicate': 'is russian car', 'negated':False},
        'Short hair is cool': {'subject': 'hair', 'verb': 'is', 'predicate': 'is cool', 'negated':False},
        'Tram is the fastest vehicle': {'subject': 'Tram', 'verb': 'is', 'predicate': 'is the fastest vehicle', 'negated':False},
        'The sun is a star': {'subject': 'sun', 'verb': 'is', 'predicate': 'is a star', 'negated':False},
        'Yogurt is a dairy product': {'subject': 'Yogurt', 'verb': 'is', 'predicate': 'is a dairy product', 'negated':False},
        'The Russia, which is the largest country, has not the largest military in the world': {'subject': 'Russia',
                                                                                            'verb': 'has',
                                                                                            'predicate': 'has not the largest military in the world', 'negated':8},
        'Putin is not a jerk': {'subject': 'Putin', 'verb': 'is', 'predicate': 'is not a jerk', 'negated':2},
        'Vladimir Putin is a jerk': {'subject': 'Vladimir Putin', 'verb': 'is', 'predicate': 'is a jerk', 'negated':False},
        'Cats are better than dogs': {'subject': 'Cats', 'verb': 'are', 'predicate': 'are better than dogs', 'negated':False},
        'May 22nd is the best day of the year': {'subject': 'May 22nd', 'verb': 'is',
                                                 'predicate': 'is the best day of the year', 'negated':False},

    }

    sentence_analyzer = sa.SentenceAnalyzer()
    for k in sentences.keys():
        sentence = sentence_analyzer.parse_sentence(k)

        assert sentence.subject == sentences[k]['subject']
        assert sentence.verb == sentences[k]['verb']
        assert sentence.verbs == sentences[k]['predicate']
        assert sentence.negated == sentences[k]['negated']
