import logging
import os
import sys


def custom_logger(logger):
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if 'DYNO' in os.environ:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:

        file_handler = logging.FileHandler('stattic.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
