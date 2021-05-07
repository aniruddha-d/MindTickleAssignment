

import logging


def init_logging(path='results/automation.log', loglevel='INFO'):
    logging.basicConfig(format='%(asctime)s ::: %(pathname)s,%(lineno)d :::  %(levelname)s ::: %(message)s',
                        filename=path, level=loglevel.upper())


