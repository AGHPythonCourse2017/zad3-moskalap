import ptvalidator.scripts.sentence_analyzer as sa


def test_sentence_parser():
    sentences = {
        'Donald Trump is president of USA' : {'subject': 'Donald Trump'},
        'Ariana Grande dies at manchester.' : {'subject' : 'Ariana Grande'},
        'World War II was in 1940' : {'subject': 'World War II'},
        'Audi is russian car' : {'subject': 'Audi'},
        'Short hair is cool' : {'subject': 'hair'},
        'Tram is the fastest vehicle' : {'subject': 'Tram'},
        'The sun is a star' : {'subject': 'sun'},
        'Yogurt is a dairy product' : {'subject': 'Yogurt'},
        'The US has the largest military in the world' : {'subject': 'US'},
        'Putin is a jerk' : {'subject': 'Putin'},
        'Vladimir Putin is a jerk' : {'subject': 'Vladimir Putin'},
        'Cats are better than dogs' : {'subject': 'Cats'},
        'May 22nd is the best day of the year' : {'subject': 'May 22nd'},

    }

    sentence_analyzer = sa.SentenceAnalyzer()
    for k in sentences.keys():
        assert sentence_analyzer.parse_sentence(k).subject == sentences[k]['subject']


