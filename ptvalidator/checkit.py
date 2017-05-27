import ptvalidator.scripts.sentence_analyzer as sa


def test_sentence():
    verbs =  sentence.find_verbs()
    verbs = list(verbs)
    a = verbs[0].text
    print(a)

def checker():
    import ptvalidator.scripts.crawler as crawler
    import ptvalidator.scripts.data_manager as crawler
    crawler = crawler.GoogleCrawler('andrzej duda żyje', 50)
    crawler.crawl()

    map = crawler.get_sources()

    for k in map.keys():
        print (str(k).split('//',1)[1].split('/',1)[0] +':'+ str(map[k]))

def datamng():
    import ptvalidator.scripts.data_manager as dm
    from ptvalidator.scripts.sentence_analyzer import SentenceAnalyzer
    menage = dm.DataManager(SentenceAnalyzer('Ariana Grande died'))
    a = menage.get_result()

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    datamng()
