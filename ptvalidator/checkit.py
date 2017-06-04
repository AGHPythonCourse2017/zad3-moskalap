import ptvalidator.scripts.sentence_analyzer as sa
from ptvalidator.scripts.data_manager import DataManager
from ptvalidator.scripts.datarecievier import DataReceiver


def validate(query, key, verbose_log=True):
    import logging
    if verbose_log:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(level=logging.FATAL)
    nsa = sa.SentenceAnalyzer()
    sen = nsa.create_sentence(query)
    dr = DataReceiver(sen, key)
    tup = dr.get_data()
    a, b = tup
    a.infos += b.infos
    dm = DataManager(sen, a)
    res = dm.verify_information()

    return res
